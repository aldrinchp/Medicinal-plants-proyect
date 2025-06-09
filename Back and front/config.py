#Configurar el docker
class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456789@localhost:3306/Medicinal_plants_proyect'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
