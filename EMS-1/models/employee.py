from app import db

class EmployeeModel(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.INTEGER, primary_key=True)
    fullName = db.Column(db.String, nullable=True)
    #gender = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    phoneNumber = db.Column(db.String, nullable=False)
    nationalId = db.Column(db.String, nullable=False, unique=True)
    KRAPin = db.Column(db.String, nullable=False, unique=True)
    #basicSalary = db.Column(db.Float, nullable=False)
    #benefits = db.Column(db.Float, nullable=False)
    dept_id = db.Column(db.Integer, db.ForeignKey('departments.id'))

    def create(self):
        db.session.add(self)
        db.session.commit()


    @classmethod
    def check_employee_exist(cls,id):
        record = EmployeeModel.query.filter_by(nationalId =id).first()

        if record:
            return  True
        else:
            return False