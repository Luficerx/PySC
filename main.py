from pysc.pysc import PySCOpen
from pysc.log import LOG

def main():
    LOG("START", "PySC")
    PySCOpen("input.pysc")
    
    # with open("output.txt", "w") as fl:
    #     for line in PySCOpen("config.pysc"):
    #         fl.write(line):

    LOG("OUTPUT", "output.txt")

if __name__ == "__main__":
    main()