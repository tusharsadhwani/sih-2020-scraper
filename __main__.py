import pickle
import os
from requests_html import HTMLSession

def store_problems():
    session = HTMLSession()
    problems = []

    for index in range(1, 37):
        page = session.get(f'https://www.sih.gov.in/sih2020PS?page={index}')

        table = page.html.find('#table_id')[0]
        thead, tbody = table.element

        for tr in tbody:
            org = tr[1].text
            code = tr[4].text
            field = tr[6].text
            
            title = tr[2][0].text

            desc_table = tr[2][1][0][1][1][0]        
            description = desc_table[0][0][1][0].text
            
            problems.append([code, title, org, field, description])

    with open('problems.pickle', 'wb') as f:
        pickle.dump(problems, f)

def search_problems():
    if not os.path.exists('problems.pickle'):
        print('Database not found')
        return
    
    with open('problems.pickle', 'rb') as f:
        problems = pickle.load(f)
    
    while True:
        query = input('Enter code or title> ')

        for prob in problems:
            code = prob[0]
            title = prob[1]
            
            if query.lower() in code.lower():
                for i in prob: print(i, end='\n\n')
                print('-'*40)
            
            elif query.lower() in title.lower():
                for i in prob: print(i, end='\n\n')
                print('-'*40)

if __name__ == "__main__":
    search_problems()