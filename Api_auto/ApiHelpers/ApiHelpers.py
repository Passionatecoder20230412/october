import requests
from Api_auto.APIObjects.ApiObjects import ApiEndpoints


class ApiHelpers(ApiEndpoints):

    def get_api(self,endpoint,json):
        url=self.BASE_URL+self.PATH_URL
        url=url+endpoint
        resp=requests.get(url,json=json)
        return resp

    def post_api(self,endpoint,data):
        url = self.BASE_URL + self.PATH_URL
        url = url + endpoint
        resp = requests.post(url, data=data)
        return resp


