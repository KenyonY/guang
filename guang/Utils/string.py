import re

def find_match(start, end, S, IGNORECASE=True):
    """find the string between `start` and `end` of `S`
    and ignore case
    """
    START = re.search(start, S, re.IGNORECASE).span()[1]
    END = re.search(end, S, re.IGNORECASE).span()[0]
    return S[START:END]

def replace(string, beRepl, repl, count=1):
    """replace `beRepl` to 'repl' from `string` count times.
    if count=0, relplace all."""
    strinfo = re.compile(beRepl)
    return strinfo.sub(repl, string, count)
