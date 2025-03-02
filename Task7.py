import json

# Read the JSON data from the file
with open('resources/example.json', 'r') as file:
    data = json.load(file)

# Iterate over each item in the data and print specific fields
for person in data:
    # Extract specific fields with default value if not found
    person_id = person.get('id', 'N/A')
    name = person.get('name', 'N/A')
    email = person.get('email', 'N/A')
    age = person.get('age', 'N/A')

    # Print the formatted data
    print(f"ID: {person_id}")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Age: {age}")
    print("-" * 30)