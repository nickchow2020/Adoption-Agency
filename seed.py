from models import Pet,db,connect_db
from app import app


connect_db(app)

db.drop_all()
db.create_all()

pet1 = Pet(
            name="Keeshond",
            species="dog",
            photo_url="http://cdn.akc.org/content/article-body-image/keeshond_dog_pictures.jpg",
            age=2,
            notes="I love this Dog")

pet2 = Pet(
    name="Sherry",
    species="dog",
    photo_url="http://cdn.akc.org/content/article-body-image/newfoundland_dog_pictures.jpg",
    age=3,
    notes="Good Enough"
)

pet3 = Pet(
    name = "Modena",
    species = "dog",
    photo_url = "http://cdn.akc.org/content/article-body-image/golden_puppy_dog_pictures.jpg",
    age = 2
)

pet4 = Pet(
    name = "Fiona",
    species = "dog",
    photo_url = "http://cdn.akc.org/content/article-body-image/great_pyr_puppy_dog_pictures_.jpg",
    age = 1,
    notes= "Hello,World"
)

pet5 = Pet(
    name = "Andy",
    species = "dog",
    photo_url = "http://cdn.akc.org/content/article-body-image/Finnishlapphundpuppies_dog_pictures.jpg",
    age = 1,
    notes = "I'm Chihuahua"
)

db.session.add(pet1)
db.session.add(pet2)
db.session.add(pet3)
db.session.add(pet4)
db.session.add(pet5)

db.session.commit()