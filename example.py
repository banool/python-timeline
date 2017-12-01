# I'm using this dict to build the json.

from collections import namedtuple

# Example Duration('2014-01-01', '2015-01-01', '', True)
# Example Duration('2017-01-06', '2017-04-06', 'In America', False)
# Example Duration('2017-01-06', '', '', True)  # Empty end means ongoing.
Duration = namedtuple('Duration', ['start', 'end', 'description', 'present'])

MAIN_START = '2015-01-02'

d = {
    'Daniel':
    [
        Duration(MAIN_START, '2017-01-05', '', True),
        Duration('2017-01-06', '2017-04-06', 'In America', False),

    ],
    'Kurt':
    [
        Duration(MAIN_START, '?', '', True),
        Duration('2016-11-??', '', 'Westpac', False),
    ]
    'Antonio':
    [
        Duration('2016-11-19', '', '', True),
    ],
    'Dean':
    [
        Duration('2017-07-29', '', '', True),
    ]
}

'''
Daniel
Kurt
Meg
Elsie
Roger
Lachy
Jasreena
Shannon
Niamh
Boyd
Damon
Antonio
Bianca
Ren-ai
Dean
Sarah
'''
