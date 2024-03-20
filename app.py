"""Adopt application."""

from flask import Flask, render_template, redirect, request, flash
from models import db, connect_db, Pet
from forms import AddPetForm


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///adopt"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "38432084"

connect_db(app)
app.app_context().push()


@app.route("/")
def show_home_page():
    """Show all pets"""
    pets = db.session.execute(db.select(Pet)).scalars()
    return render_template("home.html", pets=pets)


@app.route("/add", methods=["GET", "POST"])
def show_add_pet_form():
    """Add Pet form; form-handler."""

    form = AddPetForm()

    if request.method == "POST":
        if form.validate_on_submit():
            # Adds new pet to db if valid.
            name = form.name.data
            species = form.species.data
            photo_url = form.photo_url.data
            age = form.age.data
            notes = form.notes.data
            new_pet = Pet(
                name=name, species=species, photo_url=photo_url, age=age, notes=notes
            )
            db.session.add(new_pet)
            db.session.commit()
            return redirect("/")
        else:
            # Renders with server side errors available for user to see.
            return render_template("pet_form.html", form=form)
    else:
        return render_template("pet_form.html", form=form)


@app.route("/<int:pet_id>", methods=["GET", "POST"])
def show_pet_page(pet_id):
    """Pet detail page."""

    # Uses same AddPetForm to update specific pet record.
    pet = db.get_or_404(Pet, pet_id)
    form = AddPetForm(obj=pet)

    if request.method == "POST":
        if form.validate_on_submit():
            pet = db.get_or_404(Pet, pet_id)
            pet.name = form.name.data
            pet.species = form.species.data
            pet.photo_url = form.photo_url.data
            pet.age = form.age.data
            pet.notes = form.notes.data
            db.session.add(pet)
            db.session.commit()
            return redirect(f"{pet.id}")
        else:
            return render_template("pet_page.html", pet=pet, form=form)
    else:
        return render_template("pet_page.html", pet=pet, form=form)
