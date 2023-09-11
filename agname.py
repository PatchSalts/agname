import argparse
import os.path
import glob
import importlib

def agname(args = None):
    # Parse the passed-in arguments
    parsedargs = parseargs(args)

    # Generate the list of files to process
    filelist = generatefilelist(parsedargs.include, set(parsedargs.exclude))

    # Import and prepare the processor
    processormodulename = parsedargs.processor
    processormodule = importlib.import_module('processor_modules.' + processormodulename)
    processorinit = getattr(processormodule, parsedargs.processor.capitalize())
    processorobject = processorinit()
    
    # Process the filenames and display the changes
    mapping = {file: processorobject.process(file) for file in filelist}
    currenthead = str()
    for map in mapping:
        if not parsedargs.dry_run:
            os.rename(map, mapping[map])
        oldhead, oldtail = os.path.split(map)
        if currenthead != oldhead:
            currenthead = oldhead
            print(currenthead)
        if map == mapping[map]:
            print('\t' + oldtail)
        else:
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
    parser.add_argument('-p', '--processor', \
                        help = 'which processor to use (e.g. "upper", "lower")', \
                        required = True)
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

if __name__ == '__main__':
    agname()
