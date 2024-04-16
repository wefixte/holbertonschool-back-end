#!/usr/bin/python3
""" Python script to export data in the JSON format """

import json
import requests
import sys

API_URL = "https://jsonplaceholder.typicode.com/"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    employee = requests.get(API_URL + "users/{}".format(employee_id)).json()
    todos = requests.get(API_URL + "todos",
                         params={"userId": employee_id}).json()
    done_tasks = [task for task in todos if task.get("completed") is True]

    all_employees_data = {}

    # This part is always wrong so trying again after

    json_file = "todo_all_employees.json"

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_employees_data, jsonfile)
