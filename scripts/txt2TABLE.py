import sys


with open(sys.argv[1]) as fh, open(sys.argv[2], 'w') as out:
    out.write('\\bTABLE\n')
    for line in fh:

        # ignore empty lines
        if not line:
            continue

        out.write('\\bTR\n')

        words = line.split()
        for word in words:
            out.write('\\bTD ' + word + ' ''eTD ')
        
        out.write('\n\\eTR\n')
    out.write('\\eTABLE\n')
