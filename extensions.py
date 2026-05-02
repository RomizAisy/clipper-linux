import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
import redis
from rq import Queue


db = SQLAlchemy()
migrate = Migrate()
mail = Mail()


# ---------------- REDIS QUEUE ----------------
redis_conn = redis.Redis.from_url(
    os.getenv("REDIS_URL", "redis://redis:6379/0")
)

clipper_queue = Queue(
    "clipper",
    connection=redis_conn,
    default_timeout=7200  # long video jobs
)