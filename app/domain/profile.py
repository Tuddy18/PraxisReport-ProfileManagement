from app import db
from sqlalchemy import Table, Column, Integer, ForeignKey, String
from app.domain.json_serializable import JsonSerializable


class Profile(db.Model, JsonSerializable):
    __tablename__ = 'Profile'
    id = Column(Integer, primary_key=True)
    email = Column(String(120))
    name = Column(String(120))
    phone = Column(String(120), nullable=True)

    type = Column(String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'profile',
        'polymorphic_on': type
    }

    def __repr__(self):
        return '<Profile [%r] %r - %r %r>' % (self.type, self.email, self.name)