from sqlalchemy import Table, Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from app.domain.profile import Profile


class SecretaryProfile(Profile):
    __tablename__ = 'SecretaryProfile'
    id = Column(Integer, ForeignKey('Profile.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'secretaryprofile',
    }

    def __repr__(self):
        return '<SecretaryProfile %r - %r>' % (self.email, self.name)