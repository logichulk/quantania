import subprocess as cmd
#import paramiko

from datetime import datetime

# Auto-commit script for content.

#ssh_client = paramiko.SSHClient()
#ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#ssh_client.connect(hostname='https://github.com/logichulk/books.git',username='',password='')

statements = list()

statements.append("git add .")
statements.append("git commit -m 'Autocommit at " + str(datetime.now()) + "'")
statements.append("git push -u origin master -f")

for statement in statements:
	cmd.call(statement, shell=True)
