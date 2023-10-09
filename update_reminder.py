  # Importing the necessary libraries
import ctypes  # For displaying a Windows MessageBox
import time    # For handling time-related functions

# Function to display a Windows MessageBox with a reminder
def check_for_updates():
    ctypes.windll.user32.MessageBoxW(0, "Check for system update!", "System Update Reminder", 0x40)

# Main execution block
if __name__ == "__main__":
    # Define the time interval for the reminder (one week in seconds)
    one_week = 7 * 24 * 60 * 60

    # Run the reminder loop indefinitely
    while True:
        check_for_updates()  # Display the reminder MessageBox
        time.sleep(one_week)  # Sleep for one week before showing the reminder again
