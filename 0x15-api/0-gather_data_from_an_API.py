#!/usr/bin/python3
"""
    Module implementing a script that uses an API
    to return employee information.

"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """Prints employee todo progress"""
    base_url = 'https://jsonplaceholder.typicode.com'
    todo_url = '{}/todos'.format(base_url)
    user_url = '{}/users/{}'.format(base_url, employee_id)

    user_res = requests.get(user_url)
    if user_res.status_code != 200:
        print(f"Error fetching employee info")
        return
    user_data = user_res.json()
    employee_name = user_data['username']

    todo_res = requests.get(todo_url, params={'userId': employee_id})
    if todo_res.status_code != 200:
        print(f"Error fetching TODO list")
        return
    todo_data = todo_res.json()
    ttl = len(todo_data)
    cpltd = sum(1 for task in todo_data if task['completed'])
    print(f"Employee {employee_name} is done with tasks({cpltd}/{ttl})")
    for task in todo_data:
        if task['completed']:
            print(f"\t{task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py employee_id")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
