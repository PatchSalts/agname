# Currently under initial development
Do not assume that anything here is ready for use

You may end up with a bunch of files with a bunch of "a"s prepended to their names

# agname
Rename files using arbitrary rules

# Usage
```
usage: agname.py [-h] [-v] -i INCLUDE [-e EXCLUDE] -p PROCESSOR [-a ARGUMENTS] [-d]

Rename files using arbitrary rules

options:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -i INCLUDE, --include INCLUDE
                        directories to include (supports expansion, globbing)
  -e EXCLUDE, --exclude EXCLUDE
                        directories to exclude (supports expansion, globbing)
  -p PROCESSOR, --processor PROCESSOR
                        which processor to use (e.g. "upper", "lower")
  -a ARGUMENTS, --arguments ARGUMENTS
                        arguments to pass to the processor, if it supports them
  -d, --dry-run         do not rename any files, just show the new name

This process may be destructive; please backup your files if they are important.
```

* Use `-i`/`--include` to add a directory you would like the program to recursively walk through and process/rename files
  * Supports system globbing/expansion
  * You may use multiple `-i`/`--include` options to include multiple folders
* Use `-e`/`--exclude` to add a directory you would like the program to recursively ignore when walking the directories
  * Supports system globbing/expansion
  * You may use multiple `-e`/`--exclude` options to exclude multiple folders
* Use `-p`/`--processor` to choose which module to use to process the filenames
  * Case-sensitive
  * Must refer to a module in the `processor_modules` folder
  * You can write your own!
    * Create a module with a class that extends `processor_modules.processor.Processor`
    * Place it in the `processor_modules` folder
    * The `process` function takes and returns fully qualified filepaths
    * You can use `os.path.split` and `os.path.join` to work with just the file names
* Use `-a`/`--arguments` to give arguments to the processor, if it accepts any arguments
* Use `-d`/`--dry-run` to prevent the program from actually renaming your files, allowing you to preview the changes it will make
  * Use this in combination with the `nochange` processor to preview the list of files that your `include` and `exclude` parameters would create