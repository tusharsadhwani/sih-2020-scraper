"""SIH 2020 Problem Statement Scraper"""
import os
import pathlib
import pickle
import sys
from requests_html import HTMLSession


PROBLEMS_FILEPATH = (
    pathlib.Path(__file__).parent.absolute().joinpath('problems.pickle')
)


def store_problems():
    """Scrapes the website and stores all the problems locally"""
    session = HTMLSession()
    problems = []

    for index in range(1, 37):
        page = session.get(f'https://www.sih.gov.in/sih2020PS?page={index}')

        table = page.html.find('#dataTablePS')[0]
        _, tbody, _ = table.element

        for row in tbody:
            org = row[0].text
            code = row[3].text
            field = row[4].text

            title = row[1][0].text

            desc_table = row[1][1][0][1][1][0]
            description = desc_table[0][0][1][0].text

            problems.append([code, title, org, field, description])

    with open(PROBLEMS_FILEPATH, 'wb') as problems_file:
        pickle.dump(problems, problems_file)


def search_problems():
    """Search through the problemset"""
    if not os.path.exists(PROBLEMS_FILEPATH):
        print('Problems not found. Trying to download...')
        store_problems()

    with open(PROBLEMS_FILEPATH, 'rb') as problems_file:
        problems = pickle.load(problems_file)

    while True:
        try:
            query = input('Enter code or title> ')
        except KeyboardInterrupt:
            sys.exit()

        for prob in problems:
            code = prob[0]
            title = prob[1]

            if query.lower() in code.lower():
                for i in prob:
                    print(i, end='\n\n')
                print('-'*40)

            elif query.lower() in title.lower():
                for i in prob:
                    print(i, end='\n\n')
                print('-'*40)


if __name__ == "__main__":
    search_problems()
