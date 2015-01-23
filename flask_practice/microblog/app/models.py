from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    
    #NOT an attribute, defined for the "one" side of one-to-many relationship
    #backref means we can use post.author to get the user who made the post
    posts = db.relationship('Post', backref='author', lazy='dynamic') 

    def __repr__(self):     #how to print out an instance of this obj
        return '<User %r>' % (self.nickname)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):     
        return '<Post %r>' % (self.body)
