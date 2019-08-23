from app import db

class DepartmentModel(db.Model):
    __tablename__ = 'departments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True, unique=True)
    employee = db.relationship('EmployeeModel', backref='department', lazy=True)

    def create(self):
        db.session.add(self)
        db.session.commit()


    # a class method is bound to a class
    @classmethod
    def check_dept_exist(cls,dpt_name):
        record = DepartmentModel.query.filter_by(name =dpt_name).first()

        if record:
            return  True
        else:
            return False
    @classmethod
    def fetch_all_departments(cls):
        return cls.query.all()