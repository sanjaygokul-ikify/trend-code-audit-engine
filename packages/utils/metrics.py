import time

def collect_metrics(start_time):
    elapsed_time = time.time() - start_time
    return {'elapsed_time': elapsed_time}