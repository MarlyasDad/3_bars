import json
import math
from functools import reduce


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        parsed_json = json.loads(file.read())
    return parsed_json


def get_biggest_bar(data):
    return reduce(lambda x, y: x if max([x['properties']['Attributes']['SeatsCount'],
                                         y['properties']['Attributes']['SeatsCount']])
                  == x['properties']['Attributes']['SeatsCount'] else y, data)


def get_smallest_bar(data):
    return reduce(lambda x, y: x if min([x['properties']['Attributes']['SeatsCount'],
                                         y['properties']['Attributes']['SeatsCount']])
                  == x['properties']['Attributes']['SeatsCount'] else y, data)


def get_closest_bar(data, longitude, latitude):
    return reduce(lambda x, y: x if min([calc_distance(x['geometry']['coordinates'][1],
                                                       x['geometry']['coordinates'][0],
                                                       longitude,
                                                       latitude),
                                         calc_distance(y['geometry']['coordinates'][1],
                                                       y['geometry']['coordinates'][0],
                                                       longitude,
                                                       latitude)])
                  == calc_distance(x['geometry']['coordinates'][1],
                                   x['geometry']['coordinates'][0],
                                   longitude,
                                   latitude) else y, data)

def calc_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


if __name__ == '__main__':
    data = load_data('bars.json')
    biggest_bar = get_biggest_bar(data['features'])
    print(biggest_bar)
    smallest_bar = get_smallest_bar(data['features'])
    print(smallest_bar)
    longitude = input('Please input longitude: ')
    # longitude = 55.820875
    latitude = input('Please input latitude: ')
    # latitude = 37.604430
    closest_bar = get_closest_bar(data['features'], longitude, latitude)
    print(closest_bar)
