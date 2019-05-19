import sys
import re


with open(sys.argv[1]) as f:
    contents = f.read()
    fixed = re.sub(r'<p>\[caption (.+)\](<img .+>|<a .+a>)(.*)\[/caption\]</p>', r'<figure \1>\2<figcaption>\3</figcaption></figure>', contents)
    fixed = re.sub(r'align="align', r'style="float: ', fixed)
    print(fixed)
