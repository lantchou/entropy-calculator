# Shannon entropy calculator

Python script that calculates the conditional Shannon entropy for regular text files. A memory of N characters is assumed for the information source.

## Usage
The script expects:
- an integer argument N >= 0 that signifies the assumed memory size of the information source
- input text from stdin

##### Example
```console
python3 entropy.py 5 < input.txt
```
