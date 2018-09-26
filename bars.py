import json
import math
from functools import reduce


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        parsed_json = json.loads(file.read())
    return parsed_json


def get_biggest_bar(data):
    return reduce(lambda x, y: x if max([x['properties']['Attributes']['SeatsCount'],
                                         y['properties']['Attributes']['SeatsCount']]) \
                                    == x['properties']['Attributes']['SeatsCount'] else y, data)


def get_smallest_bar(data):
    return reduce(lambda x, y: x if min([x['properties']['Attributes']['SeatsCount'],
                                         y['properties']['Attributes']['SeatsCount']]) \
                                    == x['properties']['Attributes'][
                                        'SeatsCount'] else y, data)


def get_closest_bar(data, longitude, latitude):
    """distance  = math.sqrt((x2-x1)**2+(y2-y1)**2)"""

    pass
    # "geometry" "coordinates" [37.5808294018246, 55.759148105306608]


if __name__ == '__main__':
    data = load_data('bars.json')
    # print(data)
    biggest_bar = get_biggest_bar(data['features'])
    print(biggest_bar)
    smallest_bar = get_smallest_bar(data['features'])
    print(smallest_bar)
    # longitude = input('Please input longitude: ')
    # latitude = input('Please input latitude: ')
    # get_closest_bar(data, longitude, latitude)
