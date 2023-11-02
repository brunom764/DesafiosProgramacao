class Book {
  id: string;
  title: string;
  description: string;
  author: string;

  constructor(id: string, title: string, description: string, author: string) {
    this.id = id;
    this.title = title;
    this.description = description;
    this.author = author;
  }
}

class Library {
  books: Book[];

  constructor() {
    this.books = [];
  }

  addBook(bookInfo: {
    title: string;
    description: string;
    author: string;
  }): Book {
    const newBook = new Book(
      this.generateBookId(),
      bookInfo.title,
      bookInfo.description,
      bookInfo.author,
    );
    this.books.push(newBook);
    return newBook;
  }

  getBooks(): Book[] {
    return this.books;
  }

  removeBookById(id: string): void {
    const index = this.books.findIndex((book) => book.id === id);
    if (index !== -1) {
      this.books.splice(index, 1);
    }
  }

  getBookById(id: string): Book | undefined {
    return this.books.find((book) => book.id === id);
  }

  updateBookById(
    id: string,
    info: { title?: string; description?: string; author?: string },
  ): Book | undefined {
    const book = this.getBookById(id);
    if (book) {
      if (info.title) {
        book.title = info.title;
      }
      if (info.description) {
        book.description = info.description;
      }
      if (info.author) {
        book.author = info.author;
      }
    }
    return book;
  }

  private generateBookId(): string {
    return (
      Math.random().toString(36).substring(2) +
      new Date().getTime().toString(36)
    );
  }
}

// Ex:
const saraiva = new Library();

const book1 = saraiva.addBook({
  title: 'Harry Potter',
  description: 'Descrição xxxx bbbb yyyy',
  author: 'JK Rowling',
});

const book2 = saraiva.addBook({
  title: 'Jogos Vorazes',
  description: 'Descrição zzzzz bbbbb aaaa',
  author: 'Suzanne Collins',
});

console.log(saraiva.getBooks());

saraiva.updateBookById(book1.id, { title: 'Star wars' });
console.log(saraiva.getBooks());

saraiva.removeBookById(book2.id);
console.log(saraiva.getBooks());
