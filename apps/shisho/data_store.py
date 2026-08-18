import json
from pathlib import Path
import sqlite3


def read_translations():
    conn, cursor = create_db()

    cursor.execute("SELECT * FROM expressions")
    expressions = cursor.fetchall()

    cursor.execute("SELECT * FROM readings")
    readings = cursor.fetchall()

    cursor.execute("SELECT * FROM definitions")
    definitions = cursor.fetchall()

    cursor.execute("SELECT * FROM examples")
    examples = cursor.fetchall()

    conn.close()

    return expressions, readings, definitions, examples


def read_ignore_list():
    conn, cursor = create_ignore_db()

    cursor.execute("SELECT * FROM ignore_words")
    words = cursor.fetchall()
    conn.close()

    return words


def load_jmdict():
    conn, cursor = create_db()
    create_words_table(conn, cursor)
    data = read_words_file()
    save_words(conn, cursor, data)


# JMDict parser
def read_words_file():
    jp_en = {}
    for file in Path('jmdict').glob('term_bank_*.json'):
        with open(file, encoding='utf-8') as f:
            entries = json.load(f)

        for entry in entries:
            expression = entry[0]
            reading = entry[1]
            content = entry[5]

            defs, examples = parse_jm_content(content)

            jp_en.setdefault(expression, []).append({
                'reading': reading,
                'definitions': defs,
                'examples': examples
            })

    return jp_en


def parse_jm_content(content):
    defs, examples = [], []
    wrapper = content[0]
    if type(wrapper) != dict or wrapper.get('type') != 'structured-content':
        return defs, examples

    sections = wrapper.get('content')
    if not sections:
        return defs, examples

    if type(sections) == dict:
        sections = [sections]

    for sec in sections:
        parsed = parse_content_section(sec)
        if not parsed:
            continue

        match parsed[0]:
            case 'glossary':
                defs += parsed[1]
            case 'examples':
                examples += parsed[1]
            case _:
                continue

    return defs, examples


def parse_content_section(sec):
    t_wrapper = sec.get('data')
    if not t_wrapper:
        return None

    t_value = t_wrapper.get('content')
    if not t_value:
        return None

    sec_content = sec.get('content')
    if not sec_content:
        return None

    entries = []
    try:
        for entry in sec_content:
            entries.append(entry.get('content'))
    except:
        return None
    return t_value, entries


# DB Setup
chunk_size = 10_000


def save_words(conn, cursor, data):
    expressions = list(data.keys())
    ids = batch_save(conn, cursor, expressions, 'expressions', ['expr'])
    i_readings, i_defs, i_examples = [], [], []
    for i, (_, content) in enumerate(data.items()):
        id = ids[i]
        for entry in content:
            i_readings.append((id, entry.get('reading')))
            for d in entry.get('definitions'):
                i_defs.append((i, d))
            for e in entry.get('examples'):
                i_examples.append((i, e))
    cursor.executemany(
        "INSERT INTO readings (expression_id, reading) VALUES (?, ?)", i_readings)
    cursor.executemany(
        "INSERT INTO definitions (expression_id, definition) VALUES (?, ?)", i_defs)
    cursor.executemany(
        "INSERT INTO examples (expression_id, example) VALUES (?, ?)", i_examples)
    conn.commit()


def batch_save(conn, cursor, data, table, fields):
    cursor.execute("BEGIN TRANSACTION;")
    ids = []

    cs = chunk_size // len(fields)
    placeholder = "(" + ", ".join(['?'] * len(fields)) + ")"
    fields_str = "(" + ", ".join(fields) + ")"
    try:
        for i in range(0, len(data), cs):
            chunk = data[i: i + cs]
            placeholders = ", ".join([placeholder] * len(chunk))
            query = f"INSERT INTO {table} {fields_str} VALUES {placeholders} RETURNING id;"
            cursor.execute(query, chunk)
            chunk_ids = [row[0] for row in cursor.fetchall()]
            ids.extend(chunk_ids)
    except sqlite3.Error as e:
        conn.rollback()
        raise e
    return ids


def save_expression(conn, cursor, expression):
    cursor.execute("""
        INSERT INTO expressions (expr)
        VALUES (?)
    """, (expression, ))
    conn.commit()
    return cursor.lastrowid


def save_reading(conn, cursor, reading, expr_id):
    cursor.execute("""
        INSERT INTO readings (reading, expression_id)
        VALUES (?, ?)
    """, (reading, expr_id))
    conn.commit()


def save_definition(conn, cursor, definition, expr_id):
    cursor.execute("""
        INSERT INTO definitions (definition, expression_id)
        VALUES (?, ?)
    """, (definition, expr_id))
    conn.commit()


def save_example(conn, cursor, example, expr_id):
    cursor.execute("""
        INSERT INTO examples (example, expression_id)
        VALUES (?, ?)
    """, (example, expr_id))
    conn.commit()


def create_db():
    conn = sqlite3.connect("shisho.db")
    cursor = conn.cursor()

    cursor.execute("PRAGMA foreign_keys = ON;")
    conn.commit()

    return conn, cursor


def create_words_table(conn, cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expressions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            expr TEXT NOT NULL UNIQUE
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS readings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            reading TEXT NOT NULL,
            expression_id INTEGER NOT NULL,
            FOREIGN KEY (expression_id) REFERENCES expressions(id)
                ON DELETE CASCADE
                ON UPDATE CASCADE
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS definitions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            definition TEXT NOT NULL,
            expression_id INTEGER NOT NULL,
            FOREIGN KEY (expression_id) REFERENCES expressions(id)
                ON DELETE CASCADE
                ON UPDATE CASCADE
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS examples (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            example TEXT NOT NULL,
            expression_id INTEGER NOT NULL,
            FOREIGN KEY (expression_id) REFERENCES expressions(id)
                ON DELETE CASCADE
                ON UPDATE CASCADE
        )
    """)
    conn.commit()


# Ignore list DB
def create_ignore_db():
    conn = sqlite3.connect("ignore_list.db")
    cursor = conn.cursor()
    conn.commit()

    return conn, cursor


def create_ignore_table(conn, cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ignore_words (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word TEXT NOT NULL UNIQUE
        )
    """)
    conn.commit()


def save_ignore_words(words):
    conn, cursor = create_ignore_db()
    _save_ignore_words(conn, cursor, words)


def _save_ignore_words(conn, cursor, words):
    for w in words:
        _save_ignore_word(conn, cursor, w)


def _save_ignore_word(conn, cursor, word):
    try:
        cursor.execute("INSERT INTO ignore_words (word) VALUES (?)", (word,))
        conn.commit()
    except sqlite3.IntegrityError as e:
        print(f'Failed to save the word: {word}')
        print('SQL Error:', e.sqlite_errorname)
