import argparse

parser = argparse.ArgumentParser(description='Sign up for a game')
parser.add_argument('start_hour', type=int)
parser.add_argument('end_hour', type=int)
parser.add_argument('-d', '--day_offset', type=int, default=0)
parser.add_argument('-l', '--level', type=str)
parser.add_argument('-n', '--number_of_players', type=int, default=1)
parser.add_argument('-f', '--full_field', action='store_const', const=True, default=False)
parser.add_argument('-r', '--refresh_rate', default=60, type=int)
parser.add_argument('-a', '--advance', type=int, default=30, help='Time in advance required to accept a match (minutes)')

args = parser.parse_args()