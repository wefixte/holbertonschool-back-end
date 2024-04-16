#!/usr/bin/python3
""" Script that export data in the JSON format """

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

    with open("{}.json".format(employee_id), "w") as jsonfile:
        json.dump({employee_id: [{
            "task": task.get("title"), "completed": task.get("completed"),
            "username": employee.get("username")}
            for task in todos]}, jsonfile)
