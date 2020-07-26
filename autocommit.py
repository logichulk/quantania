import subprocess as cmd
import paramiko

from datetime import datetime

# Auto-commit script for content.

ssh_client=paramiko.SSHClient()
ssh_client.connect(hostname=’hostname’,username=’logichulk’,password=’F22rptr’)

statements = list()

statements.append("git add .")
statements.append("git commit -m 'Autocommit at " + str(datetime.now()) + "'")
statements.append("git push -u origin master -f")
statements.append("logichulk")
statements.append("F22rptr")

for stmt in statement:
	cmd.call(stmt, shell=True)
