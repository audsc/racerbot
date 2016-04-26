import sys

def read_phrases(p_file):
    p_list = []
    f = open(p_file, 'r')
    for line in f:
        p_list.append(line.strip('\n'))
    f.close()
    return p_list

def add_phrase(p_file, phrase):
    f = open(p_file,'a')
    f.write(phrase)
    f.write('\n')
    f.close()

def get_p_dict():
    p_dict = {}
    p_dict['commands'] = read_phrases('./commands.txt')
    p_dict['actions'] = read_phrases('./actions.txt')
    p_dict['address'] = read_phrases('./address.txt')
    return p_dict

if __name__ == "__main__":
    while(True):
        if int(raw_input("Would you like to continue (press 1 for continue)"))!=1:
            break
        var = int(raw_input("Would you like to add (1) a command, (2) an action, or (3) an address?"))
        if var == 1:
            p_file = "commands.txt"
        if var == 2:
            p_file = "actions.txt"
        if var == 3:
            p_file = "address.txt"
        phrase = raw_input("What would you like to add?")
        add_phrase(p_file, phrase)
    p_dict = get_p_dict()
    for key, value in p_dict.items():
        print key , " : " , value

