import re
import logging
import sys
import argparse
import os
#uncomment the below to enable debuggin :) just wanted to add this in for everyone
#import pdb; pdb.set_trace()_

def start_parsing(log_file, searchqueries):
    
    try:
        logFile = open(log_file,'r')
        outputFile = open(os.path.dirname(log_file)+'/parsedOutput.txt', 'a')
        Lines=logFile.readlines()
        print searchqueries[0]
        for i in range(len(Lines)):
            if any(str(query) in Lines[i].strip().replace('\x00','') for query in searchqueries):
	            outputFile.write(Lines[i].strip().replace('\x00',''))
	            outputFile.write('\n\n')
        logFile.close()
        outputFile.close()
    
    except Exception as e:
    	print 'Caught exception: %s' % e
    	try:
            logFile.close()
            outputFile.close()
        except:
            pass
        sys.exit(1)

def main():
	print ("In parser")
	parser = argparse.ArgumentParser(description='The Parser!')
	parser.add_argument('log_file', metavar='log_file', type=str, nargs=1)
	parser.add_argument('-s','--searchqueries', nargs='+')
	args = parser.parse_args()
	start_parsing(log_file=args.log_file[0], searchqueries=args.searchqueries)

if __name__ == "__main__":main()
