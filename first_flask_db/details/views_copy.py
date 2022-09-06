from flask import Blueprint, jsonify, request
from first_flask_db import db
from first_flask_db.details.models import User

mod = Blueprint("details", __name__, url_prefix='/user_info')

####################################################################################################################
# SQLAlchemy API:-
#    GET Api: 3-API=fetchall, fetch_console1_individual(user_id ,password, username),fetch_console2_users
#             3-API=fetch user_id, fetch user_id(pop password),fetch_console1,2(users,individual id,password).
#             2-API= Double username-fetch (.first) & fetch both
#   POST API: 1-API=Normal post
#             1-API=Form
#   PUT API:  1-API
#   DELETE API: 1-API

####################################################################################################################
############################################## [GET] ######################################################
## API-1.1_Normal
@mod.route("/", methods=["GET"])
def fetchall():
    users = User.query.all()                        ## Select * from user
    response = [x.__repr__() for x in users]
    return jsonify(response)                        ## ANS: http://127.0.0.1:5000/user_info

## API-1.2:fetch to console without __repr__ comment.
@mod.route("/console1",methods=["GET"])
def fetch_console1():
    users=User.query.all()
    print(users[0].username,users[1].username)         ## for fetch username on console
    print(users[0].id, users[1].password)              ## for fetch id,password on console
    response=[x.__repr__() for x in users]
    return jsonify(response)                           ## ANS: http://127.0.0.1:5000/user_info/console1

## API-1.3:fetch to console with __repr__ comment.
@mod.route("/console2",methods=["GET"])
def fetch_console2():
    users=User.query.all()
    print(users[0],users[1])                        ## fetch only <user1> & <user2> but comment __repr__ inside models
    response=[x.__repr__() for x in users]
    return jsonify(response)                        ## ANS: http://127.0.0.1:5000/user_info/console2


######################################## [retrive by id/get by id/fetch by id] ###################################
## API-2.1: get(retrive) user id
@mod.route("/<user_id>",methods=["GET"])
def fetch_id(user_id):
    users=User.query.get(int(user_id))         ## int or eval
    response=users.__repr__()                  ## response=[x.__repr__() for x in users] this is not possible.
    return jsonify(response)                   ## ANS: http://127.0.0.1:5000/user_info/1

## API-2.2: get(retrive) user id--by using pop to hide the password
@mod.route("pop/<user_id>")
def fetch_id_pop(user_id):
    users=User.query.get(int(user_id))
    response=users.__repr__()
    response.pop("password")                    ## by using pop to hide the password
    return jsonify(response)                    ## ANS: http://127.0.0.1:5000/user_info/pop/1

## API-2.3: get by user id--fetch user by repr on models with/without comment.
@mod.route("console1/<user_id>")
def fetch_id_console1(user_id):
    users=User.query.get(int(user_id))
    #print(users)                               ## repr with comment possible,without comment not possible.
    print(users.username, users.password)       ## repr with or without comment possible.
    response=users.__repr__()
    return jsonify(response)                    ## ANS: http://127.0.0.1:5000/user_info/console1/1


#######################################  [Same double usernames]  ###############################################
## API-3.1 :WHEN double usernames to show one username.    here [.first()] is must
@mod.route("/get_user1")
def double_user():                                              ## if single username show single.
    username=request.args.get("username")                       ## double same username then first one username show.
    users=User.query.filter(User.username==username).first()    ## if .first() remove then answer object come.
    response=users.__repr__()
    return jsonify(response)           ## ANS: http://127.0.0.1:5000/user_info/get_user1?username=Suresh

## API-3.2 :WHEN double same usernames to show both.    here [.first()] is no need.
@mod.route("/get_user2")
def double_user_both():
    username=request.args.get("username")
    users=User.query.filter(User.username==username)           ## if double/single username then both showing.
    # users=User.query.filter(User.username==username).first() ## if using .first() then object ans showing.(Not possible)
    response=[x.__repr__() for x in users]
    return jsonify(response)        ## ANS: http://127.0.0.1:5000/user_info/get_user2?username=Bashu

#######################################################################################################################
##############################################  [POST]  ######################################################
## API-1: Json_request:
# @mod.route("/json_request",methods=["POST"])
# def abc1():
#     user_data=request.get_json()
#     users=User(username=user_data["username"],
#                email=user_data["email"],
#                password=user_data["password"])
#     db.session.add(users)                     ## to add data to db.
#     db.session.commit()                       ## to save data to db_table & show.
#     return "json data added successfully"     ## ANS: http://127.0.0.1:5000/user_info/json_request

## postman->POST->Body->raw->Json [id:auto_gen,username,email,password put]


## API-2: form_data:
# @mod.route("/form_data",methods=["POST"])
# def abc1():
#     username=request.form.get("username")
#     email=request.form.get("email")
#     password=request.form.get("password")
#     users=User(username=username,
#                email=email,
#                password=password)
#     db.session.add(users)
#     db.session.commit()
#     return "Form data added successfully"         ## ANS: http://127.0.0.1:5000/user_info/form_data

## Postman->Body-->form data->[type username,email,password]only.


################################################ [PUT]   ##################################################
## API-3: update/rename data:
# @mod.route("/rename/<user_id>",methods=["PUT"])
# def update(user_id):
#     user_data=request.get_json()                       ## we put data on postman.
#     users=User.query.get(int(user_id))                 ## to get data from mysql
#     users.email=user_data["email"]                     ## compare data
#
#     db.session.commit()                                ## saved or updated data on mysql.
#     return "data update successfully"       ## ANS: http://127.0.0.1:5000/user_info/rename/5

## Postman->Body-->form data->[type email=uddated email]only.


################################################ [DELETE]   ##################################################
## API-4: Delete data:
# @mod.route("/delete/<user_id>",methods=["DELETE"])
# def delete(user_id):
#     users=User.query.get(int(user_id))       ## to get data from mysql
#
#     db.session.delete(users)
#     db.session.commit()
#     return "data delete successfully"        ## ANS: http://127.0.0.1:5000/user_info/delete/3

## Postman->any parameter.


