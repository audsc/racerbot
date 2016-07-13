import sqlite3
#from bottle import route, run

#@route('/test_database')
def test_database():
    conn = sqlite3.connect('sentences.db')
    c = conn.cursor()
    c.execute("SELECT phrase FROM sentences WHERE status LIKE 'action'")
    c.execute("SELECT phrase FROM sentences WHERE status LIKE 'command'")
    result = c.fetchall()
    print str(result)

test_database()
