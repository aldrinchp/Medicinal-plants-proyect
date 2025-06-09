from flask_sqlalchemy import SQLAlchemy
from datetime import date as dt_date

db = SQLAlchemy()
#Tabla Images
class Image(db.Model):
    __tablename__ = 'images'     
    id = db.Column(db.Integer, primary_key=True)
    plant_id = db.Column(db.Integer, db.ForeignKey('plants.id'), nullable=False)

    date = db.Column(db.Date, nullable=False)  # no se usa default
    place = db.Column(db.String(100)) 
    link = db.Column(db.Text, nullable=False)

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __init__(self, plant_id, image_date, place, link):
        self.plant_id = plant_id
        self.date = image_date  # lo provee el usuario
        self.place = place
        self.link = link

    def __repr__(self):
        return f'Image {self.id}>'

#Tabla Plants
class Plant(db.Model):
    __tablename__ = 'plants'     
    id = db.Column(db.Integer, primary_key=True)

    # Clave foránea que referencia a la tabla 'Site_Origin'
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'), nullable=False)

    current_name = db.Column(db.String(100))
    scientific_name = db.Column(db.String(100))

    images = db.relationship('Image', backref='plants', lazy=True, cascade='all, delete-orphan')
    previous_researches = db.relationship('PreviousResearch', backref='plants', lazy=True, cascade='all, delete-orphan')
    uses = db.relationship('Use', backref='plants', lazy=True, cascade='all, delete-orphan')
    toponimos = db.relationship('Toponimo', backref='plants', lazy=True, cascade='all, delete-orphan')

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __init__(self, location_id,current_name,scientific_name):
        self.location_id = location_id
        self.current_name = current_name
        self.scientific_name = scientific_name

    def __repr__(self):
        return 'Plant %d>' % self.id


#Tabla Locations
class Location(db.Model):
    __tablename__ = 'locations'     
    id = db.Column(db.Integer, primary_key=True)
    city_name = db.Column(db.String(100), nullable = False)
    province_name = db.Column(db.String(100), nullable = False)

    plants = db.relationship('Plant', backref='locations', lazy=True, cascade='all, delete-orphan')
    interview_customers = db.relationship('InterviewCustomer', backref='locations', lazy=True, cascade='all, delete-orphan')
    interview_vendors = db.relationship('InterviewVendor', backref='locations', lazy=True, cascade='all, delete-orphan')

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __init__(self, city_name,province_name):
        self.city_name = city_name
        self.province_name = province_name

    def __repr__(self):
        return 'Location %d>' % self.id

#Tabla PreviousResearch
class PreviousResearch(db.Model):
    __tablename__ = 'previous_researches'
    id = db.Column(db.Integer, primary_key=True)
    id_plant = db.Column(db.Integer, db.ForeignKey('plants.id'), nullable=False)
    title = db.Column(db.String(255))
    link = db.Column(db.Text, nullable=False)

    def __init__(self, id_plant, title, link):
        self.id_plant = id_plant
        self.title = title
        self.link = link

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __repr__(self):
        return '<PreviousResearch %d: %s>' % (self.id, self.title)

#Tabla Uses
class Use(db.Model):
    __tablename__ = 'uses'
    id = db.Column(db.Integer, primary_key=True)
    id_plant = db.Column(db.Integer, db.ForeignKey('plants.id'), nullable=False)
    description = db.Column(db.Text, nullable=False)
    type_use = db.Column(db.String(200), nullable=False)

    def __init__(self, id_plant, description, type_use):
        self.id_plant = id_plant
        self.description = description
        self.type_use = type_use

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __repr__(self):
        return '<Use %d: %s>' % (self.id, self.description)

#Tabla Toponimo
class Toponimo(db.Model):
    __tablename__ = 'toponimos'
    
    id = db.Column(db.Integer, primary_key=True)
    id_plant = db.Column(db.Integer, db.ForeignKey('plants.id'), nullable=False)
    origin = db.Column(db.Text)
    comercial_distribution = db.Column(db.String(400))
    distribution = db.Column(db.String(400))


    def __init__(self, id_plant, origin, comercial_distribution, distribution):
        self.id_plant = id_plant
        self.origin = origin
        self.comercial_distribution = comercial_distribution
        self.distribution = distribution

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __repr__(self):
        return '<Toponimo %d: %s>' % (self.id, self.origin)

#Tabla InterviewCustomer
class InterviewCustomer(db.Model):
    __tablename__ = 'interview_customers'
    
    id = db.Column(db.Integer, primary_key=True)
    id_location = db.Column(db.Integer, db.ForeignKey('locations.id'), nullable=False)
    link = db.Column(db.String(500), nullable=False)
    
    # Campos q1 a q24 como varchar
    q1 = db.Column(db.String(255), nullable=False)
    q2 = db.Column(db.String(255), nullable=False)
    q3 = db.Column(db.String(255), nullable=False)
    q4 = db.Column(db.String(255), nullable=False)
    q5 = db.Column(db.String(255), nullable=False)
    q6 = db.Column(db.String(255), nullable=False)
    q7 = db.Column(db.String(255), nullable=False)
    q8 = db.Column(db.String(255), nullable=False)
    q9 = db.Column(db.String(255), nullable=False)
    q10 = db.Column(db.String(255), nullable=False)
    q11 = db.Column(db.String(255), nullable=False)
    q12 = db.Column(db.String(255), nullable=False)
    q13 = db.Column(db.String(255), nullable=False)
    q14 = db.Column(db.String(255), nullable=False)
    q15 = db.Column(db.String(255), nullable=False)
    q16 = db.Column(db.String(255), nullable=False)
    q17 = db.Column(db.String(255), nullable=False)
    q18 = db.Column(db.String(255), nullable=False)
    q19 = db.Column(db.String(255), nullable=False)
    q20 = db.Column(db.String(255), nullable=False)
    q21 = db.Column(db.String(255), nullable=False)
    q22 = db.Column(db.String(255), nullable=False)
    q23 = db.Column(db.String(255), nullable=False)
    q24 = db.Column(db.String(255), nullable=False)

    def __init__(self, id_location,link, **kwargs):
        self.id_location = id_location
        self.link = link
        for i in range(1, 25):  # Asignar los valores de q1 a q23 dinámicamente
            setattr(self, f'q{i}', kwargs.get(f'q{i}', None))

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __repr__(self):
        return '<InterviewCustomer %d: Location ID %d>' % (self.id, self.id_location)

#Tabla InterviewVendor
class InterviewVendor(db.Model):
    __tablename__ = 'interview_vendors'
    
    id = db.Column(db.Integer, primary_key=True)
    id_location = db.Column(db.Integer, db.ForeignKey('locations.id'), nullable=False)
    link = db.Column(db.String(500), nullable=False)
    
    # Campos q1 a q23 como varchar
    q1 = db.Column(db.String(255), nullable=False)
    q2 = db.Column(db.String(255), nullable=False)
    q3 = db.Column(db.String(255), nullable=False)
    q4 = db.Column(db.String(255), nullable=False)
    q5 = db.Column(db.String(255), nullable=False)
    q6 = db.Column(db.String(255), nullable=False)
    q7 = db.Column(db.String(255), nullable=False)
    q8 = db.Column(db.String(255), nullable=False)
    q9 = db.Column(db.String(255), nullable=False)
    q10 = db.Column(db.String(255), nullable=False)
    q11 = db.Column(db.String(255), nullable=False)
    q12 = db.Column(db.String(255), nullable=False)
    q13 = db.Column(db.String(255), nullable=False)
    q14 = db.Column(db.String(255), nullable=False)
    q15 = db.Column(db.String(255), nullable=False)
    q16 = db.Column(db.String(255), nullable=False)
    q17 = db.Column(db.String(255), nullable=False)
    q18 = db.Column(db.String(255), nullable=False)
    q19 = db.Column(db.String(255), nullable=False)
    q20 = db.Column(db.String(255), nullable=False)
    q21 = db.Column(db.String(255), nullable=False)
    q22 = db.Column(db.String(255), nullable=False)
    q23 = db.Column(db.String(255), nullable=False)
    

    def __init__(self, id_location,link, **kwargs):
        self.id_location = id_location
        self.link = link
        for i in range(1, 24):  # Asignar los valores de q1 a q23 dinámicamente
            setattr(self, f'q{i}', kwargs.get(f'q{i}', None))
        

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __repr__(self):
        return '<InterviewVendor %d: Location ID %d>' % (self.id, self.id_location)
        

# Initialize the review database
class Review(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    plant_id = db.Column(db.Integer, db.ForeignKey('plants.id'), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)  # 1 a 5
    date = db.Column(db.Date, nullable=False, default=dt_date.today)

    def __init__(self, plant_id, author, content, rating, review_date=None):
        self.plant_id = plant_id
        self.author = author
        self.content = content
        self.rating = rating
        self.date = review_date or dt_date.today()

    def __repr__(self):
        return f'<Review {self.id}: Plant {self.plant_id} - {self.author}>'
    
