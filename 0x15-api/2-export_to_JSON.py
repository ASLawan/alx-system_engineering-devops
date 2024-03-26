#!/usr/bin/python3
"""
    Model implementing a script that that exports
    data to JSON format

"""
import json
import requests
import sys


def convert_to_json(employee_id):
    """Converts employee data to CSV"""
    api_url = 'https://jsonplaceholder.typicode.com'
    user_url = '{}/users/{}'.format(api_url, employee_id)
    todo_url = '{}/todos?userId={}'.format(api_url, employee_id)

    user_res = requests.get(user_url)
    user_data = user_res.json()

    todo_res = requests.get(todo_url)
    todo_data = todo_res.json()

    json_data = {
            '{}'.format(user_data['id']): [
                {
                    "task": todo['title'],
                    "completed": todo['completed'],
                    "username": user_data['username']
                }
                for todo in todo_data
            ]
        }

    filename = "{}.json".format(employee_id)
    with open(filename, mode='w') as file:
        json.dump(json_data, file, separators=(', ', ': '))

    print("Data exported to {}".format(filename))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        exit(1)

    employee_id = int(sys.argv[1])
    convert_to_json(employee_id)
