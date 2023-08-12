import json
from datetime import datetime


def save_list(hour_list):
    with open("./data/gpt_limit.json", "w") as file:
        json.dump(hour_list, file)


def read_list():
    with open("./data/gpt_limit.json", "r") as file:
        return json.load(file)


# hour_list = [hour, count]
def is_under_limit(limit):
    hour = datetime.now().hour
    hour_list = read_list()
    if hour == hour_list[0]:
        if hour_list[1] < limit:
            hour_list[1] += 1
            save_list(hour_list)
            return [True, hour_list[1]]
        else:
            return [False, hour_list[1]]
    else:
        hour_list[0] = hour
        hour_list[1] = 1
        save_list(hour_list)
        return [True, hour_list[1]]
