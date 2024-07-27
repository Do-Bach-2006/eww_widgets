from requests import get
from json import dump , load
from datetime import date
from os import chdir


def main():
    PATH_TO_EPIC_DATA = "./data/epic_free_games.json"

    data = None


    try:
        with open(PATH_TO_EPIC_DATA, "r") as file_obj:
            data = load(file_obj)

            current = date.today()

            current_date = current.strftime("%Y-%m-%d")

        # the date is called expired when the min date is the expiredate ( current date is bigger than or equal the expiredate)
        if "expire_date" not in data or get_min_date( [data["expire_date"] , current_date ] ) == data["expire_date"]:
            with open(PATH_TO_EPIC_DATA, "w") as file_obj:
                # update the json
                data = get_epic_free_games_json()
                dump(data, file_obj)


    except FileNotFoundError:


        with open(PATH_TO_EPIC_DATA, "w") as file_obj:

            data = get_epic_free_games_json()
            dump(data, file_obj)


    print( " , ".join(data["names"]) )


def get_epic_free_games_json() -> dict:

    request = get('https://epic-free-games1.p.rapidapi.com/currentGames' , headers = {
    'x-rapidapi-key': "3c80cd1d39msh4646d536d544796p186b57jsn362c1681c902",
    'x-rapidapi-host': "epic-free-games1.p.rapidapi.com"
        } )


    if request.status_code == 200:


        format_result = {"names":[] , "expire_date":"" }

        dates = []

        result_dict = request.json()

        for game_info in result_dict:

            if game_info["discountPrice"] != "0":
                break

            format_result["names"].append( game_info["title"] )
            dates.append( get_date(game_info["offerEndDate"]) )

        format_result[ "expire_date" ] = get_min_date( dates )


        return format_result

    else:
        # return an empty dict to write to json file and prevent error
        return {}

def get_date(input_string) -> str:
    # yyyy-mm-dd
    return input_string[:10]

def get_min_date(dates) -> str:

    min_date = dates[0]

    def date_compare(date1 , date2):
        year1 , month1 , day1 = map(int , date1.split("-"))
        year2 , month2 , day2 = map(int , date2.split("-"))

        if year1 < year2:
            return date1

        if year2 < year1:
            return date2

        if month1 < month2:
            return date1

        if month2 < month1 :
            return date2

        if day1 < day2:
            return date1

        if day2 < day1 :
            return date2

        # if reaching this point means that 2 date are the same
        return date1


    for date in dates:
        min_date = date_compare(min_date, date)

    return min_date


if __name__ == "__main__":
    main()
