import datetime
import time
import os
import sys
import sched # Events can be scheduled to run at a specific time.
import platform

# Initialize the scheduler
reminder_scheduler = sched.scheduler(time.time, time.sleep)

def add_reminder(reminder_message, year, month, day, hour, minute):
    reminder_time = datetime.datetime(year, month, day, hour, minute)
    now = datetime.datetime.now()

    if reminder_time < now:
        print("Invalid reminder time.")
        return

    delay = (reminder_time - now).total_seconds()
    reminder_scheduler.enter(delay, 1, display_reminder, (reminder_message,))


def display_reminder(reminder_text):
    os.system(platform.system() == 'Windows' and 'cls' or 'clear')  # Clear the terminal screen
    print("Reminder:", reminder_text)


def main():
    while True:
        print("\nReminder Menu:")
        print("1. Add Reminder")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            reminder_message = input("Enter the reminder message: ")
            year = int(input("Enter the year (like 2023): "))
            month = int(input("Enter the month (1-12): "))
            day = int(input("Enter the day (1-31): "))
            hour = int(input("Enter the hour (0-23): "))
            minute = int(input("Enter the minute (0-59): "))

            add_reminder(reminder_message, year, month, day, hour, minute)
            print("Reminder added successfully.")
        elif choice == '2':
            print("Exit Reminder Application.")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

try:
    reminder_scheduler.run()
except KeyboardInterrupt:
    print("Reminder application terminated.")
