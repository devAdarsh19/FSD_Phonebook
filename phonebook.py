import sqlite3

# Create a connection to the database
conn = sqlite3.connect('contacts.db')

# Create a cursor object
c = conn.cursor()

# Create the contacts table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT NOT NULL
            )''')

# Add a new contact
def add_contact(name, phone):
    c.execute("INSERT INTO contacts (name, phone) VALUES (?, ?)", (name, phone))
    conn.commit()

# Get all contacts
def get_all_contacts():
    c.execute("SELECT * FROM contacts")
    return c.fetchall()

# Get a contact by name
def get_contact_by_name(name):
    c.execute("SELECT * FROM contacts WHERE name = ?", (name,))
    return c.fetchone()

# Update a contact
def update_contact(id, name, phone):
    c.execute("UPDATE contacts SET name = ?, phone = ? WHERE id = ?", (name, phone, id))
    conn.commit()

# Delete a contact
def delete_contact(id):
    c.execute("DELETE FROM contacts WHERE id = ?", (id,))
    conn.commit()

# Close the connection to the database
# conn.close()

# Example usage:

add_contact('Alice', '123-456-7890')
add_contact('Bob', '987-654-3210')

print(get_all_contacts())

print(get_contact_by_name('Alice'))

update_contact(1, 'Alice Smith', '123-456-7890')

delete_contact(2)

print(get_all_contacts())