import os
from typing import overload, Any
from .log import LOG, PySCLogs

PySCOutput = "-o : Output File\nex: my_output.pysc | my_output.txt | my_output.py"
PySCInput = "-i : Input File\nex: my_input.pysc"
PySCTest = f"-t : Test\nargs: all | stress"

PySCHelp = f"-h : Help\nDisplay this information table.\n\n{PySCInput}\n\n{PySCOutput}\n\n{PySCTest}"

PySCFlags = ("-i", "-o", "-t")
PySCHelpCmds = {
    "-i -h": PySCInput,
    "-o -h": PySCOutput,
    "-t -h": PySCTest,
    }

PySCTestFileError = -2

PySCCMDError = -1
PySCCMDEmtpy = 0
PySCCMDInfo = 1

PySCErrorInfo = ""

PySCErrorMessages = {
    PySCCMDEmtpy: "[ERROR] No flags provided\n[HINT] consider using -h to check available flags.",
    PySCTestFileError: "Could not find test file:",
    PySCCMDError: "[ERROR]",
    }

@overload
def PySCCMDResult(args: list[str]) -> tuple[str | bool, str | bool] | int: ...

def PySCCMDResult(args: list):
    global PySCErrorInfo

    file_name = args.pop(0)
    input = False
    output = False
    
    if not args:
        return PySCCMDEmtpy
    
    while args:
        if args[0] == "-h":
            print(PySCHelp)
            break
        
        arg = args.pop(0)

        if arg == "-h":
            continue

        if arg in PySCFlags:
            try:
                argc = args.pop(0)

            except:
                if arg == "-o":
                    return (input, "output.txt")

                PySCErrorInfo = f"No argument provided to flag {arg}.\n[HINT] Consider using '{arg} -h' for help."
                return PySCCMDError
            
            if (cmd := PySCHelpCmds.get(f"{arg} {argc}", False)):
                PySCLogs(cmd)
                return PySCCMDInfo
            
            if arg == "-i":
                input = argc

            if arg == "-o":
                output = argc

            if arg == "-t":
                if argc.endswith(".pysc"):
                    input = argc

                else:
                    input = os.path.join("tests", f"{argc}.pysc")

                if not os.path.exists(input):
                    PySCErrorInfo = f"{input}."
                    return PySCTestFileError
                
                LOG("TESTING", input)
            
        else:
            PySCErrorInfo = f"Unrecognized flag '{arg}', use -h for help."
            return PySCCMDError
        
    return (input, output)

@overload
def PySCCMDFailure(result: tuple[Any, Any] | int) -> bool: ...

def PySCCMDFailure(result: int) -> bool:
    if result == PySCCMDInfo:
        return True
    
    if result in PySCErrorMessages:
        PySCLogs(PySCErrorMessages.get(result), PySCErrorInfo)
        return True
    
    return False