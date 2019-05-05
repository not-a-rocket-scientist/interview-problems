#!/usr/bin/env python


def remove_comments(some_str: str) -> str:
    """
    Returns tring with removed C++ comments-like substrings

    :param some_str:
    :return:
    """

    # 'states' of iterator:
    states = {
        '"': '"',       # inside string literal
        '//': '\n',     # inside one-line comment
        '/*': '*/'      # inside multi line comment
    }

    # 'state' represents if we output chars or not
    allowed = {None, '"'}

    res = ''                # always return string even if empty given
    state = None            # default state: we are outside strings or comments
    prev = None             # default: we check current and previous symbols
    skip_slash = False      # flag to skip second slash
    skipped_slash = False   # flag to skip first slash (don't know if '//' or '/*' starts currently
    for char in some_str:
        if prev is None:
            pass
            # edge case
            if not (some_str.startswith('//') or some_str.startswith('/*')):
                res += char
        else:
            if state is None:
                if char == '"':
                    state = '"'
                elif prev == '/':
                    if char in {'/', '*'}:
                        state = prev + char
                        skip_slash = True
                        skipped_slash = False
                elif prev != '/' and char == '/':
                    skip_slash = True
                    skipped_slash = True
            else:
                if state == '"' and char == state:
                    state = None
                else:
                    if (states[state] == prev+char) or (states[state] == char):  # state is ('*/' or '\n')
                        state = None

            if state in allowed:
                if char == '/':
                    if skip_slash:
                        skip_slash = False
                    else:
                        if skipped_slash:
                            skipped_slash = False
                            res += '/'
                        res += char
                else:
                    if skipped_slash:
                        skipped_slash = False
                        res += '/'
                    res += char
        prev = char

    return res
