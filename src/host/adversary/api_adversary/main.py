import json
import multiprocessing as mp
import sys
import time

import esmf_client
from api_adversary.esmf_communicator import ESMFCommunicator
from esmf_client.apis.tags import slice_management_api
from esmf_client.model.endpoint import Endpoint
from esmf_client.model.slice import Slice


def main():
    # Validate that cmd args are present
    if len(sys.argv) <= 2:
        print("Please specify an destination for traffic and a mode: "
              "python3 -m api_adversary <config>.json <VALID|INVALID>")
        exit(1)

    # Load our config
    f = open(sys.argv[1], 'r')
    config: dict = json.load(f)
    f.close()

    num_requests = config["num_req"]
    print_every_num = config["print_every"]

    test = sys.argv[2]
    if test.upper() == "VALID":
        body = Slice(
            slice_id=0,
            min_rate=50000,
            max_rate=100000,
            burst_rate=120000,
            latency=3,
            tunnel_id=0,
            transport_protocol="UDP",
            fr=Endpoint(config["fr"]),
            to=Endpoint(config["to"])
        )
        startt = time.time()
        for i in range(0, num_requests):
            my_slices = ESMFCommunicator.request_slice([body], config["esmf"])
            if my_slices:
                ESMFCommunicator.delete_slice([x.slice_id for x in my_slices], config["esmf"])
            if (i + 1) % print_every_num == 0:
                print(f"Sent {i + 1} requests")
        print(f"Sent {num_requests} requests in {time.time() - startt} seconds")
    elif test.upper() == "INVALID":
        startt = time.time()
        pool = mp.Pool(mp.cpu_count())
        pool.starmap(send_invalid_requests, [(i, int(num_requests / mp.cpu_count()))
                                             for i in range(mp.cpu_count())])
        print(f"Sent {int(num_requests / mp.cpu_count()) * mp.cpu_count()} requests in {time.time() - startt} seconds")
    else:
        print("Invalid mode given. Supported modes are VALID and INVALID!")
        exit(1)


def send_invalid_requests(tid, num_requests):
    # Load our config in this context because multiprocessing doesnt support it
    f = open(sys.argv[1], 'r')
    config: dict = json.load(f)
    f.close()

    print_every_num = config["print_every"]

    body = Slice(
        slice_id=0,
        min_rate=50000,
        max_rate=100000,
        burst_rate=120000,
        latency=3,
        tunnel_id=0,
        transport_protocol="UDP",
        fr=Endpoint(config["fr"]),
        to=Endpoint(config["to"])
    )

    print(f"[{tid}] Created thread to spam {num_requests} requests")
    for i in range(num_requests):
        if i % print_every_num == 0:
            print(f"[{tid}] Send request {str(i)}")
        configuration = esmf_client.Configuration(
            host="http://" + config["esmf"] + ":" + str(8080) + "/v1"
        )
        with esmf_client.ApiClient(configuration) as api_client:
            api_instance = slice_management_api.SliceManagementApi(api_client)

            query_params = {
                'auth': "someinvalidauth",
            }
            try:
                api_instance.slice_put(
                    query_params=query_params,
                    body=[body]
                )
            except BaseException:
                continue
