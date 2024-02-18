import datetime
from tabulate import tabulate

def get_date():
    date = datetime.date.today()
    return date

def send_email(prs):
    sender = input('Enter sender ')
    receiver = input('Enter receiver ')
    subject = input('Enter subject ')
    body = input('Enter body ')
    
    print(f'From: {sender}')
    print(f'To: {receiver}')
    print(f'Subject: {subject}')
    print(f'Body: {body}')
    
    table_data = []
    for pr in prs:
        table_data.append([pr['number'], pr['title'], pr['user']['login'],pr['state'], pr['created_at']])
    # print(table_data)
    print(tabulate(table_data, headers=['Number', 'Title', 'User', 'Status', 'Created At'], tablefmt='heavy_grid'))