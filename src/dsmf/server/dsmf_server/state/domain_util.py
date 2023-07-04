import heapq as hq
import math

from dsmf_server.state.domain_state import DomainState


class DomainUtil(object):
    @classmethod
    def route_network(cls, fr: str, to: str) -> [str]:
        # index, index -> weight
        graph: [[(int, int)]] = [[(DomainUtil.index_of(y), 1) for y in x.reachable] for x in
                                 DomainState.config.networks]
        t = DomainUtil.index_of(to)

        # Perform dijkstra on graph with start node "to"
        path, weights = DomainUtil.dijkstra(graph, t)

        # Now traverse the path to get our result. Each element in the path array refers to the node index closer to the
        # destination node on the shortest path.
        s = DomainUtil.index_of(fr)
        ret = []
        while s != t:
            ret.append(DomainState.config.networks[s].name)
            s = path[s]
        ret.append(DomainState.config.networks[t].name)

        # Return the resulting dumped data. Will contain elements [fr, ..., to]
        return ret

    @classmethod
    def index_of(cls, net: str) -> int:
        i = 0
        for network in DomainState.config.networks:
            if network.name == net:
                return i
            i += 1
        return -1

    @classmethod
    # https://stackoverflow.com/a/56740241
    def dijkstra(cls, graph: list[list[(int, int)]], s: int):
        n = len(graph)
        visited = [False] * n
        weights = [math.inf] * n
        path = [None] * n
        queue = []
        weights[s] = 0
        hq.heappush(queue, (0, s))
        while len(queue) > 0:
            g, u = hq.heappop(queue)
            visited[u] = True
            for v, w in graph[u]:
                if not visited[v]:
                    f = g + w
                    if f < weights[v]:
                        weights[v] = f
                        path[v] = u
                        hq.heappush(queue, (f, v))
        return path, weights
