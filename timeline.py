# The plan here is to make something that produces a nice graphical timeline.
# The main use case I have in mind is to display the timeline of who has lived
# in my sharehouse, I've always been interested in making something like this.

from contextlib import suppress
from datetime import datetime
from loader import Duration


def validate(timeline_dict):
    '''Validate the input:
    1. Assert that the keys are just strings (names).
    2. Assert that the values are just a list of Duration namedtuples.
    3. Assert that the values in the namedtuple are the expected types.
    4. Assert that the dates line up.
    '''
    for k, v in timeline_dict.items():
        assert isinstance(k, str)
        last = None
        for i in v:
            assert isinstance(i, Duration)
            assert get_valid_date(i.start) is not None
            assert get_valid_date(i.end) is not None or i.end == ''
            assert isinstance(i.present, bool)
            if last is not None:
                # Assert that this start is one day ahead of `last`.
                diff = (get_valid_date(i.start) - get_valid_date(last)).days
                assert diff == 1
            last = i.end


def get_valid_date(date_to_validate):
    '''Returns a datetime object on success, None otherwise.'''
    res = None
    with suppress(ValueError, TypeError):
        res = datetime.strptime(date_to_validate, '%Y-%m-%d')
    return res


def main():
    print('Using "d" from example.py')
    from example import d
    validate(d)


if __name__ == '__main__':
    main()
