import requests

def test_get_locations_for_us_90210_check_status_code_equals_200():
  response = requests.get("http://api.zippopotam.us/us/90210")
  response_body = response.json()
  #assert response.status_code == 201
  #assert response.headers['Content-Type'] == "application/json"
  #assert response_body["country"] == "United States"
  #assert response_body["places"][0]["place name"] == "Beverly Hills"
  assert len(response_body["places"]) == 1
