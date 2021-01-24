from sqlalchemy import Table, Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from app.domain.profile import Profile


class ProfessorProfile(Profile):
    __tablename__ = 'ProfessorProfile'
    id = Column(Integer, ForeignKey('Profile.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'professorprofile',
    }

    functie = Column(String(120), nullable=True)
    fax = Column(String(120), nullable=True)

    def __repr__(self):
        return '<ProfessorProfile %r - %r>' % (self.email, self.name)