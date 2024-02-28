#!/usr/bin/env python3

"""
Fetches information about an employee's TODO list progress using a REST API.
"""

import requests
import sys

def get_employee_todo_progress(employee_id):
    """
    Fetches employee TODO list progress and displays it in the specified format.

    Args:
        employee_id (int): The ID of the employee.
    """
    # Fetch employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()
    employee_name = employee_data.get('name')

    if not employee_name:
        print(f"Employee with ID {employee_id} not found.")
        return

    # Fetch employee TODO list
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Calculate progress
    total_tasks = len(todos_data)
    done_tasks = sum(1 for todo in todos_data if todo.get('completed'))

    # Display progress
    print(f"Employee {employee_name} is done with tasks ({done_tasks}/{total_tasks}):")
    for todo in todos_data:
        if todo.get('completed'):
            print(f"\t{todo.get('title')}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
