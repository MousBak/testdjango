
## Objective: 
Create an app in django with posgreSQL to save and search book. Use Docker to local postgress.
Design and implement APIs using Django REST Framework, create a documentation for launch the project.


### Task: 
  1. Endpoint for saving books:

            Method: POST
            Route: /test/books/
            Payload:
            Title: String
            Author: String
            Description: String (optional)
            ISBN: String (unique)
            Publication date: Date (optional)
     
  3. Endpoint for searching books:

          Method: GET
          Route: /test/books/search/
          Parameters:
          q: String (search parameter by title or author)

     
3. Data model:

        Entity: Book
        Attributes:
        ID: Integer (auto-generated primary key)
        Title: String
        Author: String
        Description: String (optional)
        ISBN: String (unique)
        Publication date: Date (optional)
        Creation date: Date (auto-generated)
        Update date: Date (auto-generated)
   
5. Implementation:

        Framework: Django
        Database: PostgreSQL
        API: Django REST Framework

6. Create a initial migration


      JSON of data for initial migration:

```json
[
  {
    "title": "The Little Prince",
    "author": "Antoine de Saint-Exupéry",
    "description": "An aviator crashes in the desert and meets a little prince who has traveled from a distant asteroid.",
    "isbn": "978-2-07-057428-9",
    "publication_date": "1943-04-01"
  },
  {
    "title": "One Hundred Years of Solitude",
    "author": "Gabriel García Márquez",
    "description": "The story of the Buendía family over seven generations in Macondo, a fictional village in Colombia.",
    "isbn": "978-84-264-1828-6",
    "publication_date": "1967-05-30"
  },
  {
    "title": "1984",
    "author": "George Orwell",
    "description": "A man lives in a dystopian society where the government constantly monitors him.",
    "isbn": "978-84-663-1632-9",
    "publication_date": "1949-06-08"
  }
]
```

5. Deliverables:

        Application source code (this repository)
        API documentation (new readme to how to run the project)
   



