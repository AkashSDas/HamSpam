
# HamSpam

  

  

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

  

[![](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)

  

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/AkashSDas)

  

[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://github.com/AkashSDas)

  

[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](LICENSE)

  

  

## Table of contents

  

  

*  [About](#about)

  

*  [Technologies Used](#technologies-used)

* [Results of the Project](#results-of-the-project)

*  [Metrics of the ML model used](#metrics-of-the-ml-model-used)

  

*  [ML Model source code](#ml-model-source-code)

  

*  [Installation](#installation)

  

*  [License](#license)

  

  

## About

  

> `Spam` and `Ham` classification is very useful since it save a lot of time of users. The time spend in reading spam emails are saved.

  

> This is the implementation of `machine learning model` that can classify `ham` and `spam` emails.

  
  

## Technologies Used

> [![](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/) is used as Programming Language.

  
  

> `Sciki-learn` is used to use the model for `prediction`.

  

> `Django` is used to build the backend of website.

  

> `HTML5`, `CSS3` and `Bootstrap4` is used for frontend of the website.

  

> `FontAwesome` is used for `icons`.

  

> `django-crispy-forms` package is used to to apply the styles of `bootstrap4` to the forms.

  

> `Pipenv` is the virtual environment used for the project. `Jupyter Notebook` is used to for the entire data science and machine learning life cycle.

## Results of the Project  

![Result](https://github.com/AkashSDas/HamSpam/blob/master/reults-gif-and-video/results.gif)


## Metrics of the ML model used

  

#### Metrics Scores

  

![Metrics Scores](https://github.com/AkashSDas/HamSpam/blob/master/project-results-images/metrics-scores.png)

  

#### Confusion Matrix

  

```python
precision    recall  f1-score   support

           0       0.99      1.00      0.99      1314
           1       1.00      0.97      0.98       405

    accuracy                           0.99      1719
   macro avg       0.99      0.98      0.99      1719
weighted avg       0.99      0.99      0.99      1719
```

  

![Confusion Matrix](https://github.com/AkashSDas/HamSpam/blob/master/project-results-images/confusion-matrix.png)

  

## ML Model source code

  

> The `machine learning model` is build using `Numpy`, `Pandas`, `Matplotlib`, `Sciki-learn` and `Jupyter Notebook`

  

> The source code is available [here](https://github.com/AkashSDas/Ham-or-Spam).

  

## Installation

  

  

It is highly **recommended** to use **`virtual environment`** for this project to avoid any issues related to dependencies.

  

  

Here **`pipenv`** is used for this project.

  

  

There is a **`requirements.txt`** file in `'HamSpam'/requirements.txt` which has all the dependencies for this project.

  

  

- First, start by closing the repository

  

  

```bash
git clone https://github.com/AkashSDas/HamSpam
```

  

  

- Start by installing **`pipenv`** if you don't have it

  

```bash
pip install pipenv
```

  

  

- Once installed, access the venv folder inside the project folder

  

```bash
cd  'HamSpam'/venv/
```

  

  

- Create the virtual environment

  

```bash
pipenv install
```

  

The **Pipfile** of the project must be for creating replicating project's virtual environment.

  

  

This will install all the dependencies and create a **Pipfile.lock** (this should not be altered).

  

  

- Enable the virtual environment

  

```bash
pipenv shell
```


- To start the server go the `HamSpam/venv/src` and run `python manage.py runserver`
```bash
cd src/
python manage.py runserver
```

- After doing that you will see
```bash
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
Copy paste `http://127.0.0.1:8000/` url and press `Enter`.
  



  

## License

  

  

This project is licensed under the MIT License - see the [MIT LICENSE](LICENSE) file for details.
