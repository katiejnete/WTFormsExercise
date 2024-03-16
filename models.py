"""Models for adopt."""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


def connect_db(app):
    with app.app_context():
        db.app = app
        db.init_app(app)


class Pet(db.Model):
    """Pet Model."""

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)
    species: Mapped[str] = mapped_column(nullable=False)
    photo_url: Mapped[str] = mapped_column(nullable=True)
    age: Mapped[int] = mapped_column(nullable=True)
    notes: Mapped[str] = mapped_column(nullable=True)
    available: Mapped[bool] = mapped_column(nullable=False, default=True)
