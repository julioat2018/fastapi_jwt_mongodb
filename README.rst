What for
----------
This project is a realworld backend based on fastapi+mongodb. It can be used as a sample backend or a sample fastapi project with mongodb.


Quickstart
----------
Then run the following commands to bootstrap your environment with ``poetry``: ::

    git clone https://github.com/julioat2018/fastapi-jwt-mongodb
    cd fastapi-jwt-mongodb
    poetry install
    poetry shell

Then create ``.env`` file (or rename and modify ``.env.example``) in project root and set environment variables for application: ::

    touch .env
    echo "PROJECT_NAME=FastAPI APP" >> .env
    echo DATABASE_URL=mongo://$MONGO_USER:$MONGO_PASSWORD@$MONGO_HOST:$MONGO_PORT/$MONGO_DB >> .env
    echo SECRET_KEY=$(openssl rand -hex 32) >> .env
    echo ALLOWED_HOSTS='"127.0.0.1", "localhost"' >> .env

To run the web application in debug use::

    uvicorn app.main:app --reload


Web routes
----------

All routes are available on ``/docs`` or ``/redoc`` paths with Swagger or ReDoc.


Project structure
-----------------

Files related to application are in the ``app`` directory. ``alembic`` is directory with sql migrations.
Application parts are:

::

    models  - pydantic models that used in crud or handlers
    crud    - CRUD for types from models (create new user/article/comment, check if user is followed by another, etc)
    db      - db specific utils
    core    - some general components (jwt, security, configuration)
    api     - handlers for routes
    main.py - FastAPI application instance, CORS configuration and api router including


Todo
----
1) Add more unit test
