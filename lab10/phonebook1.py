import psycopg2
from psycopg2 import sql
import csv

# Database connection parameters
DB_NAME = "lab10"
DB_USER = "postgres"
DB_PASSWORD = "Asylzhan2007"
DB_HOST = "localhost"
DB_PORT = "5432"

def create_connection():
    """Create a database connection"""
    conn = None
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )
        print("Connection to PostgreSQL DB successful")
        return conn
    except psycopg2.OperationalError as e:
        print(f"The error '{e}' occurred")
        return None

def create_tables(conn):
    """Create PhoneBook table if it doesn't exist"""
    create_table_query = """
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50),
        phone VARCHAR(20) NOT NULL UNIQUE,
        email VARCHAR(100),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_query)
        conn.commit()
        print("Table created successfully")
    except psycopg2.Error as e:
        print(f"The error '{e}' occurred")

def insert_from_csv(conn, file_path):
    """Insert data from CSV file into phonebook"""
    try:
        cursor = conn.cursor()
        
        with open(file_path, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Skip header row if exists
            
            for row in reader:
                # Assuming CSV format: first_name,last_name,phone,email
                insert_query = """
                INSERT INTO phonebook (first_name, last_name, phone, email)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (phone) DO NOTHING;
                """
                cursor.execute(insert_query, row)
        
        conn.commit()
        print(f"Data from {file_path} inserted successfully")
    except (psycopg2.Error, FileNotFoundError) as e:
        print(f"The error '{e}' occurred")
        conn.rollback()

def insert_from_console(conn):
    """Insert data from user input into phonebook"""
    print("\nEnter new contact information:")
    first_name = input("First name: ").strip()
    last_name = input("Last name (optional): ").strip() or None
    phone = input("Phone number: ").strip()
    email = input("Email (optional): ").strip() or None
    
    try:
        cursor = conn.cursor()
        insert_query = """
        INSERT INTO phonebook (first_name, last_name, phone, email)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (phone) DO NOTHING
        RETURNING id;
        """
        cursor.execute(insert_query, (first_name, last_name, phone, email))
        
        result = cursor.fetchone()
        if result:
            print(f"Contact added successfully with ID: {result[0]}")
        else:
            print("A contact with this phone number already exists.")
        
        conn.commit()
    except psycopg2.Error as e:
        print(f"The error '{e}' occurred")
        conn.rollback()

def update_contact(conn):
    """Update contact information"""
    print("\nUpdate contact information")
    phone = input("Enter phone number of the contact to update: ").strip()
    
    # Check if contact exists
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM phonebook WHERE phone = %s;", (phone,))
    contact = cursor.fetchone()
    
    if not contact:
        print("No contact found with that phone number.")
        return
    
    print(f"\nCurrent contact information:")
    print(f"1. First name: {contact[1]}")
    print(f"2. Last name: {contact[2]}")
    print(f"3. Phone: {contact[3]}")
    print(f"4. Email: {contact[4]}")
    
    field = input("\nEnter the number of the field to update (1-4): ").strip()
    new_value = input("Enter the new value: ").strip()
    
    field_map = {
        '1': 'first_name',
        '2': 'last_name',
        '3': 'phone',
        '4': 'email'
    }
    
    if field not in field_map:
        print("Invalid field selection.")
        return
    
    try:
        update_query = sql.SQL("""
        UPDATE phonebook
        SET {} = %s
        WHERE phone = %s
        """).format(sql.Identifier(field_map[field]))
        
        cursor.execute(update_query, (new_value, phone))
        conn.commit()
        print("Contact updated successfully")
    except psycopg2.Error as e:
        print(f"The error '{e}' occurred")
        conn.rollback()

def query_contacts(conn):
    """Query contacts with different filters"""
    print("\nQuery options:")
    print("1. Search by first name")
    print("2. Search by last name")
    print("3. Search by phone number")
    print("4. Search by email")
    print("5. Show all contacts")
    
    option = input("Select query option (1-5): ").strip()
    
    query_map = {
        '1': ('first_name', 'Enter first name to search: '),
        '2': ('last_name', 'Enter last name to search: '),
        '3': ('phone', 'Enter phone number to search: '),
        '4': ('email', 'Enter email to search: '),
        '5': (None, None)
    }
    
    if option not in query_map:
        print("Invalid option selected.")
        return
    
    field, prompt = query_map[option]
    
    try:
        cursor = conn.cursor()
        
        if option == '5':
            cursor.execute("SELECT * FROM phonebook ORDER BY first_name;")
        else:
            search_term = input(prompt).strip()
            query = sql.SQL("""
            SELECT * FROM phonebook 
            WHERE {} ILIKE %s 
            ORDER BY first_name;
            """).format(sql.Identifier(field))
            cursor.execute(query, (f"%{search_term}%",))
        
        contacts = cursor.fetchall()
        
        if not contacts:
            print("No contacts found.")
            return
        
        print("\nContacts:")
        print("-" * 60)
        for contact in contacts:
            print(f"ID: {contact[0]}")
            print(f"Name: {contact[1]} {contact[2] or ''}")
            print(f"Phone: {contact[3]}")
            print(f"Email: {contact[4] or 'N/A'}")
            print(f"Added on: {contact[5]}")
            print("-" * 60)
            
    except psycopg2.Error as e:
        print(f"The error '{e}' occurred")

def delete_contact(conn):
    """Delete contact by username or phone"""
    print("\nDelete contact")
    print("1. Delete by first name")
    print("2. Delete by phone number")
    
    option = input("Select delete option (1-2): ").strip()
    
    if option not in ['1', '2']:
        print("Invalid option selected.")
        return
    
    try:
        cursor = conn.cursor()
        
        if option == '1':
            first_name = input("Enter first name to delete: ").strip()
            # First show matching contacts
            cursor.execute("SELECT * FROM phonebook WHERE first_name ILIKE %s;", (f"%{first_name}%",))
            contacts = cursor.fetchall()
            
            if not contacts:
                print("No contacts found with that first name.")
                return
            
            print("\nMatching contacts:")
            for i, contact in enumerate(contacts, 1):
                print(f"{i}. {contact[1]} {contact[2] or ''} - {contact[3]}")
            
            choice = input("Enter the number of the contact to delete (or 'all' to delete all): ").strip()
            
            if choice.lower() == 'all':
                cursor.execute("DELETE FROM phonebook WHERE first_name ILIKE %s;", (f"%{first_name}%",))
                print(f"Deleted {cursor.rowcount} contacts.")
            elif choice.isdigit() and 1 <= int(choice) <= len(contacts):
                contact_id = contacts[int(choice)-1][0]
                cursor.execute("DELETE FROM phonebook WHERE id = %s;", (contact_id,))
                print("Contact deleted successfully.")
            else:
                print("Invalid selection.")
        
        elif option == '2':
            phone = input("Enter phone number to delete: ").strip()
            cursor.execute("DELETE FROM phonebook WHERE phone = %s RETURNING id;", (phone,))
            deleted_id = cursor.fetchone()
            
            if deleted_id:
                print("Contact deleted successfully.")
            else:
                print("No contact found with that phone number.")
        
        conn.commit()
    except psycopg2.Error as e:
        print(f"The error '{e}' occurred")
        conn.rollback()

def main_menu():
    """Display main menu and handle user input"""
    conn = create_connection()
    if not conn:
        return
    
    create_tables(conn)
    
    while True:
        print("\nPhoneBook Application")
        print("1. Insert contacts from CSV file")
        print("2. Insert contact from console")
        print("3. Update contact")
        print("4. Query contacts")
        print("5. Delete contact")
        print("6. Exit")
        
        choice = input("Select an option (1-6): ").strip()
        
        if choice == '1':
            file_path = input("Enter CSV file path: ").strip()
            insert_from_csv(conn, file_path)
        elif choice == '2':
            insert_from_console(conn)
        elif choice == '3':
            update_contact(conn)
        elif choice == '4':
            query_contacts(conn)
        elif choice == '5':
            delete_contact(conn)
        elif choice == '6':
            print("Exiting application...")
            break
        else:
            print("Invalid choice. Please try again.")
    
    conn.close()

if __name__ == "__main__":
    main_menu()