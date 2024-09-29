from requests import get
from json import dump , load
from datetime import date
from os import chdir


def main():
    PATH_TO_LEETCODE_DATA = "./data/leetcode_today_problem.json"

    data = None

    """
        I add a file to store leetcode today problem .
        with this approach , we make sure that only need to call the api once each day
    """

    try:
        with open(PATH_TO_LEETCODE_DATA, "r") as file_obj:
            data = load(file_obj)

        current = date.today()

        format_date = current.strftime("%Y-%m-%d")

        # if the json file does not hold anything or the data is outdated
        if "date" not in data or data["date"] != format_date:


            # update the json
            with open(PATH_TO_LEETCODE_DATA, "w") as file_obj:
                data = get_leetcode_today_json()
                dump(data, file_obj)


    except FileNotFoundError:


        with open(PATH_TO_LEETCODE_DATA, "w") as file_obj:

            data = get_leetcode_today_json()
            dump(data, file_obj)

    # yes , I know , this shit happens quite some times
    format_data = str(data).replace("'" , '"')

    print( format_data )

def get_leetcode_today_json() -> str:
    request = get('https://alfa-leetcode-api.onrender.com/daily')
    if request.status_code == 200:

        format_dict = {}
        result_dict = request.json()

        format_dict['link'] = result_dict["questionLink"]
        format_dict['name'] = result_dict["questionTitle"]
        format_dict['difficulty'] = result_dict["difficulty"]
        format_dict['color'] = "green" if format_dict['difficulty'] == "#a3be8c" else "#ebcb8b" if format_dict['difficulty'] == "Medium" else "#bf616a"
        format_dict['tags'] = []
        format_dict['date'] = result_dict["date"]

        for tag in result_dict["topicTags"]:
            format_dict['tags'].append( tag["name"] )

        format_dict['tags'] = " , ".join( format_dict["tags"] )

        return format_dict

    else:
        # return an empty dict to write to json file and prevent error
        return {}

if __name__ == "__main__":
    main()