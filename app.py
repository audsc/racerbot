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
    COMMAND1 = request.forms.get('COMMAND1')
    COMMAND2 = request.forms.get('COMMAND2')
    COMMAND3 = request.forms.get('COMMAND3')
    COMMAND4 = request.forms.get('COMMAND4')
    COMMANDS = filter(lambda name: name!= '' , [COMMAND1, COMMAND2, COMMAND3, COMMAND4])
    print COMMANDS
    for phrase in COMMANDS:
        sentence_logic.add_phrase('commands.txt', phrase)
    ACTION1 = request.forms.get('ACTION1')
    ACTION2 = request.forms.get('ACTION2')
    ACTION3 = request.forms.get('ACTION3')
    ACTION4 = request.forms.get('ACTION4')
    ACTIONS = filter(lambda name: name!= '' , [ACTION1, ACTION2, ACTION3, ACTION4])
    print ACTIONS
    for phrase in ACTIONS:
        sentence_logic.add_phrase('actions.txt', phrase)
    phrases = sentence_logic.test()
    ADDRESS1 = request.forms.get('ADDRESS1')
    ADDRESS2 = request.forms.get('ADDRESS2')
    ADDRESS3 = request.forms.get('ADDRESS3')
    ADDRESS4 = request.forms.get('ADDRESS4')
    ADDRESSS = filter(lambda name: name!= '' , [ADDRESS1, ADDRESS2, ADDRESS3, ADDRESS4])
    print ADDRESSS
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
    port = int(os.environ.get('PORT', 8080))
    run(host='0.0.0.0', port=port, debug=True)
