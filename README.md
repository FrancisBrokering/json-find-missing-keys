# json-find-missing-keys

A tiny python script that indicates if a key is missing from one of the JSON files.

If a key is missing the script will print the missing key and the file name. If there are no key mismatches, the script will print "no missing keys!".

This script will work with any number of files but will only look top-level keys.

## Usage

```bash
./json-find-missing-keys.py samples/sample1.json samples/sample2.json samples/sample3.json
```

The program will exit with code 1 if there is an missing key.
