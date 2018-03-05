#coding:utf-8
from flask import Flask,g,request,session,redirect,url_for,jsonify
from extensions import db
from models import Article,User,Readability
import config

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

with app.app_context():
    db.create_all()

# @app.route('/')
# def hello_world():
#     print 'hello_world'
#     session["username"] = "sss"
#     return jsonify(success='1', message="Succeesful link")

@app.route('/FirstCookieRequest')
def FirstCookieRequest():
    if session.get('username'):
        userResult = User.query.filter(User.username == session.get('username')).first()
        if userResult:
            return jsonify(success="1", message="Cookie login successful!", user_id=userResult.id)
        else:
            return jsonify(success="0", message="over time")
    return jsonify(success="0", message="over time")



@app.route('/login',methods=["POST"])
def login():
    json = request.get_json()
    username = json.get('username')
    password = json.get('password')
    session["username"] = username

    userResult = User.query.filter(User.username == username).first()
    if userResult != None:
        if userResult.password == password:
            session['username'] = username
            print("Login action --------> user id : %d" % userResult.id)
            return jsonify(success="1", message="login successful!",user_id=userResult.id)
        return jsonify(success="0", message="password is wrong!")
    return jsonify(success="0", message="no account!")



@app.route('/register',methods=["POST"])
def register():
    json = request.get_json()
    username = json.get('username')
    password = json.get('password')
    print username,password
    userResult = User.query.filter(User.username == username).first()
    if userResult != None:
        return jsonify(success="0", message="Username has already be registered!")
    else:
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        userResultNew = User.query.filter(User.username == username).first()
        session["username"] = username
        print("Register action --------> user id : %d" % userResultNew.id)
        return jsonify(success="1", message="register successful!", user_id=userResultNew.id)


@app.route('/postReadability',methods=["POST"])
def postReadability():

    json = request.get_json()
    user_id = json.get('user_id')
    url_add = json.get('url_add')
    readability_rate = json.get('readability_rate')
    print("PostReadability action --------> user id : %d " % user_id)
    readability_objectOld = Readability.query.filter(Readability.user_id == user_id, Readability.url_add == url_add).first()
    #if there is a data -update
    if readability_objectOld != None:
        readability_objectOld.readability_rate = readability_rate
        db.session.commit()
        return jsonify(success="1", message="update successful!", user_id=user_id)
    # if there is no data -add
    else:
        readability_object = Readability(user_id=user_id, url_add=url_add,readability_rate=readability_rate)
        db.session.add(readability_object)
        db.session.commit()
        return jsonify(success="1", message="post successful!", user_id=user_id)

@app.route('/<path:url>',methods = ['GET'])
def getData(url):
    print url
    return jsonify({'ARI_Score': 7, 'FRE_Score': 5, 'FKG_Score': 9, 'GFI_Score': 3,
                    'SmogIdx': 8, 'ColemanIdx': 3, 'LIX': 5, 'RIX': 9})

#for each request,do it before execute the action
@app.before_request
def before_request():
    # if session.get('username') :
    #     g.username = session.get('username')
    #only first function with cookie for login , other function without cookie, just check it  in android coding
    print('Before request (cookie action) --------> username : %s  '    % session.get('username'))


if __name__ == '__main__':
    app.run()


