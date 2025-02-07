def LOG(type: str, message: str):
    print(f"[{type}]:", message)

class PySCFileException(Exception):
    pass

class PySCCommentException(Exception):
    pass