# I personally think it's easiest to just define the data in a Python dict,
# like in example.py. This file gives you other options just in case.

import json

from collections import namedtuple

# Example Duration('2014-01-01', '2015-01-01', '', True)
# Example Duration('2017-01-06', '2017-04-06', 'In America', False)
# Example Duration('2017-01-06', '', '', True)  # Empty end means ongoing.
Duration = namedtuple('Duration', ['start', 'end', 'description', 'present'])


def _dict_to_json(d):
    return json.dumps(d)


def _json_to_dict(j):
    d = json.loads(j)
    new = {}
    for k, v in d.items():
        new[k] = [Duration(*i) for i in v]
    return new

# Only the below functions should be used externally.


def load_from_csv(fname):
    '''
    TODO
    '''
    pass


def load_from_json(fname):
    '''
    Given a json file, load the data into a python dictionary.
    '''
    with open(fname, 'r') as f:
        return _json_to_dict(f.read())


# I've included this because I would prefer to work with a straight dictionary
# instead of having to deal with json while I'm developing it.
def load_from_python(fname):
    '''
    Given a python file with a single dictionary defined called d, load it.
    This is the least solid function here, converting a filename to a module
    name is flaky at best. I recommend avoiding this function.
    '''
    from importlib import import_module
    module_name = '.'.join(fname.split('.')[:-1])
    module_name = module_name.replace('/', '.')
    module = import_module(module_name)
    return module.d


def dump_to_csv(timeline_dict):
    '''TODO'''
    pass


def dump_to_json(timeline_dict):
    '''TODO'''
    pass
