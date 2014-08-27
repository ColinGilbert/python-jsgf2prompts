python-jsgf2prompts
===================

A very quick and dirty modification to Arne Kohen's work at http://arne-koehn.de/projects/jsgfparser/, for creating prompts files from JSGF grammars.

Depends on Python 2.7 and PLY (Python Lex-Yacc, available at http://www.dabeaz.com/ply/)


This script _may_ not work with some valid .jsgf files, so I included a working example for your convenience. Recursion is not supported as I had no time to add it and would likely add way too many prompts to the file.

---

Modifications from original:

1 - The original script does not support the characters [] * + and outputs potentially misleading error messages. Added a conditional to prevent this.

2 - Made it write information pertaining the the training toolkit (silence words and file info) at the beginning and end of each sentence.

3 - Made it output to prompts.txt and fileids.txt instead of standard output.

For use with CMUSPhinx's training, as well as other toolkits which may require it. You'll also need a word dictionary file.

NOTE: Upon running this script, you may receive messages such as "WARNING: Token 'TOKEN_NAME' defined, but not used." These are completely safe to ignore. I would have suppressed them, but they belong to the PLY package itself.

---

Tested under Linux (Gentoo), but should work under any OS which supports Python (AKA: A bucket of sand with a broomhandle stuck in it could run this script...)

PS: This is my very first piece of FOSS. :D
