""" 
Program: Job Application Tracker
by Alberto Medina 
Purpose: This program helps users track job applications from the terminal.
It allows users to view applications, add new applications, update status, seach by company, 
and count applications by status"""

from applications import view_applications, add_applications, update_application_status, search_by_company, count_applications_by_status

def show_menu():
    """Displays the main menu options for the user"""
    print("\nJob Application Tracker")
    print("1. View all applications")
    print("2. Add a new application")
    print("3. Update application status")
    print("4. Search by company")
    print("5. Count applications by status")
    print("6. Exit")


def main(): 
    """runs the main program loop"""
    applications = [
        {
            "company": "OCLC",
            "title": "Data Analytics Intern",
            "date_applied": "2026-06-25",
            "status": "Applied",
            "notes": "Submitted application through company website."
        },
        {
            "company": "Cardinal Health",
            "title": "Junior Data Analyst",
            "date_applied": "2026-06-26",
            "status": "Wishlist",
            "notes": "Need to review job description before applying."
        }
    ]
    
    running = True

    while running: 
        show_menu()
        choice = input("Chose an option: ")

        if choice == "1":
            view_applications(applications)
        elif choice =="2":
            add_applications(applications)
        elif choice == "3":
            update_application_status(applications)
        elif choice == "4":
            search_by_company(applications)
        elif choice == "5":
            count_applications_by_status(applications)
        elif choice == "6":
            print("Thank you for using Job Application Tracker. Goodbye!")
            running = False
        else: 
            print("Invalid option. Please choose a number from 1 to 6.")        

if __name__ == "__main__":
    main()
