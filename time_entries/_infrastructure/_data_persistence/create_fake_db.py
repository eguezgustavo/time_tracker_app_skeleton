import sqlite3

DB_FILE_NAME = 'fake.db'


if __name__ == '__main__':
    db = sqlite3.connect(DB_FILE_NAME)
    cursor = db.cursor()
    
    with open('./time_entries/_infrastructure/_data_persistence/fake_data.sql', 'r') as create_script_file:
        create_script = create_script_file.read()
    
    cursor.executescript(create_script)
