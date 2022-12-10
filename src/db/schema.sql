CREATE TABLE citations (
    id INTEGER PRIMARY KEY,
    deleted INTEGER
);

CREATE TABLE entry_types (
    id INTEGER PRIMARY KEY,
    citation_id INTEGER,
    type TEXT,
    cite_as TEXT
);

CREATE TABLE fields(
    id INTEGER PRIMARY KEY,
    citation_id INTEGER,
    type TEXT,
    value TEXT
);
