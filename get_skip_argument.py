#!/usr/bin/python3

import sys
if len(sys.argv) == 2:
    arg = sys.argv[1].split("skip::")
    if len(arg) > 1:
        arg = arg[1].split()[0]
    else:
        print("No skip instance found.")
        sys.exit(0)
        
    with open("skip_arg.txt", "w") as arg_file:
        arg_file.write(arg)

else:
    print("Incorrect number of argument!")
    sys.exit(1)
