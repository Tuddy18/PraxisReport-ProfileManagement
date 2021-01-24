from sqlalchemy import Table, Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from app.domain.profile import Profile


class StudentProfile(Profile):
    __tablename__ = 'StudentProfile'
    id = Column(Integer, ForeignKey('Profile.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'studentprofile',
    }

    cetatenie = Column(String(120), nullable=True)
    oras = Column(String(120), nullable=True)
    strada = Column(String(120), nullable=True)
    nr_cladire = Column(String(120), nullable=True)
    apartament = Column(String(120), nullable=True)
    judet = Column(String(120), nullable=True)
    cnp = Column(String(120), nullable=True)
    serie_ci = Column(String(120), nullable=True)
    nr_ci = Column(String(120), nullable=True)
    data_nasterii = Column(String(120), nullable=True)
    locul_nasterii = Column(String(120), nullable=True)
    an_studiu = Column(String(120), nullable=True)
    grupa = Column(String(120), nullable=True)
    specializare = Column(String(120), nullable=True)
    linie_studiu = Column(String(120), nullable=True)

    def __init__(self, email, name):
        self.email = email
        self.name = name

    def __repr__(self):
        return '<StudentProfile %r - %r>' % (self.email, self.name)