from . import db
import views
from marshmallow import Schema, fields
class User(db.Model,):
  id= db.Column(db.Integer,primary_key=True)
  image = db.Column(db.String(80))
  firstname = db.Column(db.String(80))
  lastname = db.Column(db.String(80))
  age = db.Column(db.String(80))
  sex = db.Column(db.String(80))
  
  
  def __init__ (self,image,firstname,lastname,age,sex):
    self.image = image
    self.firstname=firstname
    self.lastname=lastname
    self.age = age
    self.sex = sex
    
  def __repr__ (self):
    return '<User%r>' % self.firstname

class UserSchema(Schema):
  formatted_name = fields.Method("format_name")


  class Meta:
    fields = ('firstname', 'lastname', 'image', 'age', 'sex')
 