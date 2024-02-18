import requests
import csv
import os
from utils import get_date, send_email
BASE_URL = 'https://api.github.com/repos'
class Repository:
    def __init__(self, repo='antonputra/tutorials'):
        self.repo = repo
        self.headers = {'Authorization': os.environ.get('GITHUB_TOKEN')}
        print(f"Getting Repository PR's from repository: {self.repo}")

    def fetch_pull_requests(self):    
        try:
            resp = requests.get(f'{BASE_URL}/{self.repo}/pulls?state=all', self.headers)
            if resp.status_code == 200:
                return resp.json()
        except Exception as error:
            print('An error occurred', error)
            return []
        
    def categorize_pull_requests(self):
        prs = self.fetch_pull_requests()
        
        open = list(filter(lambda x: x['state'] == 'open', prs))
        closed = list(filter(lambda x: x['state'] == 'closed', prs))
        merged = list(filter(lambda x: x['state'] == 'merged', prs))
        
        return open, closed, merged

    def print_pr_details(self):
        open_prs, closed_prs, merged_prs = self.categorize_pull_requests()
        print(f'There are {len(open_prs)} open pull requests in total')
        print(f'There are {len(closed_prs)} closed pull requests in total')
        print(f'There are {len(merged_prs)} merged pull requests in total')
    
    def print_report(self):
        prs = self.fetch_pull_requests()
        self.print_pr_details()
        send_email(prs)
        
    def generate_csv_report(self):
        open_prs, closed_prs, merged_prs = self.categorize_pull_requests()
        self.print_pr_details()
        
        with open(f'{get_date()}_pull_requests.csv', 'w', newline='') as csv_file:
            fields = ['Title','Body', 'State', 'Username']
            w = csv.DictWriter(csv_file, fieldnames=fields)
            
            w.writeheader() 
            for pr in open_prs:
                w.writerow({'Title': pr['title'], 'Body': pr['body'], 'State': pr['state'], 'Username': pr['user']['login']})
            for pr in closed_prs:
                w.writerow({'Title': pr['title'], 'Body': pr['body'], 'State': pr['state'], 'Username': pr['user']['login']})
            for pr in merged_prs:
                w.writerow({'Title': pr['title'], 'Body': pr['body'], 'State': pr['state'], 'Username': pr['user']['login']})