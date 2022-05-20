'''
Created By:         James Rogers - jmr172@utulsa.edu
Created On:         05/15/2017
Last Modified By:   James Rogers - jmr172@utulsa.edu
Last Modified On:   08/24/17
Course:             Forensics F-17
Purpose:            Provides a common command line interface for running forensics modules.
'''

# Import required for argument parsing.
import argparse, sys
from argparse import RawTextHelpFormatter

# Import the forensis module classes from their python files.
from Cracker import PasswordCracker
from Carver import FileCarver
from Steg import Steganography
from Spoof import DetectSpoof

# Main function which parses command line arguments, instantiates the proper forensics tool, and
# runs it with the provided arguments.
def main():

    # Help message that will be printed when using the '-h' flag.
    helpMsg = "Forensics Toolkit Command Line Interface \n" +\
              "---------------------------------------- \n" +\
              "This tool implements a password cracking tool, a  \n" +\
              "data carver tool, and a tool used for embeddeding \n" +\
              "and extracting data with steganography.\n" +\
              "\nPassword Cracker Command: \n" +\
              "\t" + sys.argv[0] + " cracker -d messageDigest" +\
              "\nData Carver Command: \n" +\
              "\t" + sys.argv[0] + " carver -i inputFile -o output" +\
              "\nSteganography Command: \n" +\
              "\t" + sys.argv[0] + " steg -t task [messageFile] -i inputFile" +\
              "\nDetect Spoof Command: \n" +\
              "\t" + sys.argv[0] + " spoof -i inputFile"

    # Invokes an argparse instance to parse the user provided arguments.
    parser = argparse.ArgumentParser(description=helpMsg, formatter_class=RawTextHelpFormatter)
    parser.add_argument("tool", help = "Either cracker, carver, or steg")
    parser.add_argument("-d", "--digest", help="MD5 hash for the password to be cracked")
    parser.add_argument("-i", "--input", help="Input file")
    parser.add_argument("-o", "--output", help="Output file or directory")
    parser.add_argument("-t", "--task", nargs='*', default=["extract", ""], \
        help="steg extract command or steg embed command followed by a message file")
    args = parser.parse_args()

    # Runs the correct forensic class depending on the provided arguments.
    if args.tool == "cracker":
        cracker = PasswordCracker(args.digest)
        cracker.crack()
    elif args.tool == "carver":
        carver = FileCarver(args.input, args.output)
        carver.carve()
    elif args.tool == "steg":
        steg = Steganography(args.task[0], args.task[1], args.input)
        steg.steg()
    elif args.tool == "spoof":
        spoof = DetectSpoof(args.input)
        spoof.run()

# Executes the main function if the Python interpreter is running this file as main.
if __name__ == '__main__':
    main()
