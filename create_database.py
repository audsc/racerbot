import sqlite3

con = sqlite3.connect('sentences.db')
con.execute("CREATE TABLE sentences (phrase char(200) NOT NULL, status char(100) NOT NULL)")
con.execute("INSERT INTO sentences (phrase, status) VALUES ('Dear sir ', 'address')")
con.execute("INSERT INTO sentences (phrase, status) VALUES ('I command that you', 'command')")
con.execute("INSERT INTO sentences (phrase, status) VALUES ('replenish your electrolytes ', 'action')")
con.commit()
