from book import Book
from student import Student

class LibraryManager:
    def __init__(self):
        self.books = []
        self.students = []

    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def add_book(self):
        print("\n--- Add Book ---")
        book_id = input("Enter Book ID: ").strip()
        if self.find_book(book_id):
            print("Error: Book ID already exists.")
            return

        title = input("Enter Title: ").strip()
        author = input("Enter Author: ").strip()
        
        try:
            quantity = int(input("Enter Quantity: "))
            if quantity < 0:
                raise ValueError("Quantity cannot be negative.")
        except ValueError as e:
            print(f"Invalid input: {e}")
            return

        self.books.append(Book(book_id, title, author, quantity))
        print("Book added successfully.")

    def display_books(self):
        print("\n--- View Books ---")
        if not self.books:
            print("Library is empty.")
            return
        for book in self.books:
            print(book)

    def search_book(self):
        print("\n--- Search Book ---")
        book_id = input("Enter Book ID to search: ").strip()
        book = self.find_book(book_id)
        if book:
            print(book)
        else:
            print("Book not found")

    def delete_book(self):
        print("\n--- Delete Book ---")
        book_id = input("Enter Book ID to delete: ").strip()
        book = self.find_book(book_id)
        try:
            if not book:
                raise KeyError("Book not found")
            self.books.remove(book)
            print("Book deleted successfully.")
        except KeyError as e:
            print(f"Error: {e}")

    def add_student(self):
        print("\n--- Add Student ---")
        student_id = input("Enter Student ID: ").strip()
        if self.find_student(student_id):
            print("Error: Student ID already exists.")
            return
        name = input("Enter Student Name: ").strip()
        self.students.append(Student(student_id, name))
        print("Student added successfully.")

    def display_students(self):
        print("\n--- View Students ---")
        if not self.students:
            print("No students registered.")
            return
        for student in self.students:
            print(student)

    def search_student(self):
        print("\n--- Search Student ---")
        student_id = input("Enter Student ID to search: ").strip()
        student = self.find_student(student_id)
        if student:
            print(student)
        else:
            print("Student not found.")

    def delete_student(self):
        print("\n--- Delete Student ---")
        student_id = input("Enter Student ID to delete: ").strip()
        student = self.find_student(student_id)
        if student:
            self.students.remove(student)
            print("Student deleted successfully.")
        else:
            print("Student not found.")

    def borrow_book(self):
        print("\n--- Borrow Book ---")
        book_id = input("Enter Book ID: ").strip()
        book = self.find_book(book_id)
        
        try:
            if not book:
                raise KeyError("Book not found")
            if book.quantity <= 0:
                raise ValueError("Book out of stock")
            
            book.quantity -= 1
            print("Book borrowed successfully.")
        except (KeyError, ValueError) as e:
            print(f"Error: {e}")

    def return_book(self):
        print("\n--- Return Book ---")
        book_id = input("Enter Book ID: ").strip()
        book = self.find_book(book_id)
        
        try:
            if not book:
                raise KeyError("Book not found")
            book.quantity += 1
            print("Book returned successfully.")
        except KeyError as e:
            print(f"Error: {e}")