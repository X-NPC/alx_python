#!/usr/bin/env python3

"""
Fetches information about an employee's TODO list progress using a REST API and exports it in CSV format.
"""

import csv
import requests

import sys

def get_employee_todo_progress(employee_id):
    """
    Fetches employee TODO list progress and exports it in CSV format.

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

    # Export to CSV
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for todo in todos_data:
            csv_writer.writerow([employee_id, employee_name, todo.get('completed'), todo.get('title')])
    print(f"Data exported to {csv_filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
