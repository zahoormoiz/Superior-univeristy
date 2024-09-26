class Book:
    def __init__(self, title, author, publication_year):
        self.title = title 
        self.author = author  
        self.publication_year = publication_year  

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Publication Year: {self.publication_year}"

title = input("Enter the title of the book: ")
author = input("Enter the author of the book: ")
publication_year = int(input("Enter the publication year of the book: "))

my_book = Book(title, author, publication_year)

print(my_book) 