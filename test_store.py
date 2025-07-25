from jsonschema import validate
import pytest
import schemas
import api_helpers
import app # import added
from hamcrest import assert_that, contains_string, is_

'''
TODO: Finish this test by...
1) Creating a function to test the PATCH request /store/order/{order_id}
2) *Optional* Consider using @pytest.fixture to create unique test data for each run
2) *Optional* Consider creating an 'Order' model in schemas.py and validating it in the test
3) Validate the response codes and values
4) Validate the response message "Order and pet status updated successfully"
'''
def test_patch_order_by_id():
   app.reset_pets_data() #resets data 

#create order
order_data = {"pet_id": 0}
create_response = api_helpers.post_api_data
order_id = create_response.json()["id"]

#test PATCH
test_endpoint = f"/store/order/{order_id}"
patch_data = {"status": "sold"}

response = api_helpers.patch_api_data(test_endpoint, patch_data)

#validate response code
assert response.status_code == 200

#validate response message
response_json = response.json()
assert response_json["message"] == "Order and pet status updated successfully"

#check pet status
pet_response = api_helpers.get_api_data("/pets/0")
assert pet_response.json()["status"] == "sold"