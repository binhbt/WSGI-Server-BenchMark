# WSGI server benchmark Result test with Flask
```

+-------------+       +-----------------------+           +--------------+     +-----------+
|             |       |                       |           |              |     |           |
|    nginx    +-------+  gunicorn/uwsgi/bjoern+-----------+  flask app   +-----+   redis   |
|             |       |                       |           |              |     |           |
+-------------+       +-----------------------+           +--------------+     +-----------+

```

## Environments setup

please install `docker` and `docker-compose`.

```sh
$ docker version
Client:
 Version:	17.12.0-ce
 API version:	1.35
 Go version:	go1.9.2
 Git commit:	c97c6d6
 Built:	Wed Dec 27 20:03:51 2017
 OS/Arch:	darwin/amd64

Server:
 Engine:
  Version:	17.12.0-ce
  API version:	1.35 (minimum version 1.12)
  Go version:	go1.9.2
  Git commit:	c97c6d6
  Built:	Wed Dec 27 20:12:29 2017
  OS/Arch:	linux/amd64
  Experimental:	true
$ docker-compose version
docker-compose version 1.18.0, build 8dd22a9
docker-py version: 2.6.1
CPython version: 2.7.12
OpenSSL version: OpenSSL 1.0.2j  26 Sep 2016
```

## Quick start

### build and up

```sh
$ docker-compose build
$ docker-compose up -d
Starting dockercomposeflask_redis_1 ... done
Starting dockercomposeflask_web_1 ... done
Starting dockercomposeflask_nginx_1 ... done
```

Check the service running information

```sh
$ docker-compose ps
           Name                         Command               State           Ports
--------------------------------------------------------------------------------------------
dockercomposeflask_nginx_1   /usr/sbin/nginx                  Up      0.0.0.0:80->80/tcp
dockercomposeflask_redis_1   docker-entrypoint.sh redis ...   Up      6379/tcp
dockercomposeflask_web_1     /runserver.sh                    Up      0.0.0.0:8000->8000/tcp
```

Check the web service

```sh
$ curl 127.0.0.1/gunicorn
Hello gunicorn World! I have been seen 1 times and my hostname is 09ad15ad1b51.
$ curl 127.0.0.1/uwsgi
Hello uwsgi World! I have been seen 2 times and my hostname is 09ad15ad1b51.
$ curl 127.0.0.1/bjoern
Hello bjoern World! I have been seen 3 times and my hostname is 09ad15ad1b51.
```

### stop the service

```sh
$ docker-compose stop
Stopping dockercomposeflask_nginx_1 ... done
Stopping dockercomposeflask_web_1   ... done
Stopping dockercomposeflask_redis_1 ... done


### Result Test  on Digital Ocean 2CPU -4G RAM  


```
![gunicorn result](https://raw.githubusercontent.com/binhbt/WSGI-Server-BenchMark/master/bench_gunicorn.png)   

![uwsgi result](https://raw.githubusercontent.com/binhbt/WSGI-Server-BenchMark/master/bench_uwsgi.png)  

![bjoern result](https://raw.githubusercontent.com/binhbt/WSGI-Server-BenchMark/master/bench_bjoern.png)  


### Bjoern winner - Awsome
