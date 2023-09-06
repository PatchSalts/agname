# agname
Rename files using arbitrary rules

# Usage
```
usage: agname.py [-h] [-v] -i INCLUDE [-e EXCLUDE] [-d]

Rename files using arbitrary rules

options:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -i INCLUDE, --include INCLUDE
                        directories to include (supports expansion, globbing)
  -e EXCLUDE, --exclude EXCLUDE
                        directories to exclude (supports expansion, globbing)
  -d, --dry-run         do not rename any files, just show the new name

This process may be destructive; please backup your files if they are important.
```

* Use `-i`/`--include` to add a directory you would like the program to recursively walk through and process/rename files
  * Supports system globbing/expansion
  * You may use multiple `-i`/`--include` options to include multiple folders
* Use `-e`/`--exclude` to add a directory you would like the program to recursively ignore when walking the directories
  * Supports system globbing/expansion
  * You may use multiple `-e`/`--exclude` options to exclude multiple folders
* Use `-d`/`--dry-run` to stop the program before it will actually rename your files, allowing you to preview the changes it will make
