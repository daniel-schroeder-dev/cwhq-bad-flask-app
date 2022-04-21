from .connect import get_db
from pathlib import Path


def create_db():
    con = get_db()
    cur = con.cursor()
    query = """
        DROP TABLE IF EXISTS uh_oh;
    """
    cur.execute(query)
    query = """
        CREATE TABLE uh_oh (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT
        );
    """
    cur.execute(query)
    query = """
        INSERT INTO uh_oh (data) VALUES ("break the GIT!!!");
    """
    cur.execute(query)
    con.commit()


def delete_db():
    Path("approot/uh-oh-database.sqlite").unlink(missing_ok=True)
