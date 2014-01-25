from bottle import route, run
import redis

version = "1.0"
r = redis.StrictRedis(host='localhost', port=6379, db=0)

@route('/')
def start():
    return "Welcome to the SeChat-API version " + version

@route('/<key>', method='GET')
def get(key):
    r.set('test', 'bla')
    value = r.get(key)
    if(value==None):
        return { "success": False, "value": "Key not found"}
    return { "success": True, "value": value }

run(server='paste')