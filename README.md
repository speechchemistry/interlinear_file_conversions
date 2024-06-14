Scripts to convert interlinear glossed texts (IGT) into different formats

Script `tsv_to_flextext.py` converts from a TSV file that has two column, the first column is phrases in the vernacular language and the second is free translation in the analysis language (e.g. English). One common scenario that this script is meant to help with is when you have grammar paradigms listed in a spreadsheet and you want to do more analysis with Flex.    

## Requirements

You need Python version 3 and the following python modules:

- pandas
- xml.etree.ElementTree

## Installation

You can either clone this repository or just select the script you want and download the raw code (e.g. in the Chrome browser on Windows right click on the "Raw" github button, and click "Save link as..."). To use the script anywhere in your file directory you may need to add the script's location to your PATH environmental variable. 

## Examples

Say you have the following table:

|zhi|en|
|---|---|
|zying ma|the woman|
|sezying ma|the women|
|byo ma|the goat|
|byo ma|the goats|
|chi ma|the tree|
|chii ma|the trees|

This could be represented with tab separated values (TSV) in a file zhire_definite_determiners.tsv 

This is how you would convert it to a flextext file:

```
python3 tsv_to_flextext.py zhire_definite_determiners.tsv > zhire_definite_determiners.flextext
```
