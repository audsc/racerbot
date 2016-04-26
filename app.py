from bottle import run, template, get, post, request, redirect


# keep phrases in sql database
# load from sql database when page is loaded
# enter new selections that get entered into the database

@get('/')
def menu():
    return template('menu', title='Menu of Events')


