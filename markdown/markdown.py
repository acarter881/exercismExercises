import re

headingRegEx = re.compile('(#{1,6}) (.*)')
boldRegEx = re.compile('(.*)__(.*)__(.*)')
italicRegEx = re.compile('(.*)_(.*)_(.*)')
unorderedListRegEx = re.compile(r'\* (.*)')
tagRegEx = re.compile('<h|<ul|<p|<li')

def boldTest(s=None):
    m1 = re.match(boldRegEx, s)
    if m1:
        curr = m1.group(1) + '<strong>' + \
            m1.group(2) + '</strong>' + m1.group(3)
        is_bold = True

def italicTest(s=None):
    m1 = re.match(italicRegEx, s)
    if m1:
        curr = m1.group(1) + '<em>' + m1.group(2) + \
            '</em>' + m1.group(3)
        is_italic = True

def parse(markdown):
    lines = markdown.split('\n')
    res = ''
    in_list = False
    in_list_append = False

    for i in lines:
        if re.match(headingRegEx, i):
            i = '<h' + str(len(re.match(headingRegEx, i).group(1))) + '>' + i[len(re.match(headingRegEx, i).group(1))+1:] + '</h' + str(len(re.match(headingRegEx, i).group(1))) + '>'
        
        m = re.match(unorderedListRegEx, i)

        if m:
            if not in_list:
                in_list = True
                is_bold = False
                is_italic = False

                curr = m.group(1)
                boldTest(curr)
                italicTest(curr)

                i = '<ul><li>' + curr + '</li>'
            else:
                is_bold = False
                is_italic = False

                curr = m.group(1)
                boldTest(curr)
                italicTest(curr)
                
                i = '<li>' + curr + '</li>'
        else:
            if in_list:
                in_list_append = True
                in_list = False

        m = re.match(tagRegEx, i)

        if not m:
            i = '<p>' + i + '</p>'
        
        boldTest(m)
        italicTest(m)
        
        if in_list_append:
            i = '</ul>' + i
            in_list_append = False
        res += i

    if in_list:
        res += '</ul>'
    return res

print(parse('This will _be_ __mixed__'))