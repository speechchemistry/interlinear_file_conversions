import pandas as pd
import xml.etree.ElementTree as ET
import os
import sys
import argparse

def tsv_to_flextext(tsv_path):

    # Extract the title from the filename
    title = os.path.splitext(os.path.basename(tsv_path))[0]

    # Read the TSV file into a DataFrame, including the header
    df = pd.read_csv(tsv_path, delimiter='\t')
    
    # Extract the ISO language codes from the first row (header)
    src_lang, trg_lang = df.columns[0], df.columns[1]
    
    # Create the root of the XML tree
    document = ET.Element('document')
    interlinear_text = ET.SubElement(document, 'interlinear-text')
    
    # Add the title
    title_item = ET.SubElement(interlinear_text, 'item', type="title", lang="en")
    title_item.text = title
    
    # Add paragraphs and phrases - one for each line in the TSV file
    paragraphs = ET.SubElement(interlinear_text, 'paragraphs')
    
    for idx, row in df.iterrows():
        paragraph = ET.SubElement(paragraphs, 'paragraph')
        phrases = ET.SubElement(paragraph, 'phrases')
        phrase = ET.SubElement(phrases, 'phrase')
        
        # Segment number
        segnum = ET.SubElement(phrase, 'item', type="segnum", lang="en")
        segnum.text = str(idx + 1)
        
        # Source text
        txt = ET.SubElement(phrase, 'item', type="txt", lang=src_lang)
        txt.text = row[0]
        
        # Gloss/Translation
        gls = ET.SubElement(phrase, 'item', type="gls", lang=trg_lang)
        gls.text = row[1]
        
        # Empty words element because we don't yet have word glosses
        words = ET.SubElement(phrase, 'words')
    
    # Add writing system languages
    languages = ET.SubElement(interlinear_text, 'languages')
    language_src = ET.SubElement(languages, 'language', lang=src_lang)
    language_trg = ET.SubElement(languages, 'language', lang=trg_lang)
    
    # Create the tree and write to standard output
    tree = ET.ElementTree(document)
    ET.indent(tree)
    tree.write(sys.stdout, encoding='unicode', xml_declaration=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert a TSV file to FlexText format and output to standard out.')
    parser.add_argument('tsv_path', help='Path to the input TSV file')
    args = parser.parse_args()
    tsv_to_flextext(args.tsv_path)
