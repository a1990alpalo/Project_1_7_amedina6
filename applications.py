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

    
    
    
def add_applications(applications):
    """Asks the user for job application details and adds it to the list"""
    print("\nAdd new job application")

    company = input("Company name: ")
    title = input("Job title: ")
    date_applied = input("Date applied: ")
    status = input("Status: ")
    notes = input("Notes: ")

    new_application = {
        "company": company,
        "title": title,
        "date_applied": date_applied,
        "status": status,
        "notes": notes
    }

    applications.append(new_application)
    print(f"\nApplication for {title} at {company} has beed added to the list")


def update_application_status(applications):
    """Updates the status of a job applications for a company"""
    if not applications:
        print("\nNo job applications are available to update.")
        return
    
    company_search = input("\nEnter the company name to update")
    applications_found = False

    for application in applications:
        if application["company"] == company_search:
            print(f"\nCurrent status for {application["company"]}: {application["status"]}")
            new_status = input("Enter the new status: ")

            application["status"] = new_status
            applications_found = True

            print(f"\nStatus updated to: {new_status}")

    if not applications_found:
        print("\nNo application found for that company.")

def search_by_company(applications):
    """Sarch for applications by company name"""
    company_name = input("Enter the company name to search: ")

    found = False

    for application in applications:
        if company_name in application["company"].lower():
            print("\nApplication Found:")
            print(f"Company: {application['company']}")
            print(f"Title: {application['title']}")
            print(f"Date applied:{application['date_applied']}")
            print(f"Status: {application['status']}")
            print(f"Notes: {applications['notes']}")
            found = True

    if not found:
        print("No application found for that company.")

def count_applications_by_status(applications):
    """Count and display the applications by status!"""
    status_count = {}

    for application in applications:
        status = application['status']

        if status in status_count:
            status_count[status] += 1
        else: 
            status_count[status] = 1

    print("\nApplication Count by status: ")

    for status, count in status_count.items():
        print(f"{status}: {count}")