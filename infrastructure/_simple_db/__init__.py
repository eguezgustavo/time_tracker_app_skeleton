import sqlite3



def init(connection_string):
    db = sqlite3.connect(connection_string)
    cursor = db.cursor()
    
    with open('./infrastructure/_simple_db/fake_data.sql', 'r') as create_script_file:
        create_script = create_script_file.read()
    
    cursor.executescript(create_script)
