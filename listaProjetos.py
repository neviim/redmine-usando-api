#!/usr/bin/env python
# -*- coding: utf-8 -*-

from redmine import Redmine

abre = Redmine('http://seuRedmine.com', key='f1f8b5627d32b48332324556545fe4545eda3434sf4545f')

projeto = abre.projects[3]

print projeto.id
print projeto.identifier
#print dir(projeto)
print "--------------"

# Lista todos os projetos
for proj in abre.projects:
	print "%s : %s : %s" % (str(proj.id).rjust(4,'0'), proj.name, proj.parent)

print "--------------"

# Lista todos os itens de um projeto
# http://%@:%@%@/issues.xml
for issue in projeto.issues:
	print issue.id, issue.start_date
	#print normalize('NFKD', issue).encode('ascii','ignore')
