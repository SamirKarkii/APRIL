Library = { "Man’s Search for Meaning" : {"author":"abc", "status":"Available "},
         "The Alchemist": {"author":"def", "status":"Availabel"}, 
         "Meditations": {"author":"ghi", "status": "Checked Out"},
         "The Great Gatsby": {"author": "F. Scott Fitzgerald", "status": "Available"},
    "1984": {"author": "George Orwell", "status": "Checked Out"},
    "The Hobbit": {"author": "J.R.R. Tolkien", "status": "Available"}
}

Library["1984"]["status"] = "Available"

user = input("Enter the a book title:").title()
if user in Library.keys():
    print(f'We have the book by {Library[user]["author"]}')
else:
    print("Sorry, we don't have that one")

for i,j in Library.items():
    if Library[i]["status"] == "Available":
        print(f'{i} is Available')
    else:
        print(f'{i} is not available')