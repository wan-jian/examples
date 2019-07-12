# key-value

cources = [{'title': 'operating system', 'scores':[{'id':'0001',
                                                   'name': 'Zhangsan',
                                                   'score': 80},
                                                  {'id':'0002',
                                                   'name': 'Lisi',
                                                   'score': 75}]},
           {'title': 'database system', 'scores':[{'id':'0001',
                                                   'name': 'Zhangsan',
                                                   'score': 90},
                                                  {'id':'0002',
                                                   'name': 'Lisi',
                                                   'score': 85}]}
         ]
for c in cources:
    print(c['title'])
    for s in c['scores']:
        print(s['name'], s['score'])




