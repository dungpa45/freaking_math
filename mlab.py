import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds251747.mlab.com:51747/movies

host = "localhost"
port = 27017
db_name = "math"
user_name = "admin"
password = "123456"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())