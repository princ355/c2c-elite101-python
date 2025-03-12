
"""
    Welcome to Elite 101 this program is a starter for your chatbot project.
    The starter prompts the user to enter their name and then greets them with a personalized message.

    Functions:
        get_user_name(): Prompts the user to enter their name and returns it.
        greet_user(name): Prints a greeting message using the provided name.
        main(): Main function that orchestrates the user input and greeting process.

    Execution:
        When the script is run directly (not imported as a module), it will execute the main() function.
"""

def get_user_name():
    return input("Can I get your name please? ")

def greet_user(name):
    print(f"Hello, {name}! How may I be of assistance with you today? ")


def ask_for_order_number(self):
    order_digits= input("Please enter your order number:")
    self.check_order_status(order_number)
def check_order_status(self, order_number):
    if order_number in orders:
        status= orders[order_number]
        if status == "Out for delivery":
            print(f"Your order is on its way and will arrive soon.")
        elif status == "Preparing":
            print(f"Your order is being prepared now.")
        elif status == "Delivered":
            print(f"Your order had been delivered! If you haven't received please contact support.")
        else: 
            print("Sorry, we couldn't find your order. Please re-enter your order number again.")
            
def main():
    print{"Welcome to Princess's delivery HELP CHATBOT!"}
    user_name = get_user_name()
    greet_user(user_name)
    ask_for_order_number()
    check_order_status()

def orders= {
    12345: {"Status": "Out for delivery" "Estimated time": "12 minutes "Driver ": "John Doe" "Contact info:" "(123)-234-5678"}
    67890: {"Status": "Preparing", "Estimated_time": "35 minutes" "Driver": None "Contact": None} 
    17181: {"status": "Delivered" "Estimated_time": "0 minutes" "Driver": "John Doe" "Contact info": "(123)-234-5678"}
}
