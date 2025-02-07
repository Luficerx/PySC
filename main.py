import sys

from pysc.pysc import PySCOpen
from pysc.log import LOG
import pysc.util as util

def main():
    result = util.PySCCMDResult(sys.argv[:])
    
    if util.PySCCMDFailure(result):
        return

    input, output = result

    if input:
        LOG("START", "PySC")

        blocks = PySCOpen(input)
    
    if output and input:
        with open(output, "w") as fl:
            for line in blocks:
                fl.write(line)

        LOG("OUTPUT", output)

        print("[DONE]")
        return

if __name__ == "__main__":
    main()