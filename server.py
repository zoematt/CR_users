from flask import Flask, request, render_template, redirect, session
from user import User

app= Flask(__name__)



@app.route('/show')
def index():
    users = User.getall_users()
    return render_template('readall.html', users=users)

@app.route('/')
def user_form():
    return render_template('create.html')

@app.route('/create_user', methods=['POST'])
def create_user():
    User.create(request.form)
    return redirect('/show')

# @app.route('/update_user')
# def update_user():
#     pass

if __name__=="__main__":     
    app.run(debug=True)