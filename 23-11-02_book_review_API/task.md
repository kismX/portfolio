**## Coding Exercise: Building a Book Review API**
***Goal:*** 
Your objective is to build a Django API for storing and fetching book reviews.

**### Instructions:**

1. ***Initial Set Up:***
    - Create a new directory named `book_reviews`.
    - Set up a virtual environment and activate it.
    - Install Django in this environment.
    - Create a new Django project named `review_project`.
    - Start a new app named `reviews`.
    - Migrate the project to set up the initial database.
    - Add the `reviews` app to the `INSTALLED_APPS` setting.
    
    
    2. ***Git Setup:***

- Initialize a new git repository within the `book_reviews` directory.
- Create a `.gitignore` file and add entries for:
  1. `.venv`
  2. `*.pyc`
  3. `db.sqlite3` (or your chosen database file)
- Commit your changes with the message "initial commit".


3. ***Models:***
- Define a `Book` model with fields:
  - `title`: CharField (max length of 255 characters)
  - `author`: CharField (max length of 255 characters)
- Define a `Review` model with fields:
  - `book`: ForeignKey relating to the `Book` model
  - `review_text`: TextField
  - `rating`: IntegerField (with a range between 1 to 5)
- Migrate your models.


4. ***Admin Interface:***
- Register both `Book` and `Review` models with the Django admin site.
- Create a superuser account to manage your data via the admin interface.


5. ***Tests:***
- Write tests for both `Book` and `Review` models to ensure that their data is stored correctly and that their string representations (`__str__` method) are correct.


6. ***Serializers:***
- Create a serializer for `Book` model displaying `id`, `title`, and `author`.
- Create a serializer for `Review` model displaying `id`, `book`, `review_text`, and `rating`.


7. ***URLs:***
- Ensure all API endpoints have a consistent path such as `api/`.
- Define URLs for:
  1. List and detail views of books (e.g., `api/books/` and `api/books/<id>/`)
  2. List and detail views of reviews (e.g., `api/reviews/` and `api/reviews/<id>/`)
  
  
  8. ***Views:***
- Use Django REST Framework's generic views to create:
  - List and detail views for `Book`.
  - List and detail views for `Review`.
  
  
  9. ***Browsable API:***
- Test your API using Django REST Framework’s browsable interface. 
- Add a few books and reviews through the interface and ensure that they are retrievable through the API endpoints.
