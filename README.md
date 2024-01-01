# Channel_App

## Enjoy Reading

> This project is for creating posts. It is designed so that only admins can publish posts, and other users can only read those posts.


![image](https://github.com/mirafzal114/apelsinmarket/assets/136591233/06eac94e-fd64-491a-a81a-570dd37f9bf0)

![image](https://github.com/mirafzal114/apelsinmarket/assets/136591233/e1e93d29-2992-4faa-aaff-7eac500b8cbf)

![image](https://github.com/mirafzal114/apelsinmarket/assets/136591233/a5a47539-a847-4f8b-888c-89a95adb2738)




**A sample program works like this.


## Installation and Usage
## Project using pipenv
### The first step you must take is to work with pipenv

This project uses the pipenv tool to manage dependencies and the Python virtual environment.

### Install pipenv

1. Make sure Python is installed on your computer.
2. Install pipenv using the command:

   ```
    $ pip install pipenv
    ```
3. Install dependencies by running `pip install -r requirements.txt`

### Cloning the project and installing dependencies

1. Clone the repository:
    ```
    $ git clone https://github.com/mirafzal114/apelsinmarket.git
    ```
2. Access the repository:
    ```
    $ git clone https://github.com/mirafzal114/apelsinmarket.git
    ```

3. Run the `pipenv install` command to create a virtual environment and install all dependencies from the `Pipfile.lock` file.

### Working with the project

- To activate the virtual environment, run:
    ```
    pipenv shell
    ```
- To install new dependencies run:
    ```
    pipenv install <package_name>
    ```
- To run scripts or an application from your project, use ``pipenv run``.

  **After you have logged into the `(mandarinshop) mandarinshop` environment, you will have `(mandarinshop) mandarinshop` in this form.

```bash
$ python manage.py makemigrations
```

**This will create all the migration files (database migrations) needed to run this application.

**To apply this migration, run the following command**
```bash
$ python manage.py migrate
```
**One final step, and then our application will be running. We need to create an admin user to run this application. Type the following command in the terminal and provide a username, password, and email address for the admin user.**
```bash
$ python manage.py createsuperuser
```
 ** Run the program with
 **Start the program with the command:**
```bash
$ python manage.py runserver
```

4. Exit the environment:
    ````bash
    $ exit
    ````
