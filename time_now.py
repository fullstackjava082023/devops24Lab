import datetime

def ask_for_time():
    user_input = input("Do you want to know the current time? (y/n): ").strip().lower()
    
    if user_input == 'y':
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"The current local time is: {current_time}")
    elif user_input == 'n':
        print("Okay, have a great day!")
    else:
        print("Please answer with 'y' or 'n'.")
        ask_for_time()

ask_for_time()
