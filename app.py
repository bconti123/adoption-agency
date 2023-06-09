from flask import Flask, render_template, redirect
from models import db, connect_db, Pet
from flask_debugtoolbar import DebugToolbarExtension
from form import AddPetForm, EditPetForm

app = Flask(__name__)
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'IDK'

# DEBUG TOOLBAR

app.config['DEBUG'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
toolbar = DebugToolbarExtension(app)


connect_db(app)
db.drop_all()
db.create_all()

@app.route('/')
def home():
    pets = Pet.query.all()
    
    return render_template("/index.html", pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    form = AddPetForm()
    if form.validate_on_submit():
        # name = form.name.data
        # species = form.species.data
        # photo_url = form.photo_url.data
        # age = form.age.data
        # notes = form.notes.data
        # available = form.available.data
        # new_pet = Pet(name=name, species=species, photo_url=photo_url or None, age=age, notes=notes, available=available)
        # Another better option is below
        data = {k : v for k, v in form.data.items() if k != "csrf_token"}
        new_pet = Pet(**data)

        db.session.add(new_pet)
        db.session.commit()
        
        return redirect('/')
    else:
        return render_template("/add/add.html", form=form)
    
@app.route('/<pet_id>', methods=['GET', 'POST'])
def edit_pet(pet_id):
    pet = Pet.query.get(pet_id)
    form = EditPetForm(obj=pet)
    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        return redirect('/')

    return render_template('/edit.html', form=form, pet=pet)


