# Parent class Document
class Document:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}")

# Child class Book inheriting from Document
class Book(Document):
    def __init__(self, title, author, genre=None, pages=None):
        super().__init__(title, author)
        self.genre = genre
        self.pages = pages

    def display_info(self):
        super().display_info()
        if self.genre and self.pages:
            print(f"Genre: {self.genre}, Pages: {self.pages}")

# Child class Article inheriting from Document
class Article(Document):
    def __init__(self, title, author, journal=None, doi=None):
        super().__init__(title, author)
        self.journal = journal
        self.doi = doi

    def display_info(self):
        super().display_info()
        if self.journal and self.doi:
            print(f"Journal: {self.journal}, DOI: {self.doi}")

# File handling functions
def save_document_to_file(filename, document):
    with open(filename, 'a') as file:
        if isinstance(document, Book):
            file.write(f"Book,{document.title},{document.author},{document.genre},{document.pages}\n")
        elif isinstance(document, Article):
            file.write(f"Article,{document.title},{document.author},{document.journal},{document.doi}\n")

def read_documents_from_file(filename):
    documents = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                doc_type = parts[0]
                if doc_type == "Book":
                    _, title, author, genre, pages = parts
                    documents.append(Book(title, author, genre, int(pages)))
                elif doc_type == "Article":
                    _, title, author, journal, doi = parts
                    documents.append(Article(title, author, journal, doi))
    except FileNotFoundError:
        print("File not found. No data to read.")
    return documents

def add_new_document(filename):
    doc_type = input("Enter document type (Book/Article): ").strip().lower()
    title = input("Enter title: ")
    author = input("Enter author: ")

    if doc_type == "book":
        genre = input("Enter genre: ")
        pages = int(input("Enter number of pages: "))
        new_book = Book(title, author, genre, pages)
        save_document_to_file(filename, new_book)
        print("Book information saved successfully.")
    elif doc_type == "article":
        journal = input("Enter journal: ")
        doi = input("Enter DOI: ")
        new_article = Article(title, author, journal, doi)
        save_document_to_file(filename, new_article)
        print("Article information saved successfully.")
    else:
        print("Invalid document type.")

# Example usage
if __name__ == "__main__":
    filename = "documents.txt"

    # Add a new document
    add_new_document(filename)

    # Read documents from file
    documents = read_documents_from_file(filename)

    # Display all document information
    for doc in documents:
        doc.display_info()
        print()
