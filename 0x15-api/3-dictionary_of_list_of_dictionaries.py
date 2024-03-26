#!/usr/bin/python3
"""
    Model implementing a script that that exports
    data to JSON format

"""
import json
import requests


def convert_to_json_all_employees():
    """Converts employee data to JSON"""
    api_url = 'https://jsonplaceholder.typicode.com'
    user_url = '{}/users'.format(api_url)
    todo_url = '{}/todos'.format(api_url)

    users_res = requests.get(user_url)
    users_data = users_res.json()

    todos_res = requests.get(todo_url)
    todos_data = todos_res.json()

    tasks_by_user = {}

    for todo in todos_data:
        user_id = todo['userId']
        if user_id not in tasks_by_user:
            tasks_by_user[user_id] = []

        tasks_by_user[user_id].append({
                "username": next(
                    user['name'] for user in users_data if user['id']
                    == user_id),
                "task": todo['title'],
                "completed": todo['completed']
            })

    filename = "todo_all_employees.json"
    with open(filename, mode='w') as file:
        json.dump(tasks_by_user, file, separators=(', ', ': '))

    # print("Data exported to {}".format(filename))


if __name__ == "__main__":
    convert_to_json_all_employees()
