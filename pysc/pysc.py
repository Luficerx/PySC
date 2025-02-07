import re

from typing import Any
from .pattern import *
from .log import *

class PySCScope():
    def __init__(self, *args, **kwargs):
        self.args = []

    def append(self, key: str, value: Any):
        getattr(self, key).append(value)

    def add(self, key: str, value: Any):
        getattr(self, key).add(value)

    def extend(self, key: str, value: Any):
        getattr(self, key).extend(value)
    
    def key(self, key: str) -> bool:
        return hasattr(self, key)

scope = PySCScope()

def PySCSplit(pattern: str, line: str, repl: tuple[str, str] | None = None) -> list[Any]:
    if repl:
        pattern = pattern.replace(*repl)
        
    return re.split(pattern, line)

def PySCHandleFileFormat(file_name: str) -> str:
    if file_name.endswith(".json"):
        msg = "Bruh, Why the fuck you're trying to parse a json file?"
        raise PySCFileException(msg)
    
    if not file_name.endswith(".pysc"):
        msg = "Invalid file format: {}".format(file_name)
        raise PySCFileException(msg)

    return file_name

def PySCParseBlocks(items: list[str]) -> Any:
    pass

def PySCOpen(file_name: str) -> list[Any]:
    LOG("PARSING", file_name)

    file_name = PySCHandleFileFormat(file_name)
    blocks = []
    block = []
    pos = 0
    skip = False

    with open(file_name, "r") as fl:
        for i, line in enumerate([line.strip() for line in fl.readlines() if line.strip()]):
            pos += PySCGetPos(line)

            # FIXME: PySCStripComment matches closing embbed comments.
            # ignores <# but matches #> 
            # It's underfined behavior, quick fix is parse embbed comments before simple comments

            if skip:
                if PySCComment(PySCCloseComment, line):
                    skip = False
                continue

            if PySCComment(PySCOpenComment, line):
                skip = True
                continue

            line = PySCStripEmbbedComment(line)

            if not skip:
                line = PySCStripComment(line)

            # Skips lines that are emtpy
            if not line.strip():
                continue

            if PySCComment(PySCSimpleComment, line):
                continue
            
            block.append(line)

            if pos == 0 and block:
                result = "".join(block)
                blocks.append(result)
                block = []
    
    with open("output.txt", "w") as fl:
        for item in blocks:
            fl.write(f"{item}\n")

def PySCGetPos(line: str) -> int:
    return sum([line.count(x) for x in PySCOpenDelims]) - sum([line.count(y) for y in PySCCloseDelims])

def PySCComment(pattern: str, line: str) -> bool:
    return re.match(pattern, line) is not None

def PySCStripComment(line) -> str:
    return re.sub(PySCSimpleComment, "", line)

def PySCStripEmbbedComment(line: str) -> str:
    return re.sub(PySCEmbbedComment, " ", line)