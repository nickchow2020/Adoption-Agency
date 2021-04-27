from flask import Flask,render_template,redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db,connect_db,Pet
from form import Newpet,_Pet

app = Flask(__name__)

# the toolbar is only enabled in debug mode:
app.debug = True

# set a 'SECRET_KEY' to enable the Flask session cookies
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SECRET_KEY'] = "My_SECRET_KEY_1_@"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

toolbar = DebugToolbarExtension(app)

connect_db(app)

@app.route("/")
def home():
    all_pets = Pet.query.all()
    return render_template("home.html",pets=all_pets)


@app.route('/add',methods=["GET","POST"])
def add_new_pet():
    form = Newpet()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        url = form.url.data
        age = form.age.data
        note = form.note.data

        new_pet = Pet(name=name,species=species,photo_url=url,age=age,notes=note)
        db.session.add(new_pet)
        db.session.commit() 
        return redirect("/")
    else:
        return render_template("add_form.html",form=form)


@app.route("/pet/<int:pet_id>")
def show_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    return render_template("show_pet.html",pet=pet)


@app.route("/pet/<int:pet_id>/edit",methods=["GET","POST"])
def edit_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = _Pet(obj=pet)
    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data 
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()
        return redirect(f"/pet/{pet_id}")
    else:
        return render_template("edit_pet.html",form = form,pet=pet)


