
# To-Do List Application Using Django

This is a simple To-Do List application built using Django, a high-level Python web framework. This application allows users to manage their tasks by adding, viewing, editing, and deleting to-do items.
## Features

- **User Authentication**: Users can register, log in, and log out.
- **Task Management**: Users can create, view, edit, and delete tasks.
- **Task Status**: Users can mark tasks as completed or pending.
- **Responsive Design**: The application is designed to be responsive and user-friendly on both desktop and mobile devices.
## Requirements
- Python 3 (https://www.python.org/downloads/)
- Django (included in most Python installations)

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/BiTech5/to-do-list-django
    ```
2. **Navigate to the project directory:**
    ```bash
    python manage.py migrate

    ```
3. **Create SuperUser**
    ```bash
    python manage.py createsuperuser
    ```
3. **Run the program:**
    ```bash
    python manage.py runserver
    ```

## Usage
1. **Register**
- Go to the registration page and create a new account.
- After registration, log in using your credentials.
2. **Add a Task**
- Click on the "Add Task" button.
- Enter the task details and save.
3. **Delete a Task**
- Click on the task you want to delete.
4. **Mark Task as Completed**
- Click on the finished button next to the task to mark it as completed.
## Contributing
Contributions are welcome! Please follow these steps to contribute:


1. Fork the repository.
2. Create a new branch for your feature or bug fix:
    ```bash
    git checkout -b feature-name
    ```
3. Commit your changes:
    ```bash
    git commit -m "Description of your feature or fix"
    ```
4. Push to the branch:
    ```bash
    git push origin feature-name
    ```
5. Create a pull request on GitHub.




## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.



## Acknowledgements

We welcome contributions to this project. If you have any improvements or suggestions, please fork the repository and submit a pull request.
