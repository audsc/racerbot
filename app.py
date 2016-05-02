import os
from bottle import Bottle, run, template, get, post, request, redirect
import sentence_logic

# keep phrases in sql database
# load from sql database when page is loaded
# enter new selections that get entered into the database

def format_str(s):
    return s.replace(' ', '_').lower()

@get('/')
def menu():
    return template('menu', title='Menu of Events')

@get('/Longest_Run')
def foo():
    phrases = sentence_logic.test() 
    p_dict = sentence_logic.get_p_dict()
    return template('longest_run', title='bot for longest run', phrases=phrases, commands=p_dict['commands'], actions=p_dict['actions'], address=p_dict['address'])

@post('/Longest_Run')
def submit():
    command_str = request.forms.get('COMMAND_LIST')
    COMMANDS = command_str.replace('\r','').split('\n')
    for phrase in COMMANDS:
        sentence_logic.add_phrase('commands.txt', phrase)
    action_str = request.forms.get('ACTION_LIST')
    ACTIONS = action_str.replace('\r','').split('\n')
    for phrase in ACTIONS:
        sentence_logic.add_phrase('actions.txt', phrase)
    address_str = request.forms.get('ADDRESS_LIST')
    ADDRESSS = address_str.replace('\r','').split('\n')
    for phrase in ADDRESSS:
        sentence_logic.add_phrase('address.txt', phrase)
    phrases = sentence_logic.test()
    p_dict = sentence_logic.get_p_dict()
    return template('longest_run', title='bot for longest run', phrases=phrases, commands=p_dict['commands'], actions=p_dict['actions'], address=p_dict['address'])

@get('/<name>/')
@get('/<name>')
def dynmaic(name):
    return '<center><h1> Hello '+name+'</h1></center>'

@get('/<num_float:float>') #return data for float
@get('/<num_float:float>/')
def dynamic_float(num_float):
    return 'The floating point you have entered is: '+str(num_float)

if __name__ == '__main__':
    #port = int(argv[1])
    port = int(os.environ.get('PORT', 8080))
    run(host='0.0.0.0', port=port, debug=True)
