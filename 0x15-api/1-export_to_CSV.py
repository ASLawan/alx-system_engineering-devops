#!/usr/bin/python3
"""
    Model implementing a script that that exports
    data to CSV format

"""
import csv
import requests
import sys


def convert_to_csv(employee_id):
    """Converts employee data to CSV"""
    api_url = 'https://jsonplaceholder.typicode.com'
    user_url = '{}/users/{}'.format(api_url, employee_id)
    todo_url = '{}/todos?userId={}'.format(api_url, employee_id)

    user_res = requests.get(user_url)
    user_data = user_res.json()

    todo_res = requests.get(todo_url)
    todo_data = todo_res.json()

    filename = "{}.csv".format(employee_id)
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todo_data:
            writer.writerow([user_data['id'], user_data['name'],
                            todo['completed'], todo['title']])

    print("Data exported to {}".format(filename))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        exit(1)

    employee_id = int(sys.argv[1])
    convert_to_csv(employee_id)
