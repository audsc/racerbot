import sqlite3

def read_phrases(phrase_type):
    conn = sqlite3.connect('sentences.db')
    c = conn.cursor()
    c.execute("SELECT phrase FROM sentences WHERE status LIKE ?", (phrase_type,))
    result = c.fetchall()
    p_list = list(item[0] for item in result)
    return p_list

def add_phrase(phrase_type, p):
    if p:
        con = sqlite3.connect('sentences.db')
        con.execute("INSERT INTO sentences (phrase, status) VALUES (?, ?)", (p, phrase_type))
        con.commit()
    

def get_p_dict():
    p_dict = {}
    p_dict['commands'] = read_phrases('command')
    p_dict['actions'] = read_phrases('action')
    p_dict['address'] = read_phrases('address')
    return p_dict

def create_sentences(p_dict):
    phrases = []
    while(len(p_dict['commands'])>0):
        command = (p_dict['commands']).pop()
        for i in range(len(p_dict['actions'])):
            phrase_start = command + ' ' +  p_dict['actions'][i]
            for j in range(len(p_dict['address'])):
                phrase = phrase_start + ' ' +  p_dict['address'][j]
                phrases.append(phrase)
    print "SENTENCES : ",  phrases
    return phrases


def clear_phrases(p_type):
    con = sqlite3.connect('sentences.db')
    con.execute("DELETE FROM sentences WHERE status=?", (p_type,))
    con.commit()
    return 0

def test():
    p_dict = get_p_dict()
    for key, value in p_dict.items():
        print key, " : ", value
    sentences = create_sentences(p_dict)
    return sentences

#test()


### FOR TESTING ADD PHRASES :
###
### add_phrase("command", "Immediately")
### 
### FOR TESTING READ PHRASES :
###
### res = read_phrases("command")
### for item in res:
###     print str(item[0])
### 
### TEST FOR CLEAR PHRASES :
### 
### clear_phrases("action")
### res = read_phrases("action")
### print res
