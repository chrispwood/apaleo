# Explore the Monte Carlo API!
#
# API Documentation can be found here: https://apidocs.getmontecarlo.com/
#
# If you want to run these queries outside of the dashboard (e.g. via curl),
# you can follow these docs to generate and use an API token: 
# https://docs.getmontecarlo.com/docs/creating-an-api-token 
#
# These queries can also be run using our Python SDK (with first class 
# objects, pythonic snake_case, automatic retries, and more): 
# https://pypi.org/project/pycarlo/ 
#
# For reference here is an example query to get user information. 
# Press the play button to try it out:

#query getUser {
#   getUser {
#     email
#     firstName
#     lastName
#     createdOn
#     role
#     account {
#       uuid
#     }
#   }
# }
import requests
import json
import sys

print(sys.version)

class MakeApiCall:

  def get_data(self, api):
    response = requests.get(f"{api}")
    if response.status_code == 200:
      print("successfully fetched the data")
      self.formatted_print(response.json())
    else:
      print(
        f"Hello person, there's a {response.status_code} error with your request")
      print(f"The response is: {response.response}")

  def get_user_data(self, api, parameters):
    response = requests.get(f"{api}", params=parameters)
    if response.status_code == 200:
      print("sucessfully fetched the data with parameters provided")
      self.formatted_print(response.json())
    else:
      print(
        f"Hello person, there's a {response.status_code} error with your request")

  def formatted_print(self, obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

  def __init__(self, api):
    # self.get_data(api)

    parameters = {
      "username": "kedark"
    }
    self.get_user_data(api, parameters)



if __name__ == "__main__":
    api_call = MakeApiCall("https://dev.to/api/articles")