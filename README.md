# [**Technical Problems**](https://github.com/MoazSamy/Backend-Task/tree/main/Technical%20problems)

## [**Absolute difference**](https://github.com/MoazSamy/Backend-Task/blob/main/Technical%20problems/absolute_difference.py)

### Traditional approach:
The traditional approach to such a problem is standing with a point in the first element in the array, then looping on the rest of the array, abs subtracting the rest of the array from that element, then constantly comparing the new minimum value to the old one and setting/ignoring it accordingly.
Although this approach might be the easiest one to come to mind, it has a time complexity of O(n<sup>2</sup>).

### Used approach:
The approach I decided to use is, since we are looking for the minimum abs value, this means that it has to be the nearest two numbers to each other that will bring up that value.
This means we need to sort the array first, using TimSort which is better than MergeSort in the worst case scenario, and equally as efficient in the best case scenario, achieving time complexity of O(nLog(n)).
Then we abs subtract each two subsequent elements in the array, comparing the old minimum value to the new one.


## [**Substring problem**](https://github.com/MoazSamy/Backend-Task/blob/main/Technical%20problems/substring_WL.py)

### Used approach:
The approach I used is that I converted the strings into a list of chars, then used the first element to constantly look up if it will match with one of the other chars in the other string. If that element doesn't match, it gets pop'd (which is why I used this method because it achieves time complexity of O(n) instead of the O(n<sup>2</sup>) of the traditional approach), then it goes again till it finished iterating on the second string, returning True (YES) or False (NO).

### Another approach:
This appraoch includes using hashtables to constantly lookup the first string chars in the second string chars that are assigned in the hashtable, reaching roughly O(1) in best case scenario, and O(n) in the worst case scenario.



# [**Technical Project : API TASK**](https://github.com/MoazSamy/Backend-Task/tree/main/Technical%20project/task_state_api)
This is a RESTful API that allows users to do CRUD operations on tasks in a list. It also allows them to change the tasks' status moving forwardly, but not backwardly, this enables users to archive the task and/or make it move only one step in progress. This is based on a predefined state machine.

Code style follows [**PEP8 style guidelines**](https://www.python.org/dev/peps/pep-0008/).

## Getting started
### Requirements and pre-requisites
To effectively initialize this project, user needs to have python(3.7+) on their machines and pipenv using `pip install --user pipenv`.
From inside the project folder *../task_state_api/*, run `pipenv sync` to sync and install the pre-requisites like django and djangorestframework.
Then run `pipenv shell` to actively start the virtual environment to start putting in the required commands to run the API.

To start the API , start by entering
```
python manage.py runserver
```
This starts the API on `127.0.0.1:8000/`, but this blank has no reference or usage to the API.
So we start on `127.0.0.1:8000/api/v1`.

This starts us on the "Task List" page, which displays the tasks list in Bootswatch theme.


### Tests
The tests are written using the [**unittest**](https://docs.python.org/2/library/unittest.html) package from Python's standard library. 
The tests are run by using `python manage.py test`.
There are provided 7 tests provided in the [**tests.py**](https://github.com/MoazSamy/Backend-Task/blob/main/Technical%20project/task_state_api/tasks/tests.py).
Each state has at least 1 test for its case.

### Project Structure
    └───task_state_api
    │   db.sqlite3
    │   manage.py
    │   Pipfile
    │   Pipfile.lock
    │
    ├───config
    │       asgi.py
    │       settings.py
    │       urls.py
    │       wsgi.py
    │       __init__.py
    │
    └───tasks
        │   admin.py
        │   apps.py
        │   models.py
        │   serializers.py
        │   tests.py
        │   urls.py
        │   views.py
        │   __init__.py
        │
        └───migrations
                0001_initial.py
                0002_auto_20211214_1656.py
                0003_auto_20211214_1756.py
                __init__.py
This structure has 2 main folders:
* config, which stores the [**settings**](https://github.com/MoazSamy/Backend-Task/blob/main/Technical%20project/task_state_api/config/settings.py) of the django and the admin [**urls**](https://github.com/MoazSamy/Backend-Task/blob/main/Technical%20project/task_state_api/config/urls.py).
* tasks, which stores the most important aspects of the api like [**models**](https://github.com/MoazSamy/Backend-Task/blob/main/Technical%20project/task_state_api/tasks/models.py), [**views**](https://github.com/MoazSamy/Backend-Task/blob/main/Technical%20project/task_state_api/tasks/views.py), [**urls**](https://github.com/MoazSamy/Backend-Task/blob/main/Technical%20project/task_state_api/tasks/urls.py), and more..


## API Reference
### Endpoints
#### GET /api/v1/
* Returns a list of tasks.
* Sample: `curl http://127.0.0.1:8000/api/v1/`
```
      [{
        "id":1,
        "state":"ARCH",
        "title":"Work"
       },
       {
        "id":2,
        "state":"ARCH",
        "title":"School"
       },
       {
        "id":3,
        "state":"DRFT",
        "title":"Chores"
       },
       {
        "id":4,
        "state":"ARCH",
        "title":"Chores"
      }]
```

#### GET /api/v1/<task_id>
* Returns a single task by id.
* Returns a 404:NOT_FOUND if the id doesn't exist.
* Sample: `curl http://127.0.0.1:5000/api/v1/1/`
```
      {
      "id":1,
      "state":"ARCH",
      "title":"Work"
      }
```

#### DELETE /api/v1/<task_id>
* Deletes an existing task using its id.

#### GET /api/v1/<task_id>/advance
* Advances the task to the next stage of progress, using its id.
* This returns a 400:BAD_REQUEST if the task is already archived and can't progress any further.
```
      {
      "id":3,
      "state":"DN",
      "title":"Chores"
      }
```

### GET /api/tasks/<task_id>/archive
* Advances the task to the archived state, using its id.
* This returns a 400:BAD_REQUEST if the task is already archived.
```
      {
      "id":3,
      "state":"ARCH",
      "title":"Chores"
      }
```

### Error handling
The API returns a couple of error messages for invalid action, or for inexistent task:
* `400`: Bad Request
* `404`: Not Found

## Authors
Moaz Samy
