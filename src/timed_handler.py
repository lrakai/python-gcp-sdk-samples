import time


class timed_handler(object):
    @staticmethod
    def time_handler(handler, event, context):
        start = time.time()

        result = handler(event, context)

        end = time.time()
        print(end - start)

        return result