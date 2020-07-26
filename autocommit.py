import subprocess as cmd

from datetime import datetime

# Auto-commit script for content.

statements = list()

statements.append("git add .")
statements.append("git commit -m 'Autocommit at " + str(datetime.now()) + "'")
statements.append("git push -u origin master -f")
statements.append("logichulk")
statements.append("F22rptr")

for statement in statements:
	cmd.call(statement, shell=True)
