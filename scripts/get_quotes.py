import requests

api_url = 'https://stoic.tekloon.net/stoic-quote'

response = requests.get(api_url)


if response.status_code == requests.codes.ok:
    result_dict = response.json().get("data")

    if result_dict["author"] == "":
        result_dict["author"] = "unknown"

    # for some problems with shits ( eww.yuck ) , we have to replace the ' with "
    # for the widget to operate normally
    format_string = str(result_dict).replace("'" , '"')

    print(format_string)
else:
    print("Error:", response.status_code, response.text)
