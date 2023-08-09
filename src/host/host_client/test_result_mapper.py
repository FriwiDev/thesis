from host_client.test_utilities import iperf3, sockperf, udp_ping


class TestResultMapper(object):
    @classmethod
    def map_test_result(cls, result: iperf3.TestResult or sockperf.TestResult or udp_ping.TestResult) -> dict:
        if isinstance(result, sockperf.TestResult):
            return {"min_latency": result.min_latency,
                    "max_latency": result.max_latency,
                    "mean_latency": result.mean_latency,
                    "jitter_ms": result.jitter_ms,
                    "dropped_packets": result.dropped_messages,
                    "duplicated_packets": result.duplicated_messages,
                    "out_of_order_packets": result.out_of_order_messages}
        elif isinstance(result, udp_ping.TestResult):
            return {
                "latency_ms": result.latency_ms,
                "loss": result.loss,
                "loss_rev": result.loss_rev,
                "lost_messages": result.lost_messages,
                "lost_messages_rev": result.lost_messages_rev,
                "bps": result.bps,
                "bps_rev": result.bps_rev
            }
        else:
            if result.protocol:
                if result.protocol == "TCP":
                    return {"bps_sent": result.sent_bps,
                            "bps_received": result.received_bps,
                            "retransmits": result.retransmits,
                            "min_rtt": result.min_rtt,
                            "max_rtt": result.max_rtt,
                            "mean_rtt": result.mean_rtt}
                else:
                    return {"bps_sent": result.bps,
                            "loss": result.lost_percent,
                            "jitter_ms": result.jitter_ms}
            else:
                return {}
