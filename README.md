# Working with RESTFul APIs in Python

[Slides](https://littlepea.github.io/python-rest-api-talk/) and code for the "Working with RESTFul APIs in Python" talk 
at the [Beijing Python Meetup](https://www.meetup.com/Beijing-Python/events/pmtxglyxcblb/).

## Talk Description

* Title: Working with RESTFul APIs in Python
* Duration: 1 hour
* Level: Intermediate
* Presenter: [Evgeny Demchenko](https://twitter.com/littlepea12)

## Summary

As modern developers we have to interact with external services with APIs as well as create our own APIs to provide integration points to other developers.

In this talk well discuss what are the most productive ways to do both of these things.
 
This is an Intermediate level talk but both beginners and advanced developers will find something new or useful here too.


---

### References:

* [Presentation Slides](https://littlepea.github.io/python-rest-api-talk/)

---

## Running the example code

### Set up the environment

```
virtualenv env
. env/bin/activate
pip install -r requirements.txt
```

### Run the API

```
hug -f jobs/api.py
```

### Run the Jupyter notebook

```
jupyter notebook
```

### Create the slides

```
jupyter-nbconvert --to slides talk.ipynb --post serve
```
