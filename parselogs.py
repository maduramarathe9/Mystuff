
import os
import re
import sys,getopt


def main(argv):

    inputfile =''
    outputfile =''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print 'test.py -i <inputfile> -o <outputfile>'
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
            testfile= open(os.path.expanduser(inputfile))
            f = testfile.readlines()

        elif opt in ("-o", "--ofile"):
            outputfile = arg
    print 'Input file is "', inputfile
    print 'Output file is "', outputfile

    for i in range(len(f)):
        f[i] = (f[i].rstrip('\n').replace("\x00",""))

    for line in f:

        if "Unable" in line:
            print line

if __name__ == "__main__":
    main(sys.argv[1:])







