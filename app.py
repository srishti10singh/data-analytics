# write fapp
from flask import Flask, render_template, redirect ,request
from database import User , add_to_db,get_db
app = Flask(__name__)
app.secret_key = "themostsecretkeyever"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/example1/form',methods =['GET', 'POST'])
def example_from():
    status= None
    if request.method== 'POST': 
        name= request.form.get('uname')
        email= request.form.get('email')
        password=request.form.get('pwd')
        if len(email)> 0 and len(name)>0 and len(password)>0:
            user=User(name=name, email=email,password=password)
            add_to_db(user)
            status = "user added successfully"
        else: 
            status="fill all "    
    return render_template('form.html',status=status)

@app.route('/example1/list')
def example_1_list():
    db=get_db()
    users = db.query(User).all()
    return render_template('list.html', userlist=users)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 