# Project setup

Make sure you are at backend directory and follow the instructions

## virtual env
Create a new virtual env and activate
```
python3 -m venv venv

source venv/bin/activate
```

## install the dependencies

```
pip install -r requirements.txt
```

## start the server 
```
uvicorn main:app
```

Go to http://localhost:8000/docs and see the documentation.

