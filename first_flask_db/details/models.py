from first_flask_db import db

class User(db.Model):                                                  ## "User" is a mysql Table name.
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(100),index=True,unique=True)
    email=db.Column(db.String(100),unique=True)
    password=db.Column(db.String(100))

    def __repr__(self):
        return {"username":self.username,
                "email":self.email,
                "password":self.password}
