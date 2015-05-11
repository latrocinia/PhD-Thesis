import sys


with open(sys.argv[1]) as fh, open(sys.argv[2], 'w') as out:
    out.write('\\bTABLE\n')
    for line in fh:

        # ignore empty lines
        if not line:
            continue

        # split at | and remove white space
        words = line.split('|')
        data = ' \\eTD \\bTD '.join(words)
        out.write('\\bTR\n\\bTD ' + data[:-1] + ' \\eTD\n\\eTR\n')
        
    out.write('\\eTABLE\n')
