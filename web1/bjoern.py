import bjoern
from app.app import app
if __name__ == '__main__':
    bjoern.run(app, '0.0.0.0', 8000)
    # bjoern.listen(app, '0.0.0.0', 8000)
    # bjoern.run()
    NUM_WORKERS = 8
    worker_pids = []
    for _ in range(NUM_WORKERS):
        pid = os.fork()
        if pid > 0:
            # in master
            worker_pids.append(pid)
        elif pid == 0:
            # in worker
            try:
                bjoern.run()
            except KeyboardInterrupt:
                pass
            exit()
    try:
    # Wait for the first worker to exit. They should never exit!
    # Once first is dead, kill the others and exit with error code.
        pid, xx = os.wait()
        worker_pids.remove(pid)
    finally:
        for pid in worker_pids:
            os.kill(pid, signal.SIGINT)
            exit(1)