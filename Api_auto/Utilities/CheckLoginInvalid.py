from Api_auto.ApiHelpers.ApiHelpers import ApiHelpers


class CheckLoginInvalid(ApiHelpers):

    def check_login_with_invalid_cred(self,data):
        resp=self.post_api(self.VERIFY_LOGIN,data=data)
        return resp
