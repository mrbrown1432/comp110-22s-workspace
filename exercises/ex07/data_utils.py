"""EX07 Data Wrangling."""

__author__ = "730481331"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
   
    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")
    
    # Prepare to read the date file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(data_cols_head: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first N rows of data for each column."""
    result: dict[str, list[str]] = {}
    if n > len(data_cols_head):
        n = len(data_cols_head)
    for column in data_cols_head:
        co: list[str] = []
        for x in range(0, n):
            co.append(data_cols_head[column][x])
            x += 1
        result[column] = co
    return result


def select(data_cols_head: dict[str, list[str]], ncolumn: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for column in ncolumn:
        result[column] = data_cols_head[column]
    return result


def concat(data_cols_head: dict[str, list[str]], table: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new-column based table with two column-based tables combined1."""
    result: dict[str, list[str]] = {}
    for column in data_cols_head:
        result[column] = data_cols_head[column]
    for x in table:
        if x in result:
            for y in table[x]:
                result[x].append(y)
        else: 
            result[x] = table[x]
    return result


def count(alist: list[str]) -> dict[str, int]:
    """Produce a dictionary that returns the amount of times an event appears."""
    result: dict[str, int] = {}
    for x in alist:
        if x in result:
            result[x] += 1
        else:
            result[x] = 1
    return result