#!/usr/bin/env python
from __future__ import print_function
import sys
import os
import argparse
import shutil

# This script is the beginning of a barebones implementation of the OCI runtime spec
# Located at https://github.com/opencontainers/runtime-spec/blob/master/runtime.md#start 

# Check if a container already exist
def container_exists(container_id):
    return container_id in containers

# Remove an id that is no longer needed
def free_id(container_id):
    print("IN FREE")
    containers.pop(container_id, None)
      
# Start a container
def start(container_id):
    print("IN START")
    # Read the json.config

    # Run the process specified in program

    # Genererate an error if container does not exists
    if not container_exists(container_id):
        error() 

# Create a container
def create(container_id, path):
    print("In CREATE")
    # Check if container-id exist 
    
    # Check path

    # Load json.conf
    pass

# Stop a container 
def kill(container_id):
    container = containers[container_id]

    if not container_exists(container_id):
        error("kill: container does not exist") 
    if not container_running(container_id):
        error("kill: container is currently running")
    
# Delete a container
def delete(container_id):
    print("IN DELETE")
    container = containers[container_id]

    #if container.state = RUNNING:
    #    error("Container must be stopped")
    
    # Delete the container and all resources created during create step
    
    free_id(container_id)

# Returns the current state of a container
def state(container_id):
    if not container_exists(container_id):
        error("state: container doe not exist")

    container = containers[container_id]

    return container.state

# This code should parse the arguments provided by buildah
# It is currently commented out because I've had an issue getting an extra positional
# argument at the end of the invocation

# As an example, buildah will call runtime.py with 
# runtime.py create --bundle /tmp/buildah789033157 --pid-file 
# /tmp/buildah789033157/pid --no-new-keyring --console-socket 
# /tmp/buildah789033157/console.sock buildah-buildah789033157
# This parser gets create and all of the optional (--) arguments but cannot get the final buildah-buildah* 

#parser = argparse.ArgumentParser()
#parser.add_argument("operation", help="create an OCI contianer using specifed bundle", nargs="*", default=[])
#parser.add_argument("name", help="name of the oci container", nargs="?", default=[])
#parser.add_argument("--bundle", help="path to an OCI 'bundle'", nargs="1",  default=[])
#parser.add_argument("--no-new-keyring", help="dont create a new keyring", default=[])
#parser.add_argument("--console-socket", help="path to a socket", nargs="1", default=[])
#parser.add_argument("--pid-file", help="path to a pid file", nargs="1", default=[])
#
##args = parser.parse_args()
#args = parser.parse_args()
#
#if args.operation == "create":
#    print("Create")
#elif args.operation == "start":
#    print("Start")
#elif args.operation == "delete":
#    print("Delete")
#elif args.operation == "state":
#    print("State")
#elif args.operation == "kill":
#    print("Kill")
#
#if args.bundle:
#    print(args.bundle)

# Write debug output to a log
f = open("log", "w")
# Write the invocation buildah uses
f.write(str(sys.argv))
# 
bundle = str(sys.argv[3])
# Directory of the bundle
f.write(bundle)
f.write(os.listdir(bundle))

# Copy the bundle to a directory
os.system("cp -r {} ~/bundle".format(bundle))
#f.write(str(sys.argv))
#f.close()


