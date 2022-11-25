CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT
);

CREATE TABLE citations (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    deleted INTEGER
);

CREATE TABLE entry_type (
    id INTEGER PRIMARY KEY,
    citation_id INTEGER,
    tag TEXT,
    name TEXT,
    deleted INTEGER
);

CREATE TABLE field_type (
    id INTEGER PRIMARY KEY,
    citation_id INTEGER,
    tag TEXT,
    name TEXT,
    deleted INTEGER
);


