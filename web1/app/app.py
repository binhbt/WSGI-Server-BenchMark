# Copyright 2018 Cisco Systems, Inc.
# All rights reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import os
import socket

from flask import Flask
from redis import Redis


app = Flask(__name__)
redis = Redis(host=os.environ.get('REDIS_HOST', 'redis'), port=6379)


@app.route('/bjoern')
def hello():
    redis.incr('hits')
    return 'Hello Bjoern World! I have been seen %s times and my hostname is %s.\n' % (redis.get('hits'),socket.gethostname())

import bjoern
bjoern.run(app, '0.0.0.0', 8000, reuse_port=True)
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