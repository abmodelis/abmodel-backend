# API of ABMODEL course platform

This is the API of ABMODEL course platform.

# Pre-requisites

- [Python 3.11+](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/)

# Installation

## Create virtual environment

**Only using python 3.11+**
+ Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```
+ Linux/Mac:
```bash
python3 -m venv .venv
.venv/bin/activate
```
Using [anaconda](https://docs.anaconda.com/anaconda/install/)
```bash
conda create -n abmodel python=3.11
conda activate abmodel
```

Using [Pyenv](https://github.com/pyenv/pyenv).
The `.python-version` file should be in the root of the project, this file activates the virtual environment automatically, you can run `pyenv activate abmodel` to activate manually the virtual environment. 
```bash
pyenv install 3.11.8
pyenv virtualenv 3.11.8 abmodel
```

## Install dependencies
```bash
pip install -r requirements.txt
```

## Database configuration (PostgreSQL)
* Copy .env.example to .env
* Set env variables in .env
```properties
DB_USER=your_username
DB_PASS=your_password
DB_NAME=your_dbname
DB_HOST=localhost # or your db host for example: domain-db.com
DB_PORT=5432
```

## Run migrations
It will create the tables if they do not exist, It requires the database to be running.
```bash
alembic upgrade head
```

## Run server
```bash
uvicorn app:api --reload
```
Now you can visit http://127.0.0.1:8000/

You can also visit http://127.0.0.1:8000/docs/ or http://127.0.0.1:8000/redoc/ for API documentation

For more details, please visit https://fastapi.tiangolo.com

