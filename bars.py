import json
import math


def load_data(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as bars_file:
            parsed_json = json.loads(bars_file.read())
        return parsed_json['features']
    except IOError:
        raise IOError('Could not open file bars.json!')
    except ValueError:
        raise ValueError('Wrong JSON!')


def get_biggest_bar(bars_dict):
    return max(
        bars_dict,
        key=lambda x: x['properties']['Attributes']['SeatsCount']
    )


def get_smallest_bar(bars_dict):
    return min(
        bars_dict,
        key=lambda x: x['properties']['Attributes']['SeatsCount']
    )


def get_closest_bar(bars_dict, longitude, latitude):
    try:
        longitude = float(longitude)
        latitude = float(latitude)
    except ValueError:
        raise ValueError('Wrong coordinates!')
    return min(bars_dict, key=lambda x: calc_distance(
        x['geometry']['coordinates'][1],
        x['geometry']['coordinates'][0],
        longitude,
        latitude)
    )

def calc_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def display_bar_info(bar_dict):
    return '{}, {}'.format(
        bar_dict['properties']['Attributes']['Name'],
        bar_dict['properties']['Attributes']['Address']
    )


if __name__ == '__main__':
    try:
        bars_dict = load_data('bars.json')

        biggest_bar = get_biggest_bar(bars_dict)
        print('Самый вместительный бар: {}'.format(
            display_bar_info(biggest_bar))
        )

        smallest_bar = get_smallest_bar(bars_dict)
        print('Самый тесный бар: {}'.format(
            display_bar_info(smallest_bar))
        )

        longitude = input('Please input longitude: ')
        latitude = input('Please input latitude: ')
        closest_bar = get_closest_bar(bars_dict, longitude, latitude)
        print('Ближайший бар: {}'.format(
            display_bar_info(closest_bar))
        )
    except ValueError as exc_text:
        print(exc_text)
    except IOError:
        print("Could not open file!")
