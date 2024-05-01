import json

def load_user_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def display_user_details(user_data):
    for user in user_data['users']:
        print("User ID:", user['id'])
        print("Name:", user['name'])
        print("Email:", user['email'])
        print("Address:", user['address'])
        print()

if __name__ == "__main__":
    file_path = "users.json"  # Path to your JSON file
    user_data = load_user_data(file_path)
    display_user_details(user_data)
