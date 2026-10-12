import pytest
from Api_auto.TestData.TestData import user1
from Api_auto.Utilities.CheckLoginInvalid import CheckLoginInvalid
@pytest.mark.parametrize("data",[user1])
class TestInvalid(CheckLoginInvalid):

    def test_invalid(self,data):
        resp=self.check_login_with_invalid_cred(data)
        print(resp,"vijay")
        print("---------------------")
        print(resp.json( ))
        print("---------------------")
        print(resp.text)

