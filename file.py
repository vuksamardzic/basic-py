fo = open('text.txt', 'w')

print('name ', fo.name)
print('closed ? ', fo.closed)
print('opening mode: ', fo.mode)
fo.write('i love py')
fo.write(' and javascript. ')

# append mode, otherwise it gets replaced.. also there are w+ r+ etc...
fo = open('text.txt', 'a')
fo.write('And node!')
fo.close()
