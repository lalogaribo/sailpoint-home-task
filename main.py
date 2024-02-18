import sys
from repository import Repository

if __name__ == '__main__':
    repository = sys.argv[1] if len(sys.argv) > 1 else 'antonputra/tutorials'
    repo = Repository(repository)
    flag = True
    while flag:
        print('################Menu##############')
        print('To send email press 1 ')
        print('To generate a csv file press 2 ')
        print('To exit the application press 3 ')
        print('To set a new search press 4 ')
        
        option = int(input())
        if option == 1:
            repo.print_report()
        elif option == 2:
            repo.generate_csv_report()
        elif option == 3:
            print('Thank you for using the application')
            flag = False
        elif option == 4:
            repo_name = input('Insert the repository name ')
            repo = Repository(repo_name)
        else:
            print('Invalid option')
            
    
