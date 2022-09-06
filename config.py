class Config(object):
    SECRET_KEY="suresh10"                  ## This key is used for "session" purpose.
### SQLALCHEMY_DATABASE_URI=use DatabaseName://UserName:Password@ip/DatabaseName"
    SQLALCHEMY_DATABASE_URI="mysql://root:SQL102030@localhost/user_info"
    SQLALCHEMY_TRACK_MODIFICATION=False                                     ## Log file track if True

class Developmentconfig(Config):
    Debug=True                                                             ## Error Track
    SQLALCHEMY_ECHO=True                                                    ## SQLAlchemy Related Error Track

class Testingconfic(Config):
    SQLALCHEMY_DATABASE_URI="mysql://root:SQL102030@localhost/test_db"      ## here TableName id different
    SQLALCHEMY_TRACK_MODIFICATION=False
    Debug=True
    SQLALCHEMY_ECHO=True

class Productionconfig(Config):
    Debug=False

app_config={"Development":Developmentconfig,
           "Testing":Testingconfic,
           "Production":Productionconfig}


