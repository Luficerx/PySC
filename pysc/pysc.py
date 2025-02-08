from pathlib import Path
from typing import Any
from .pattern import *
from .log import *
import re

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

def PySCHandleInputFile(file_name: str) -> str:
    if file_name.endswith(".json"):
        msg = "Bruh, Why the fuck you're trying to parse a json file?"
        raise PySCFileException(msg)
    
    if not file_name.endswith(".pysc"):
        msg = "Invalid file format: {}".format(file_name)
        raise PySCFileException(msg)

    if not Path(file_name).exists():
        file_path = Path.cwd() / file_name
        msg = "Could not find file: {}".format(file_path)
        raise PySCFileException(msg)

    return file_name

def PySCParseBlocks(file_name: str) -> Any:
    skip = False
    blocks = []
    block = []
    pos = 0
    
    with open(file_name, "r") as fl:
        lines = [(x, y) for (x, y) in enumerate(fl.readlines(), start=1) if y.strip()]

        for i, line in lines:
            pos += PySCGetPos(line)

            if PySCComment(PySCSimpleComment, line):
                continue

            line = PySCStripComment(line)
            line = PySCStripEmbbedComment(line)

            if PySCComment(PySCOpenComment, line):
                skip = True
                continue

            if skip:
                if PySCComment(PySCCloseComment, line):
                    skip = False

                if PySCComment(PySCOpenComment, line):
                    PySCWarns(f"'<#' Found in line {i} while inside a comment section, Did you forget to close the previous comment block?", file_name, i)

                continue

            block.append(line)

            if pos == 0 and block:
                naked = "".join(block)
                blocks.append(naked)
                block = []

        if skip:
            raise PySCCommentException("Reached EOF and '#>' could not be found.")
    
    return blocks

def PySCOpen(file_name: str) -> list[Any]:
    PySCLogs("[PARSING]", file_name)
    PySCHandleInputFile(file_name)
    blocks = PySCParseBlocks(file_name)
    return blocks

def PySCGetPos(line: str) -> int:
    return sum([line.count(x) for x in PySCOpenDelims]) - sum([line.count(y) for y in PySCCloseDelims])

def PySCComment(pattern: str, line: str) -> bool:
    return re.match(pattern, line) is not None

def PySCStripComment(line) -> str:
    return re.sub(PySCSimpleComment, "", line)

def PySCStripEmbbedComment(line: str) -> str:
    return re.sub(PySCEmbbedComment, " ", line)