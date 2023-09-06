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
    for file in filelist:
        print(file)
    # - Get new filenames
    #   - Take args
    #   - Take filename input
    #   - Create new filename
    # - Apply new filenames
    #   - Run command to rename

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
                dirs[:] = [d for d in dirs if not inpath(os.path.join(root, d), e)]
            filelist.update([os.path.join(root, file) for file in files])
    return filelist

def inpath(patha, pathb):
    if (patha[:len(pathb)]) == pathb:
        return True
    return False

if __name__ == '__main__':
    agname()
