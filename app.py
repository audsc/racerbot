import os
from bottle import Bottle, run, template, get, post, request, redirect
import db_sentence_logic as sentence_logic

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
    for key, value in p_dict.items():
        p_dict[key] = ', '.join(p_dict[key])
    return template('longest_run', title='bot for longest run', phrases=phrases, commands=p_dict['commands'], actions=p_dict['actions'], address=p_dict['address'])

@post('/Longest_Run')
def submit():
    command_str = request.forms.get('COMMAND_LIST')
    print command_str
    COMMANDS = command_str.replace('\r','').split('\n')
    for phrase in COMMANDS:
        print phrase
        sentence_logic.add_phrase('command', phrase)
    action_str = request.forms.get('ACTION_LIST')
    ACTIONS = action_str.replace('\r','').split('\n')
    for phrase in ACTIONS:
        print phrase
        sentence_logic.add_phrase('action', phrase)
    address_str = request.forms.get('ADDRESS_LIST')
    ADDRESSS = address_str.replace('\r','').split('\n')
    for phrase in ADDRESSS:
        print phrase
        sentence_logic.add_phrase('address', phrase)
    phrases = sentence_logic.test()
    p_dict = sentence_logic.get_p_dict()
    for key, value in p_dict.items():
        p_dict[key] = ', '.join(p_dict[key])
    return template('longest_run', title='bot for longest run', phrases=phrases, commands=p_dict['commands'], actions=p_dict['actions'], address=p_dict['address'])

@get('/Longest_Run/clear/<name>')
def clear(name):
    print "Clear : " , name
    ret = sentence_logic.clear_phrases(name)
    if ret == 0:
        redirect('/Longest_Run')
    else:
        return '<center><h1> Something went wrong clearing '+name+'</h1></center>'


@get('/<name>/')
@get('/<name>')
def dynmaic(name):
    return '<center><h1> The page for '+name+' does not exist yet. </h1></center>'

if __name__ == '__main__':
    #port = int(argv[1])
    port = int(os.environ.get('PORT', 8080))
    run(host='0.0.0.0', port=port, debug=True)
