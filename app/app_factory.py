from flask import Flask
from redis import Redis
from configs import app_config

class App(Flask):
    redis: Redis = None

def create_flask_app_with_configs() -> App:
    app = App(__name__)

    app.config.update(app_config.model_dump())

    app.redis = Redis(
        host=app_config.REDIS_HOST,
        port=app_config.REDIS_PORT,
        db=app_config.REDIS_DB,
        username=app_config.REDIS_USERNAME,
        password=app_config.REDIS_PASSWORD,
        ssl=app_config.REDIS_USE_SSL,
        decode_responses=True,
        socket_connect_timeout=3
    )

    try:
        app.redis.ping()
    except Exception as e:
        raise RuntimeError(f"Failed to connect to Redis: {str(e)}") from e

    return app

def create_app() -> App:
    app = create_flask_app_with_configs()
    return app
