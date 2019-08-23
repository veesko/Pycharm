from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

#custom imports
from config.configs import Config,DevelopmentConfig,ProductionConfig

#init flask
app = Flask(__name__)

#import cofigs
app.config.from_object(DevelopmentConfig)

# init sqlachemy
db = SQLAlchemy(app)

#models
from models.departments import DepartmentModel
from models.employee import EmployeeModel

@app.before_first_request
def create_tables():
    db.create_all()
#routes
@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/departments', methods = ['GET','POST'])
def departments():
    allDepts = DepartmentModel.fetch_all_departments()
    #print(type(allDepts))
    for x in allDepts:
        print(x.name)
    if request.method == 'POST':
        nameInput = request.form['department']
        if DepartmentModel.check_dept_exist((nameInput)):
            print('dept already exist')
        else:
            record = DepartmentModel(name=nameInput)
            record.create()
            print('added')
            return redirect(url_for('departments'))
        #print(name)



    return render_template('departments.html',depts = allDepts)


@app.route('/employees', methods=['GET','POST'])
def employees():
    allDepts = DepartmentModel.fetch_all_departments()
    if request.method == 'POST':
        name = request.form['empName']
        email = request.form['email']
        phone = request.form['phonenum']
        natId = request.form['nationalId']
        krapin = request.form['kra']
        deptname = request.form['department']
        if EmployeeModel.check_employee_exist(natId):
            print('Employee already exist')
        else:
            emp = EmployeeModel(fullName = name,email = email,phoneNumber = phone,nationalId = natId,KRAPin = krapin,dept_id = deptname)
            emp.create()
            print('added')
            return redirect(url_for('employees'))

    return render_template('employees.html',depts = allDepts)


if __name__ == '__main__':
    app.run(debug = True)
