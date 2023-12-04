import sqlite3
import os
from contextlib import closing
from loguru import logger


def main():
    # find out the path where this script runs
    dir_path = os.path.dirname(os.path.realpath(__file__))
    logger.debug(f'the dir_path variable produces the value {dir_path}')
    # append the path to the database name
    db_path = f"{dir_path}/aquarium.db"
    logger.debug(f'The full database path is {db_path}')
    connection = sqlite3.connect(db_path)

    logger.info(f'Amount of changes: {connection.total_changes}')

    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS fish (name TEXT, species TEXT, tank_number INTEGER)")
    cursor.execute("INSERT INTO fish VALUES ('Sammy', 'shark', 1)")
    cursor.execute("INSERT INTO fish VALUES ('Jamie', 'cuttlefish', 7)")

    rows = cursor.execute("SELECT name, species, tank_number FROM fish").fetchall()
    logger.success(f'These rows have been found:\n{rows}')

    target_fish_name = "Jamie"
    rows = cursor.execute(
        "SELECT name, species, tank_number FROM fish WHERE name = ?",
        (target_fish_name,),
    ).fetchall()
    logger.success(f'These rows have been found:\n{rows}')

    new_tank_number = 2
    moved_fish_name = "Sammy"
    cursor.execute(
        "UPDATE fish SET tank_number = ? WHERE name = ?",
        (new_tank_number, moved_fish_name)
    )

    with closing(sqlite3.connect(db_path)) as connection:
        with closing(connection.cursor()) as cursor:
            rows = cursor.execute("SELECT 1").fetchall()
            logger.debug(f'These rows have been found:\n{rows}')


if __name__ == "__main__":
    main()
