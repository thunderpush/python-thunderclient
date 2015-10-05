import requests

try:
    import simplejson as json
except ImportError:
    import json  # NOQA


def return_response(name=None):
    def inner_return_response(f):
        def do_job(self, *args, **kwargs):
            status, data = f(self, *args, **kwargs)

            if status == requests.codes.ok:
                return data.get(name)
            elif name is None and status == requests.codes.no_content:
                return True
            else:
                return None
        return do_job
    return inner_return_response


class Thunder(object):
    API_VERSION = '1.0.0'
    API_URL = '/api/%s/%s/%s/'

    def __init__(self, apikey, apisecret, host, port=80, use_ssl=False):
        self.apikey = apikey
        self.apisecret = apisecret
        self.host = '{protocol}://{host}:{port}'.format(
            host=host,
            port=port,
            protocol='https' if use_ssl else 'http'
        )

    def _make_url(self, command, *args):
        url = self.host
        url += self.API_URL % (self.API_VERSION, self.apikey, command,)

        if args:
            url += "/".join([str(arg) for arg in args]) + "/"

        return url

    def _make_request(self, method, url, data=None):
        headers = {
            'X-Thunder-Secret-Key': self.apisecret,
            'Content-Type': 'application/json'
        }

        data = json.dumps(data) if data else None
        method = getattr(requests, method.lower())
        response = method(url, data=data, headers=headers)

        if response.status_code == requests.codes.ok:
            data = response.text

            if data:
                data = json.loads(data, 'utf-8')
        else:
            data = {}

        return (response.status_code, data)

    @return_response('count')
    def get_user_count(self):
        return self._make_request('GET', self._make_url('users'))

    @return_response('users')
    def get_users_in_channel(self, channel):
        return self._make_request('GET', self._make_url('channels', channel))

    @return_response('count')
    def send_message_to_user(self, userid, message):
        return self._make_request(
            'POST', self._make_url('users', userid), message
        )

    @return_response('count')
    def send_message_to_channel(self, channel, message):
        return self._make_request(
            'POST', self._make_url('channels', channel), message
        )

    @return_response('online')
    def is_user_online(self, userid):
        return self._make_request('GET', self._make_url('users', userid))

    @return_response()
    def disconnect_user(self, userid):
        return self._make_request('DELETE', self._make_url('users', userid))

if __name__ == '__main__':
    c = Thunder('key', 'secretkey', 'localhost', 8080)

    print(c.get_user_count())
    print(c.get_users_in_channel('test'))
    print(c.send_message_to_user('test', {'msg': 'hello!'}))
    print(c.send_message_to_channel('test', {'msg': 'hello!'}))
    print(c.is_user_online('test'))
    print(c.disconnect_user('test'))
