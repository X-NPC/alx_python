#!/usr/bin/env python3

"""
Fetches information about all employees' TODO list progress using a REST API and exports it in JSON format.
"""

import json
import requests

def get_all_employees_todo_progress():
    """
    Fetches all employees' TODO list progress and exports it in JSON format.
    """
    # Fetch all employees
    users_url = "https://jsonplaceholder.typicode.com/users"
    users_response = requests.get(users_url)
    users_data = users_response.json()

    # Dictionary to store data
    all_data = {}

    # Iterate over each employee
    for user in users_data:
        user_id = user.get('id')
        username = user.get('name')

        # Fetch employee TODO list
        todos_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        # Collect todo data for this employee
        user_todos = []
        for todo in todos_data:
            user_todos.append({"username": username, "task": todo.get('title'), "completed": todo.get('completed')})

        # Add data to the dictionary
        all_data[user_id] = user_todos

    # Export to JSON
    json_filename = "todo_all_employees.json"
    with open(json_filename, 'w') as jsonfile:
        json.dump(all_data, jsonfile, indent=4)
    print(f"Data exported to {json_filename}")

if __name__ == "__main__":
    get_all_employees_todo_progress()
