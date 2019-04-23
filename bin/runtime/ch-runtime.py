#!/usr/bin/env python
import sys
import os
import subprocess
import glob
from container import *
from error import *

# This script is the beginning of a barebones implementation of the OCI runtime spec
# Located at https://github.com/opencontainers/runtime-spec/blob/master/runtime.md#start 
pid = 0

# Create a container
def create(container_id, bundle):
    global pid
    # Add the container to the container list
    add_container(container_id, bundle)
    
    # Tar the rootfs to use with ch-tar2dir
    # Needed kludge for charliecloud
    os.chdir(bundle + "/mnt/rootfs")
    p1 = subprocess.Popen(["tar", "czf", "../container.tar.gz"] + glob.glob("*"), stdout=subprocess.PIPE)
    err = p1.communicate()[1]
    # Turn the tar into a runnable container directory
    os.chdir("..")
    subprocess.call(["ch-tar2dir", "container.tar.gz", "."])

    # We fork this process in create then write the pid of the child to 
    # the pid file. The child simply loops so that when buildah looks for 
    # the PID it's running. 
    pid = os.fork()
    if pid == 0:
        # If the child just loop
        # Should probably be some kind of busy-wait
        # Sleep forever instead
        while True:
            pass
    else:
        # Write the pid of the child to the pid file to appease buildah
        pid_file = bundle + "/pid"
        with open(pid_file, "w") as file:
            file.write(str(pid))

# Start a container
def start(container_id):
    container = get_container(container_id)
    if not container:
        err_exit("ch-runtime: (Start) Container does not exist")
    os.chdir(container.path)
    os.chdir("..")

    # Create the command to run in the container
    # TODO use the parameters from the container to see if we actually need 
    # -w and if it should be root
    command = ["ch-run", "-w", "--uid=0", "--gid=0", "container", "--", 
               "sh", "-c", container.cmd[2]] 

    # Run the commmand
    output = subprocess.check_output(command, stdin=subprocess.PIPE)
    
# Stop a container 
# This will probably not be necessary in our final implementation
def kill(container_id):
#    container = get_container(container_id)
#    if not container_exists(container_id):
#        err_exit("ch-runtime: (kill) Container does not exist") 
    pass
    
# Delete a container
def delete(container_id):
    pass

# Returns the current state of a container
def state(container_id):
    if not container_exists(container_id):
        error("state: container does not exist")
    #container = get_container(container_id)
    return 1

if __name__ == "__main__":
    if len(sys.argv) < 2:
        err_exit("Usage: ch_runtime [create | start | state | kill | delete]")
    op = sys.argv[1]
    container_id = sys.argv[-1]

    # Check if we have a 'pickle' of the previous state
    # To prevent race conditions, we give each container it's own pickle
    pickle_exists = os.path.isfile('/tmp/pickles/' + container_id + '.pickle')
    if pickle_exists:
        load_container(container_id)

    if op == "create":
        bundle = sys.argv[3]
        create(container_id, bundle)
        save_container(container_id)
    elif op == "start":
        start(container_id)
        save_container(container_id)
    elif op == "state":
        state(container_id)
    elif op == "kill":
        kill(container_id)
    elif op == "delete":
        delete(container_id)
    else:
        err_exit("ch_runtime: Unknown operation")
