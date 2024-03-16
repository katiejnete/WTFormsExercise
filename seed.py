from app import db
from models import Pet

db.drop_all()
db.create_all()
p = Pet(name="Ne-yo", species="dog", available=False)
db.session.add(p)
db.session.commit()
