import httplib

try:
    import json
except ImportError:
    import simplejson as json

def return_response(name):
    def inner_return_response(f):
        def do_job(self, *args, **kwargs):
            status, data = f(self, *args, **kwargs)

            if status == httplib.OK:
                return data.get(name)
            else:
                return None
        return do_job
    return inner_return_response

class Thunder(object):
    API_VERSION = "1.0.0"
    API_URL = "/api/%s/%s/%s/"

    def __init__(self, apikey, apisecret, host, port=80):
        self.apikey = apikey
        self.apisecret = apisecret
        self.host = "%s:%d" % (host, port,)

    def _make_url(self, command, *args):
        url = self.API_URL % (self.API_VERSION, self.apikey, command,)

        if args:
            url += "/".join([str(arg) for arg in args]) + "/"

        return url

    def _make_request(self, method, url, data=None):
        headers = {
            "X-Thunder-Secret-Key": self.apisecret,
            "Content-Type": "application/json"
        }

        if data:
            data = json.dumps(data)

        connection = httplib.HTTPConnection(self.host)
        connection.request(method, url, body=data, headers=headers)
        response = connection.getresponse()

        if response.status == httplib.OK:
            data = response.read()

            if data:
                data = json.loads(data, "utf-8")
        else:
            data = {}

        connection.close()

        return (response.status, data)

    @return_response("count")
    def get_user_count(self):
        return self._make_request("GET", self._make_url("users"))

    @return_response("users")
    def get_users_in_channel(self, channel):
        return self._make_request("GET", self._make_url('channels', channel))

    @return_response("count")
    def send_message_to_user(self, userid, message):
        return self._make_request("POST", 
            self._make_url("users", userid), message)

    @return_response("count")
    def send_message_to_channel(self, channel, message):
        return self._make_request("POST", 
            self._make_url("channels", channel), message)

    @return_response("online")
    def is_user_online(self, userid):
        return self._make_request("GET", self._make_url("users", userid))

if __name__ == '__main__':
    c = Thunder("key", "secretkey", "localhost", 8080)
    
    print c.get_user_count()
    print c.get_users_in_channel("test")
    print c.send_message_to_user("test", {"msg": "hello!"})
    print c.send_message_to_channel("test", {"msg": "hello!"})
    print c.is_user_online("test")
