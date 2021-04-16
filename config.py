"""Config file for configurate SQL Alchemy."""
import os
import pathlib

BASE_DIR = pathlib.Path(__file__).parent.absolute()


class Config:
    """Config object for settings database."""

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' +\
        str(BASE_DIR / "data" / "db.sqlite3")
    SQLALCHEMY_TRACK_MODIFICATION = False
    SECRET_KEY = 'you-will-never-know'
    HEROKU_DATABASE_URI = 'postgres://vqfvdbikupidyn:e5d02493ddd4543f985348d07830478fdd5332fad24ae5516f386f7f3e5f9f41@ec2-34-242-89-204.eu-west-1.compute.amazonaws.com:5432/d66antqhhhtk6v'
