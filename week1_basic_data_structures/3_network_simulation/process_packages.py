# python3

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []

    def process(self, request):
        if not self.finish_time:
            self.finish_time.append(request.time_to_process)
            return Response(False, request.arrived_at)
        comp_time = self.finish_time[-1]
        if request.arrived_at >= self.finish_time[0]:
            self.finish_time.pop(0)
        if len(self.finish_time) < self.size:
            comp_time = max(comp_time, request.arrived_at)
            self.finish_time.append(comp_time + request.time_to_process)
            return Response(False, comp_time)
        if request.arrived_at >= self.finish_time[-1]:
            comp_time = max(comp_time, request.arrived_at)
            self.finish_time.append(comp_time + request.time_to_process)
            return Response(False, comp_time)
        return Response(True, -1)


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
