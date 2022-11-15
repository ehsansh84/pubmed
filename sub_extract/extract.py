import re

f = open('articles.txt')
text = f.read()
f.close()
text = text.replace('\n', 'ehsan')
# print(text)
try:
    # here ; and / are our two markers
    # in which string can be found.
    # marker1 = 'Au'
    # marker2 = 'on:'
    marker1 = 'Author information:'
    marker2 = 'DOI:'
    regexPattern = marker1 + '(.+?)' + marker2
    abtracts = re.findall(regexPattern, text)
    # print(str_found)
    f = open('output.txt', 'w')
    skip = False
    output = ''
    for abtract in abtracts:
        article = abtract.replace('ehsan', '\n')
        for line in article.split('\n'):
            if len(line) > 1:
                # print(line)
                if skip:
                    skip = False
                    # f.write('+'*20 + '\n')
                    continue
                if line[0] == '(':
                    skip = True
                    # f.write('+'*20 + '\n')
                else:
                    f.write(line)
        # print(repr(abtract.replace('ehsan', '\n')))
        f.write('\n=========================\n')
    f.close()
except AttributeError:
    # Attribute error is expected if string
    # is not found between given markers
    str_found = 'Nothing found between two markers'
# print(len(abtracts))
