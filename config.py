"""Config file for configurate SQL Alchemy."""
import pathlib

BASE_DIR = pathlib.Path(__file__).parent.absolute()


class Config:
    """Config object for settings database."""

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' +\
        str(BASE_DIR / "data" / "db.sqlite3")
    SQLALCHEMY_TRACK_MODIFICATION = False
    SECRET_KEY = 'you-will-never-know'
