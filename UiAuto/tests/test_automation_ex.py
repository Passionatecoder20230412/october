import pytest
from datetime import datetime
from UiAuto.pages.RegisterAutomationEx import RegisterAutomationEx

# Define your data dictionaries inside the test file
REGISTRATION_DATA = {
    "reg1": {
        "name": "vijay",
        "email": f"vijay.test_{datetime.now().strftime("%Y%m%d_%H%M%S")}@gmail.com",
        "password": "vijay@9876",
        "day_index": 15,
        "month_label": "September",
        "year_val": "1995",
        "first_name": "Vijay",
        "last_name": "Kumar",
        "company": "Tech Corp",
        "address_v": "123 Main Street",
        "address_m": "Suite 400",
        "country_label": "India",
        "state": "Karnataka",
        "city": "Bengaluru",
        "zipcode": "560037",
        "mobile": "9876543210"
    },
    "reg2": {
        "name": "amit",
        "email": f"amit.test8501_{datetime.now().strftime("%Y%m%d_%H%M%S")}@gmail.com",
        "password": "amit@1234",
        "day_index": 20,
        "month_label": "October",
        "year_val": "1993",
        "first_name": "Amit",
        "last_name": "Sharma",
        "company": "Dev Corp",
        "address_v": "456 Oak Road",
        "address_m": "Floor 2",
        "country_label": "India",
        "state": "Maharashtra",
        "city": "Mumbai",
        "zipcode": "400001",
        "mobile": "9876543211"
    }
}


class TestAutomationEx:

    # We pass dict keys to ids so your test report shows "test_automation_ex[reg1]" and "test_automation_ex[reg2]"
    @pytest.mark.parametrize(
        "data_dict",
        REGISTRATION_DATA.values(),
        ids=REGISTRATION_DATA.keys()
    )
    def test_automation_ex(self, init_page, data_dict):
        register = RegisterAutomationEx(init_page)

        # Pass the dictionary values using kwargs matching your method parameters
        register.register_automation_ex(
            name=data_dict["name"],
            email=data_dict["email"],
            password=data_dict["password"],
            day_index=data_dict["day_index"],
            month_label=data_dict["month_label"],
            year_val=data_dict["year_val"],
            first_name=data_dict["first_name"],
            last_name=data_dict["last_name"],
            company=data_dict["company"],
            address_v=data_dict["address_v"],
            address_m=data_dict["address_m"],
            country_label=data_dict["country_label"],
            state=data_dict["state"],
            city=data_dict["city"],
            zipcode=data_dict["zipcode"],
            mobile=data_dict["mobile"]
        )
        print(data_dict['email'],data_dict['password'])
