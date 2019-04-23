from __future__ import print_function
import sys
import collections
import json
import pickle

Container = collections.namedtuple('Container', ['version', 'uid', 'gid', 
                      'read_only', 'env', 'cwd', 'path', 'cmd'])
containers = {}

def add_container(container_id, bundle):
    if container_exists(container_id):
       # Print error and exit 
       err_exit("ch_runtime: Container id: {} already exists".format(container_id))
    else:
        with open(bundle + "/config.json", "r") as f:
            config = json.load(f)
        params = parse_json(config)
        # Create a new container namedtuple from the params
        new_container = Container(*params)
        containers[container_id] = new_container

# Returns container state in pretty json
def print_container(container_id):
    container = get_container(container_id)

def container_exists(container_id):
    return container_id in containers

def remove_container(container_id):
    if container_exists(container_id):
        # Remove 
        pass
      
def get_container(container_id):
    if not container_exists(container_id):
        return -1
    else:
        return containers[container_id]

def save_container(container_id):
    with open('/tmp/pickles/' + container_id + '.pickle', 'wb') as handle:
        pickle.dump(containers, handle, protocol=pickle.HIGHEST_PROTOCOL)

def load_container(container_id):
    # looking for a better solution
    global containers
    with open('/tmp/pickles/' + container_id + '.pickle', 'rb') as handle:
        containers = pickle.load(handle)

def parse_json(config):
    # The OCI version
    version = config['ociVersion']
    # The Uid of the container
    uid = config['process']['user']['uid']
    # The Gid of the container
    gid = config['process']['user']['gid']
    # Whether the container is readonly or root
    read_only = 'readonly' in config['root']
    # Environment variables in container
    env = config['process']['env']
    # Working directory
    cwd = config['process']['cwd']
    # Path to container
    path = config['root']['path']
    # Cmd to run in the container
    cmd = config['process']['args']
    return [version, uid, gid, read_only, env, cwd, path, cmd]
