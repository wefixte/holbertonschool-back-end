#!/usr/bin/python3
""" Script that export data in the CSV format """

import csv
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

    with open("{}.csv".format(employee_id), "w") as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            csvwriter.writerow([employee_id, employee.get("username"),
                                task.get("completed"), task.get("title")])
