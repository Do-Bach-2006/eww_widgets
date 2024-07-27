import requests
import json


# get the current weather in Ho Chi Minh city .
# you can go to https://www.weatherapi.com/api-explorer.aspx
# create an account , get the API key
# then go to https://www.weatherapi.com/api-explorer.aspx
# explore the tools to get your region weather api

# FIXME: remove this line if you push the code to github!
api_key = "7b49286c06604a47b31102313242307"

request = requests.get(url=f"http://api.weatherapi.com/v1/current.json?key={api_key}&q=Ho_Chi_Minh &aqi=yes" )

if request.status_code == 200:
    result_dict = request.json()

    # we only need the name , temperature , condition icons , text and wind power
    format_dict = {}

    format_dict["name"] = result_dict["location"]["name"]
    format_dict["temperature"] = result_dict["current"]["temp_c"]
    format_dict["current_condition_text"] = result_dict["current"]["condition"]["text"]
    format_dict["wind_speed"] = result_dict["current"]["wind_kph"]

    # for some problems with shits ( eww.yuck ) , we have to replace the ' with "
    # for the widget to operate normally
    format_string = str(format_dict).replace("'" , '"')

    print(format_string)

else:
    print("error fetching weather")