import argparse
import os.path
import glob

def agname(args = None):
    # - Get filenames
    #   - Take args (-i, -e)
    parsedargs = parseargs(args)
    #   - Enumerate
    #   - Filter
    filelist = generatefilelist(parsedargs.include, set(parsedargs.exclude))
    # - Get new filenames
    #   - Take args
    #   - Take filename input
    #   - Create new filename
    # - Apply new filenames
    #   - Run command to rename
    mapping = {file: process(file) for file in filelist}
    currenthead = str()
    for map in mapping:
        if not parsedargs.dry_run:
            os.rename(map, mapping[map])
        oldhead, oldtail = os.path.split(map)
        if currenthead != oldhead:
            currenthead = oldhead
            print(currenthead)
        newhead, newtail = os.path.split(mapping[map])
        if currenthead == newhead:
            print('\t' + oldtail + ' -> ' + newtail)
        else:
            print('\t' + oldtail + ' -> ' + mapping[map])

def parseargs(args = None):
    parser = argparse.ArgumentParser(description = 'Rename files using arbitrary rules',
                                     epilog = 'This process may be destructive; \
                                         please backup your files if they are important.')
    parser.add_argument('-v', '--version', \
                        action='version', \
                        version='%(prog)s 0.1.0')
    parser.add_argument('-i', '--include', \
                        help = 'directories to include (supports expansion, globbing)', \
                        action = 'extend', \
                        default = list(), \
                        type = pathexpandglob, \
                        required = True)
    parser.add_argument('-e', '--exclude', \
                        help = 'directories to exclude (supports expansion, globbing)', \
                        action = 'extend', \
                        default = list(), \
                        type = pathexpandglob)
    parser.add_argument('-d', '--dry-run', \
                        help = 'do not rename any files, just show the new name', \
                        action = 'store_true')
    if args == None:
        parsedargs = parser.parse_args()
    else:
        parsedargs = parser.parse_args(args)
    return parsedargs

def pathexpandglob(prepath):
    return glob.glob(os.path.expanduser(os.path.expandvars(prepath)))

def generatefilelist(include, exclude):
    filelist = set()
    for inc in include:
        for root, dirs, files in os.walk(inc):
            for e in exclude:
                dirs[:] = [d for d in dirs if not indirtree(os.path.join(root, d), e)]
            filelist.update([os.path.join(root, file) for file in files])
    return sorted(list(filelist))

def indirtree(child, parent):
    return (os.path.commonpath([child, parent])) == parent

def process(path):
    head, tail = os.path.split(path)
    return os.path.join(head, 'aaaa' + tail)

if __name__ == '__main__':
    agname()
