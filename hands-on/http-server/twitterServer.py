from flask import Flask,request, abort,jsonify
import re

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello, Flask HTTP Server!</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

def userExistsCheckInternal(userName):
    for i in users.keys():
        if users[i]['username'] == userName.strip():
            return True        
    return False

def emailIdExistsCheckInternal(email_id):
    for i in users.keys():
        if users[i]['email_id'] == email_id.strip():
            return True        
    return False

@app.route('/userExistsCheck',methods=['GET'])
def userExistsCheck():
    input_user_name = request.args.get('userName')
    if userExistsCheckInternal(input_user_name):
        return 'user exists'
    else: 
        return 'user does not exist'

@app.route('/fetchUserInfo',methods=['GET'])
def fetchUserInfo():
    try:
        input_user_id = request.args.get(userId)
        return users[input_user_id]
    except Exception as e:
        abort(404, description='user not found!')

@app.route('/addUser',methods=['POST'])
def addUser():
    try:
        user_input_data = request.json
        if userExistsCheckInternal(user_input_data["username"]) or emailIdExistsCheckInternal(user_input_data["email_id"]):
            return jsonify({"success":"false"})
        else:
            users[max(users.keys())]=user_input_data
            return jsonify({"success":"true"})
    except Exception as e:
        abort(500, description='sobby, internal server error')

# logic in the below GET method needs to revisited some other time. 

@app.route('/listAllUsers',methods=['GET'])
def listAllUsers():
    try:
        offset=request.args.get(offset)
        limit=request.args.get(limit)
        output_array=str(users.keys())
        return jsonify({"success":"true","listOfUsers":output_array})
    except Exception as e:
        abort(400, description=e)



@app.route('/searchUserName',methods=['GET'])
def searchUserName():
    searchResultList=[]
    try:
        searchTerm=request.args.get('searchTerm')
        for i in users.keys():
            searchResult=re.search(".*"+searchTerm.strip()+".*",users[i]['username'])
            if searchResult:
                searchResultList.append(users[i]['username'])
        return jsonify({"success":"true","searchResult":str(searchResultList)})
        
    except Exception as e:
        abort(400, description=e)

users={1:{'username':'fat', 'email_id':'fat@g.com','phone':'','address':''},
       2:{'username':'haf', 'email_id':'haf@g.com','phone':'','address':''},
       3:{'username':'ali', 'email_id':'ali@g.com','phone':'','address':''},
       4:{'username':'abc', 'email_id':'abc@g.com','phone':'','address':''},
       5:{'username':'def', 'email_id':'def@g.com','phone':'','address':''},
       6:{'username':'ghu', 'email_id':'ghu@g.com','phone':'','address':''},
       7:{'username':'jkl', 'email_id':'jkl@g.com','phone':'','address':''},
       8:{'username':'mno', 'email_id':'mno@g.com','phone':'','address':''},
       9:{'username':'pqr', 'email_id':'pqr@g.com','phone':'','address':''},
       10:{'username':'stu', 'email_id':'stu@g.com','phone':'','address':''}
       }