# redditish server

## Setup

- Clone the [client](https://github.com/ammarbinfaisal/redditish-client)
- Install the dependencies with `pip install -r requirements.txt`
- Setup a mysql database

## Running the server

- `export DBUSER=<your db user>`
- `export DBPASS=<your db password>`
- `cd app`
- `../venv/bin/gunicorn app:main`
