from library import LibraryManager

def show_menu():
    print("\n==================== LIBRARY MANAGEMENT ====================")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Add Student")
    print("6. View Students")
    print("7. Search Student")
    print("8. Delete Student")
    print("9. Borrow Book")
    print("10. Return Book")
    print("0. Exit")

def main():
    manager = LibraryManager()
    
    while True:
        show_menu()
        choice = input("Select an option (0-10): ").strip()
        
        match choice:
            case "1":
                manager.add_book()
            case "2":
                manager.display_books()
            case "3":
                manager.search_book()
            case "4":
                manager.delete_book()
            case "5":
                manager.add_student()
            case "6":
                manager.display_students()
            case "7":
                manager.search_student()
            case "8":
                manager.delete_student()
            case "9":
                manager.borrow_book()
            case "10":
                manager.return_book()
            case "0":
                print("Exiting program. Goodbye!")
                break
            case _:
                print("Invalid choice! Please select between 0 and 10.")

if __name__ == "__main__":
    main()