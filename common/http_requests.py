import requests

class HttpRequests(object):

    def __init__(self):
        self.req = requests.session()
        self.fiddler_proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    def get(self, url, data, headers=None):
        response = self.req.get(url=url, headers=headers, json=data, proxies=self.fiddler_proxies)
        return response

    def post(self, url, data, headers=None):
        response = self.req.post(url=url, headers=headers, json=data, proxies=self.fiddler_proxies)
        return response


# if __name__ == '__main__':
    # print(get_token())
    # url = UrlConf.test_url.value
    # http = HttpRequests()
    # data = {"account":"13100000007","password":"123456","system":"pc","model":"pc","appId":"commission","role":"","uid":""}
    # print(http.post(url, data).json())