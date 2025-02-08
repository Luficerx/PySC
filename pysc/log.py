def PySCLogs(*items: tuple[str], start: str = ''):
    """
    Improved version of LOG.
    
    items: list of strings to be printed.

    start: string to be added to the start of the line."""

    if start:
        print(start, *items)

    print(*items)

def PySCWarns(message: str, file: str, line: int):
    print(f"[WARNING] {file}, line {line}", message)

class PySCFileException(Exception):
    pass

class PySCCommentException(Exception):
    pass