### Timelog

Sample Django application (learning purposes)

### Development
```bash
$ git clone https://github.com/bleepster/timelog.git
$ cd timelog
$ python -m venv timelog-env
$ source timelog-env/bin/activate
$ pip install requirements-dev.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver 
```
_NOTE_: currently using Python 3.6.9

### TODO
- [x] User Log Detailed View
- [ ] Search by Username
- [ ] Search by Date
- [ ] Edit User Log 
- [ ] Delete User Log
- [ ] Link the Table View with the Detailed View
- [ ] Unit Testing

### Nice to have (in the future)
- [ ] Authentication
- [ ] Mulitple Projects
- [ ] Redistributable
