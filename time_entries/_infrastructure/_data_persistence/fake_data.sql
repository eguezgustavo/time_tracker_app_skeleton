BEGIN;
CREATE TABLE time_entries (
    id INTEGER PRIMARY KEY,
    google_user_id TEXT,
    start_time TEXT,
    end_time TEXT,
    customer_id INTEGER,
    project_id INTEGER,
    activity_id INTEGER,
    technologies TEXT,
    ticket TEXT,
    description TEXT
);
CREATE INDEX time_entries_idx ON time_entries (id);

INSERT INTO time_entries (google_user_id, start_time, end_time, customer_id, project_id, activity_id, technologies, ticket, description)
VALUES
    ('x4UsIrlvwdd3DmRxF8tQ3ZWbdSm2', '13/10/2021 08:00', '13/10/2021 09:00', 1, 1, 1, 'python,flask,tdd', 'http://some-ticket', 'starting on some ticket'),
    ('x4UsIrlvwdd3DmRxF8tQ3ZWbdSm2', '13/10/2021 10:00', '13/10/2021 10:30', 1, 1, 1, 'python,flask,tdd', 'http://some-ticket', 'mid on some ticket'),
    ('x4UsIrlvwdd3DmRxF8tQ3ZWbdSm2', '13/10/2021 11:00', '13/10/2021 12:00', 1, 1, 1, 'python,flask,tdd', 'http://some-ticket', 'finish some ticket');

COMMIT;
