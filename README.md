# Breve Dev

A simple website for organizing developer meetings and events that makes it easy to find a nearby coffee shop.

---

## Development

This project uses Django 1.1 and Python 3

To get started setup a Virtual Environment and install Django. You'll need pip and virtualenv as well as Python 3.

(Windows)

```
virtualenv venv

call venv/Scripts/activate

pip install Django==1.10
```

(Unix)

```
virtualenv -p python3 venv

source venv/bin/activate

pip install Django==1.10
```

Then cd into the main directory and start a development server.

```
python manage.py runserver
```

---

To add start developing a new feature create a new branch and check it out.

```
git checkout -b new_branch_name
```

Then to submit it for review commit the changes then push to origin.

```
git push -u origin HEAD
```

Finally submit a pull request to review the code.

---

## Authors

- **Luke Draper** - [Luke-Draper](https://github.com/Luke-Draper)
- **Jalen Varas** - [varasjalen](https://github.com/varasjalen)
- **Adam Todd** - [lxswiftxl](https://github.com/lxswiftxl)

See also the list of [contributors](https://github.com/Luke-Draper/brevedev/contributors) who participated in this project.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

---

## Acknowledgments

- Hat tip to anyone whose code was used
- Meetup.com for inspiration
