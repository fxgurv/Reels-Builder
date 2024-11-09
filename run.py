#!/usr/bin/env python
import os
import sys
import subprocess
from collections import defaultdict

class DjangoCommandCLI:
    def __init__(self):
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ReelsBuilder.settings')
        self.commands = {
            'auth': {
                1: 'changepassword',
                2: 'createsuperuser'
            },
            'contenttypes': {
                1: 'remove_stale_contenttypes'
            },
            'django': {
                1: 'check',
                2: 'compilemessages',
                3: 'createcachetable',
                4: 'dbshell',
                5: 'diffsettings',
                6: 'dumpdata',
                7: 'flush',
                8: 'inspectdb',
                9: 'loaddata',
                10: 'makemessages',
                11: 'makemigrations',
                12: 'migrate',
                13: 'optimizemigration',
                14: 'sendtestemail',
                15: 'shell',
                16: 'showmigrations',
                17: 'sqlflush',
                18: 'sqlmigrate',
                19: 'sqlsequencereset',
                20: 'squashmigrations',
                21: 'startapp',
                22: 'startproject',
                23: 'test',
                24: 'testserver'
            },
            'sessions': {
                1: 'clearsessions'
            },
            'social_django': {
                1: 'clearsocial'
            },
            'staticfiles': {
                1: 'collectstatic',
                2: 'findstatic',
                3: 'runserver'
            }
        }

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_main_menu(self):
        self.clear_screen()
        print("\n=== Django Management Commands ===")
        print("\nAvailable command categories:")
        for i, category in enumerate(self.commands.keys(), 1):
            print(f"{i}. [{category}]")
        print("0. Exit")

    def print_category_menu(self, category):
        self.clear_screen()
        print(f"\n=== {category.upper()} Commands ===")
        for num, command in self.commands[category].items():
            print(f"{num}. {command}")
        print("0. Back to main menu")

    def execute_command(self, command):
        try:
            subprocess.run([sys.executable, 'manage.py'] + command.split())
        except Exception as e:
            print(f"Error executing command: {e}")
        input("\nPress Enter to continue...")

    def run(self):
        while True:
            self.print_main_menu()
            try:
                choice = input("\nEnter your choice (0-6): ")
                if choice == '0':
                    print("Goodbye!")
                    break

                categories = list(self.commands.keys())
                if choice.isdigit() and 1 <= int(choice) <= len(categories):
                    category = categories[int(choice) - 1]
                    
                    while True:
                        self.print_category_menu(category)
                        subchoice = input(f"\nEnter command number (0 to go back): ")
                        
                        if subchoice == '0':
                            break
                        
                        if subchoice.isdigit() and int(subchoice) in self.commands[category]:
                            command = self.commands[category][int(subchoice)]
                            print(f"\nExecuting: python manage.py {command}")
                            self.execute_command(command)
                else:
                    print("Invalid choice. Please try again.")
                    input("Press Enter to continue...")
            
            except KeyboardInterrupt:
                print("\nOperation cancelled by user.")
                break
            except Exception as e:
                print(f"An error occurred: {e}")
                input("Press Enter to continue...")

if __name__ == '__main__':
    cli = DjangoCommandCLI()
    cli.run()