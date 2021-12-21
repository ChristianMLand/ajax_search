from flask import Flask,render_template,redirect,request,session,jsonify
import user

app = Flask(__name__)
app.secret_key = 'itsasecret'
DB = 'usernames_schema'

@app.route('/')
def index():
    return render_template('index.html',all_users=user.User.get_all())

@app.post('/users/create')
def create_user():
    user.User.create(request.form)
    return redirect('/')

@app.post('/users/filter')
def filter_users():
    search_data = {
        'partial_username' : request.form['partial'] + '%'
    }
    matches = user.User.filter(search_data)
    return jsonify(matches)

if __name__=="__main__":
    app.run(debug=True)