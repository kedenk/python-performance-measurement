import time

performance_measurements = {}
PERF_ENABLED = (os.getenv('PERF_ENABLED') or 'false') in ['true', 'True', '1']


def performance_measurement(method):

    def wrapper_func(*args, **kwargs):

        # start timer
        if PERF_ENABLED:
            tstart = time.perf_counter()
            methodName = method.__name__
            args = [a for a in args]

        # invoke actual method
        retval = method(*args, **kwargs)

        # stop timer
        if PERF_ENABLED:
            tend = time.perf_counter()
            print("Method '{}' time: {}. Parameter: {}".format(methodName, str((tend - tstart)), args))
            json_repr = {
                "method": methodName,
                "time": str(tend - tstart),
                "args": args
            }
            performance_measurements[time.time()] = json_repr

        return retval
    return wrapper_func


def get_perf_measurements():
    return performance_measurements


def enable_perf_measurement():
    global PERF_ENABLED
    PERF_ENABLED = True


def disable_perf_measurement():
    global PERF_ENABLED
    PERF_ENABLED = False
