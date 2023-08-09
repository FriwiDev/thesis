import json
import sys
from threading import Thread

from esmf_client.model.slice import Slice
from host_client.esmf_communicator import ESMFCommunicator
from host_client.test_slice import TestSlice

NUM_TESTS = 10


def main():
    # Validate that file input exists
    if len(sys.argv) <= 1:
        print("Please specify a configuration file: python3 -m host_client <config>.json <IPERF|SOCKPERF|UDP_PING>")
        exit(1)

    # Determine test suite
    if len(sys.argv) <= 2:
        print("Please specify a test suite: IPERF, UDP_PING or SOCKPERF")
        exit(1)
    suite = sys.argv[2].upper()
    if suite != "IPERF" and suite != "SOCKPERF" and suite != "UDP_PING":
        print("Invalid test suite specified. Available: IPERF, UDP_PING or SOCKPERF")
        exit(1)

    # Load our config
    f = open(sys.argv[1], 'r')
    config: dict = json.load(f)
    f.close()

    # Build our slice list
    if "slices" not in config.keys():
        print("Error: No slices in config!")
        exit(1)

    slices: [TestSlice] = [TestSlice(x) for x in config["slices"]]

    localhost: str = config["host_name"]
    requested_slices: [Slice] = []

    esmf_data = str(config["esmf"]).split(":") if "esmf" in config.keys() else ["None"]
    ip = esmf_data[0]
    port = 8080
    if len(esmf_data) > 1:
        port = int(esmf_data[1])

    # Should we create slices?
    if "request_slices" in config.keys() and config["request_slices"]:
        for sl in slices:
            rsl, rsl_rev = sl.get_slices(localhost)
            if rsl:
                requested_slices.append(rsl)
            if rsl_rev:
                requested_slices.append(rsl_rev)
        consume_slices = ESMFCommunicator.request_slice(requested_slices, ip, port)
        if consume_slices:
            print("Successfully created all slices!")
        else:
            print("Error while creating slices!")
            exit(1)

        for sl in slices:
            sl.cosume_slices(localhost, consume_slices)

        if len(consume_slices) > 0:
            print("Somehow slices were left over after configuring! Something went horribly wrong!")
            exit(1)

    # Run our tests as server
    server_threads = []
    for sl in slices:
        thread = Thread(target=run_test_server, args=(sl, localhost, suite))
        thread.start()
        server_threads.append(thread)

    # Run our tests as client
    result = {}
    for i in range(0, NUM_TESTS):
        time_result = {}
        # Run all tests in new threads
        threads = []
        for sl in slices:
            # Check if there is a reverse slice
            target = None
            if "reverse_max_rate" not in sl.data.keys() or int(sl.data["reverse_max_rate"]) <= 0:
                # No reverse slice
                target = run_test_client
            else:
                # We have both: reverse slice and our slice
                if suite == "SOCKPERF":
                    # Reverse slices are not supported anyways
                    target = run_test_client
                elif suite == "IPERF":
                    # We need to test both -> alternate
                    target = run_test_client_bidir_consecutive
                elif suite == "UDP_PING":
                    # Test is always bidirectional here
                    target = run_test_client
            thread = Thread(target=target, args=(sl, localhost, suite, time_result))
            thread.start()
            threads.append(thread)
        # Wait on all tests to finish
        for thread in threads:
            thread.join()
        result[i] = time_result

    # Write results
    f = open(f"results_{config['host_name']}_{suite.lower()}.json", "w+")
    json.dump(result, f)
    f.close()

    # Should we remove slices?
    if "request_slices" in config.keys() and config["request_slices"]:
        if ESMFCommunicator.delete_slice([x.slice_id for x in requested_slices], ip, port):
            print("Successfully removed all slices!")
        else:
            print("Error while removing slices!")
            exit(1)

    # Wait on server threads (forever most likely)
    for thread in server_threads:
        thread.join()

    exit(0)


def run_test_client(sl: TestSlice, localhost: str, suite: str, time_result: dict):
    res = sl.test_slice_client(localhost, False, suite)
    if res:
        time_result[sl.name] = res


def run_test_client_reverse(sl: TestSlice, localhost: str, suite: str, time_result: dict):
    rev_res = sl.test_slice_client(localhost, True, suite)
    if rev_res:
        time_result[sl.name + "_reverse"] = rev_res


def run_test_client_bidir_consecutive(sl: TestSlice, localhost: str, suite: str, time_result: dict):
    run_test_client(sl, localhost, suite, time_result)
    run_test_client_reverse(sl, localhost, suite, time_result)


def run_test_server(sl: TestSlice, localhost: str, suite: str):
    sl.test_slice_server(localhost, suite)
