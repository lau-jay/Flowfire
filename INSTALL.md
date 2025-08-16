# Flowfire installation
 
The Flowfire library is intended for use by Python developers.

Several ways to get/use Flowfire:

* Pip - `pip install Flowfire`
* Git - `git clone https://github.com/lau-jay/Flowfire`
* Zipped source code - Download [github.com/lau-jay/Flowfire/archive/master.zip](https://github.com/lau-jay/Flowfire/archive/master.zip)

## Installation with Pip

The safe way to install and upgrade the Flowfire library:

    pip install --user --upgrade Flowfire

Flowfire supports many backends as Redis, ZeroMQ, RabbitMQ, MongoDB, PostgreSQL, Google Cloud and many others.
Flowfire is usually used with a subset of the available backends, and installing the dependencies of all backends is not required. 
Thus, to minimize the number of dependencies, the backend dependencies are optional, but easy to install.

See the file [`setup.py`](https://github.com/lau-jay/Flowfire/blob/master/setup.py#L60)
for the exhaustive list of these *extra* dependencies.

* Install all optional dependencies  
  To install Flowfire along with all optional dependencies in one bundle:

        pip install --user --upgrade Flowfire[all]

* Arctic backend  
  To install Flowfire along with [Arctic](https://github.com/man-group/arctic/) in one bundle:

         pip install --user --upgrade Flowfire[arctic]

* Google Cloud Pub / Sub backend

         pip install --user --upgrade Flowfire[gcp_pubsub]

* Kafka backend

         pip install --user --upgrade Flowfire[kafka]

* MongoDB backend

         pip install --user --upgrade Flowfire[mongo]

* PostgreSQL backend

         pip install --user --upgrade Flowfire[postgres]

* QuasarDB backend  
  To install Flowfire along with [QuasarDB](https://quasar.ai/) in one bundle:

         pip install --user --upgrade Flowfire[quasardb]

* RabbitMQ backend

         pip install --user --upgrade Flowfire[rabbit]

* Redis backend

          pip install --user --upgrade Flowfire[redis]

* ZeroMQ backend

         pip install --user --upgrade Flowfire[zmq]

