# This script takes the JSON output of the sporting_pulse_spider and produces a text file with a table for each BPL
# age group plus a BPL Championship table formatted for the Logan Lightning Match Day Program.
from __future__ import division
from StringIO import StringIO
import json
import os
import sys


def sort_clubs(a, b):
    if a['points'] == b['points']:
        return a['diff'] - b['diff']
    return a['points'] - b['points']


def get_length(buffer):
    """
    Get the length of a StringIO buffer

    """
    buffer.seek(0, os.SEEK_END)
    return buffer.tell()


def add_spaces(buffer, limit):
    """
    Add spaces to the passed buffer until its size equals limit

    """
    while get_length(buffer) < limit:
        buffer.write(' ')

def main():
    """
    Main method of the script. Script takes one argument which is the path to the json file to use.

    """
    # Build the tables
    tables = {}
    file = sys.argv[1]
    with open(file, 'r') as f:
        data = json.load(f)
        for item in data:
            competition = item['league']
            if competition not in tables:
                tables[competition] = []
            if competition == 'Trophy Superstore Premier League':
                item['apoints'] = int(item['points']) * 5
            elif competition == 'Trophy Superstore Premier League Reserves':
                item['apoints'] = int(item['points']) * 3
            elif competition == 'Trophy Superstore Premier League Under 18':
                item['apoints'] = int(item['points']) * 2
            elif competition == 'Trophy Superstore Premier League Under 16':
                item['apoints'] = int(item['points']) * 1
            existing_table = tables[competition]
            existing_table.append(item)
    # Build Championship Table
    championship = {}
    championship_table = []
    competitions = ['Trophy Superstore Premier League', 'Trophy Superstore Premier League Reserves', 'Trophy Superstore Premier League Under 18', 'Trophy Superstore Premier League Under 16']
    for key, value in tables.iteritems():
        for row in value:
            names = row['club'].split(' ', 2)
            club_name = names[0]
            if row['league'] in competitions:
                if club_name[:4] not in championship:
                    championship[club_name[:4]] = {
                        'club': club_name,
                        'played': int(row['played']),
                        'won': int(row['won']),
                        'drawn': int(row['drawn']),
                        'lost': int(row['lost']),
                        'for': int(row['goals_for']),
                        'against': int(row['goals_against']),
                        'diff': int(row['goals_diff']),
                        'points': int(row['apoints']),
                    }
                else:
                    to_update = championship[club_name[:4]]
                    to_update['played'] += int(row['played'])
                    to_update['won'] += int(row['won'])
                    to_update['drawn'] += int(row['drawn'])
                    to_update['lost'] += int(row['lost'])
                    to_update['for'] += int(row['goals_for'])
                    to_update['against'] += int(row['goals_against'])
                    to_update['diff'] += int(row['goals_diff'])
                    to_update['points'] += int(row['apoints'])
    for club, row in championship.iteritems():
        championship_table.append(row)
    # Output the tables
    for key, value in tables.iteritems():
        print ('\n Table {}'.format(key))
        for item in sorted(value, key=lambda i: int(i['points']), reverse=True):  # note the ordering of the table
            row = StringIO()
            row.write(item['position'])
            add_spaces(row, 3)
            row.write(item['club'][:16])
            add_spaces(row, 20)
            row.write(item['played'])
            add_spaces(row, 23)
            row.write(item['won'])
            add_spaces(row, 26)
            row.write(item['drawn'])
            add_spaces(row, 29)
            row.write(item['lost'])
            add_spaces(row, 32)
            row.write(item['goals_for'])
            add_spaces(row, 35)
            row.write(item['goals_against'])
            add_spaces(row, 38)
            row.write(item['goals_diff'])
            add_spaces(row, 42)
            row.write(item['points'] or '0')
            print row.getvalue()
    # Output the championship table
    print ('\n Championship Table')
    counter = 1
    for item in sorted(championship_table, cmp=sort_clubs, reverse=True):
        row = StringIO()
        row.write(counter)
        add_spaces(row, 3)
        row.write(item['club'])
        add_spaces(row, 20)
        row.write(item['played'])
        add_spaces(row, 23)
        row.write(item['won'] or '0')
        add_spaces(row, 26)
        row.write(item['drawn'] or '0')
        add_spaces(row, 29)
        row.write(item['lost'] or '0')
        add_spaces(row, 32)
        row.write(item['for'] or '0')
        add_spaces(row, 35)
        row.write(item['against'] or '0')
        add_spaces(row, 38)
        row.write(item['diff'] or '0')
        add_spaces(row, 41)
        row.write(item['points'])
        print row.getvalue()
        counter += 1


if  __name__ == '__main__': main()
