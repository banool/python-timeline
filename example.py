# I'm using this dict to build the json.

from collections import namedtuple

# Example Duration('2014-01-01', '2015-01-01', '', True)
# Example Duration('2017-01-06', '2017-04-06', 'In America', False)
Duration = namedtuple('Duration', ['start', 'end', 'description', 'present'])

d = {
    'Daniel':
    [
        Duration('2014-01-01', '2015-01-01', '', True),
        Duration('2017-01-06', '2017-04-06', 'In America', False),
    ],
}
