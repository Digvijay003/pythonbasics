import sys

sys.stderr.write("this is stdrtext\n")
sys.stdout.write("this is stdrouttext\n")
print(sys.argv)

def main(argv):
    print(sys.argv[1])# usisng sys we can pass as many 
                      # arguments we want also from command line
main(sys.argv[1])
