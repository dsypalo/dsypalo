from application import db

class Data(db.Model):
    fio = db.Column(db.String(255), unique=True, nullable=False)
    avg_grade_point = db.Column(db.Integer, unique=False, nullable=True)
    m_phone = db.Column(db.Integer, unique=False, nullable=True)
    email = db.Column(db.String(255), unique=False, nullable=True)
    education = db.Column(db.String(255), unique=False, nullable=True)
    passport = db.Column(db.Integer, unique=False, nullable=False)
    public_activity = db.Column(db.String(255), unique=False, nullable=False)

    def __init__(self, inn):
        self.inn = inn
    def __repr__(self):
        return '<Data %r>' % self.inn



class S3(db.Model):
    id_doc = db.Column(db.Integer, unique=True, primary_key=True, nullable=False)
    doc = db.Column(db.String(255),nullable=False)

    def __repr__(self):
        return '<S3 %r>' % self.doc
