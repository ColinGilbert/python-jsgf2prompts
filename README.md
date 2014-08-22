python-jsgf2prompts
===================

A very quick and dirty modification to Arne Kohen's work at http://arne-koehn.de/projects/jsgfparser/, for creating prompts files from JSGF grammars. THANK YOU, ARNE! :)

Depends on Python 2.7 and PLY (tested with version 3.4, but others should work as well.)
Porting to Python 3.* should be trivial, but I am a very busy man.

This script _may_ not work with some valid .jsgf files, so I included a working example for your convenience. Recursion is not supported as I had no time to add it and would likely add way too many prompts to the file.

---

Modifications from original:

1 - The original script does not support the characters [] * + and outputs potentially misleading error messages. Added a conditional to prevent this.

2 - Made it write <sil> </sil> at the beginning and end of each sentence.

3 - Made it output to a prompts file instead of standard output.

---

Tested under Linux (Gentoo) but should work under any OS which supports Python (AKA: A bucket of sand with a broomhandle stuck in it could run this script...)

PS: This is my very first piece of FOSS. :D
