"""
Program: Job Application Tracker
by-- Alberto Medina -- 
Purpose: This file contains helper functions for managing job applications.
It includes logic for viewing job applications stored in a list of dictionaries.
"""


def view_applications(applications):
    """Display all job applications stored in the applications list."""
    if not applications:
        print("\nNo job applications have been added yet.")
    else:
        print("\nSaved Job Applications:")

        for application in applications:
            print("-" * 40)
            print(f"Company: {application['company']}")
            print(f"Job Title: {application['title']}")
            print(f"Date Applied: {application['date_applied']}")
            print(f"Status: {application['status']}")
            print(f"Notes: {application['notes']}")