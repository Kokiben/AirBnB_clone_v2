#!/usr/bin/python3
"""Print a class state that inherits from BaseModel."""
from models.base_model import BaseModel


class State(BaseModel):
    """ class attribute."""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")


    @property
    def cities(self):
        vr = models.storage.all()
        lst = []
        rslt = []
        for ky in vr:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                lst.append(var[key])
        for elm in lst:
            if (elm.state_id == self.id):
                rslt.append(elm)
        return (rslt)


