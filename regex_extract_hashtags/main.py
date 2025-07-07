import re

text = input()

# Match hashtags: # followed by letters, numbers, or underscores
hashtags = re.findall(r'#\w+', text)

for tag in hashtags:
    print(tag)
