from loader import Duration

MAIN_START = '2016-01-05'

d = {
    'Alice':
    [
        Duration(MAIN_START, '2017-01-01', '', True),
        Duration('2017-01-02', '2017-04-01', 'In America', False),
        Duration('2017-04-02', '', '', False),
    ],
    'Bob':
    [
        Duration(MAIN_START, '', '', True),
    ],
}