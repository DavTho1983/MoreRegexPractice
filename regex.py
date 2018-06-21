import re

text_to_search = '321-555-4321'

"""raw string with r"""

print('\tTab')
print(r'\tTab')

#pattern = re.compile(r'a$') find a at the end
#\d matches any digit
# pattern = re.compile(r'\d\d\d') matches groups of three digits
#. matches any char
# pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d') matches - or . but nothing else
# pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d') matches 8 or 9 with two 0s
# pattern = re.compile(r'[1-5][1-5][1-5][-.][1-5][1-5][1-5][-.][1-5][1-5][1-5]') matches only digits between 1 and 5 inclusive
# pattern = re.compile(r'[a-zA-Z]') matches lowercase or uppercase letters
# pattern = re.compile(r'[^a-zA-Z]') matches NOT lowercase or uppercase letters
# pattern = re.compile(r'[^b]at') NOT b followed by at
# * matches 0 o more
# + matches 1 or more
# ? matches 0 or 1
# {3} matches exact number
# {3,4} matches range of numbers {min, max}
# pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
# () groups allow to match several different patterns
# pattern = re.compile(r'M(r|s|rs|iss)\.?\s[A-Z]\w*\s[A-Z]\w*')
# pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z]+\.(com|edu)') email matches
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
# pattern = re.compile(r'start', re.I) IGNORECASE flag

matches = pattern.finditer(text_to_search) #see also findall, match, search


#for match in matches:
#    print(match)


with open('urls.txt', 'r', encoding='utf-8') as f:
    contents = f.read()
    matchstr = ''
    matches = pattern.finditer(contents)
    for match in matches:
        matchstr = matchstr + '\n' + str(match)
        print(matchstr)


    subbed_urls = pattern.sub(r'\2\3', matchstr)

    print(subbed_urls)

    # for match in matches:
    #     print(match.group(0)) #prints entire url
    #     print(match.group(1)) #prints out www. or None
    #     print(match.group(2)) #prints out top level domain


    # print(subbed_urls)
