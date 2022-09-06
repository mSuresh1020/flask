from flask import Blueprint,jsonify,request
from first_flask_db import db
from first_flask_db.details.models import User

mod=Blueprint("details",__name__,url_prefix="/user_info")

@mod.route("/",methods=['GET'])
def fetchall():
    users=User.query.all()
    response=[x.__repr__() for x in users]
    return jsonify(response)

@mod.route("/console1",methods=["GET"])
def fetch_console1():
    users=User.query.all()
    response=[x.__repr__() for x in users]
    print(users[0].id,users[1].username)
    return jsonify(response)

@mod.route("/console2",methods=["GET"])
def fetch_console2():
    users=User.query.all()
    response=[x.__repr__() for x in users]
    print(users[0],users[1])
    return jsonify(response)


##############################################################################################################
@mod.route("/<user_id>",methods=["GET"])
def fetch_id(user_id):
    users=User.query.get(user_id)
    response=users.__repr__()                     ## response=[x.__repr__() for x in users] this is not possible.
    return jsonify(response)

@mod.route("pop/<user_id>",methods=["GET"])
def fetch_id_pop(user_id):
    users=User.query.get(user_id)
    response=users.__repr__()
    response.pop("password")
    return jsonify(response)


@mod.route("console1/<user_id>")
def fetch_id_console1(user_id):
    users=User.query.get(user_id)
    response=users.__repr__()
    # print(users)
    print(users.username,users.password)
    return jsonify(response)

###############################################################################################################

@mod.route("/get_user1")
def double_user():
    username=request.args.get("username")
    users=User.query.filter(User.username==username).first()
    response=users.__repr__()
    return jsonify(response)

@mod.route("/get_user2")
def double_user_both():
    username=request.args.get("username")
    users=User.query.filter(User.username==username)
    response=[x.__repr__() for x in users]
    return jsonify(response)

##################################################################################################################



