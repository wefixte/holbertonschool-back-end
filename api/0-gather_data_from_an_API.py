#!/usr/bin/python3
""" Script that returns info to-do list infos for given employee ID """

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

    print("Employee {} is done with tasks({}/{}):"
          .format(employee.get("name"), len(done_tasks), len(todos)))
    for task in done_tasks:
        print("\t {}".format(task.get("title")))
