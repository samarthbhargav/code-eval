import sys

def limit(text):
    n = len(text)
    if n <= 55:
        return text
    
    return text[:40].strip() + "... <Read More>"
    
with open(sys.argv[1]) as reader:
    for line in reader:
        print limit(line)