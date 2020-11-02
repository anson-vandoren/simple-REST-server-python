# Simple REST server example

This example shows the very basics of setting up REST endpoints to interface between a HTML/Javascript UI and some form of control code living on a server. This sample is NOT INTENDED for any sort of production environment, only to demonstrate the concepts involved.

## Getting started

Clone the repository with `git clone https://github.com/anson-vandoren/simple-REST-server-python.git`

### Prepare the backend server

```sh
$ cd server
$ pip install -r requirements.txt
$ ./start_server.sh
```

### Start a basic local webserver for the client page

```sh
$ cd ../client
$ python -m http.server
```

### Open the UI and test

In any browser, navigate to `http://localhost:8000`