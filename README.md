# agname
Rename files using arbitrary rules

# Usage
```
usage: agname.py [-h] [-v] -i INCLUDE [-e EXCLUDE]

Rename files using arbitrary rules

options:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -i INCLUDE, --include INCLUDE
                        directories to include (supports expansion, globbing)
  -e EXCLUDE, --exclude EXCLUDE
                        directories to exclude (supports expansion, globbing)

This process may be destructive; please backup your files if they are important.
```

* Use `-i`/`--include` to add a directory you would like the program to recursively walk through and process/rename files
    * Supports system globbing/expansion
    * You may use multiple `-i`/`--include` options to add multiple folders
    * It is not guaranteed that your directories or the files within will be processed in any particular order
* Use `-e`/`--exclude` to add a directory you would like the program to recursively ignore when walking the directories
    * Supports system globbing/expansion
    * You may use multiple `-i`/`--include` options to add multiple folders