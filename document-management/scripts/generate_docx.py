import argparse
import zipfile
import json
import os
import sys
from xml.sax.saxutils import escape

def create_element_raw(style, text):
    if style == "Heading1":
        style_xml = '<w:pStyle w:val="Heading1"/>'
    elif style == "Heading2":
        style_xml = '<w:pStyle w:val="Heading2"/>'
    else:
        style_xml = ''
    escaped_text = escape(str(text))
    return f'<w:p><w:pPr>{style_xml}</w:pPr><w:r><w:t>{escaped_text}</w:t></w:r></w:p>'

def generate_document(template_path, output_path, content_json_path):
    with open(content_json_path, 'r') as f:
        content_data = json.load(f)
        
    if not isinstance(content_data, list):
        print("Error: content JSON must be a list of objects containing 'style' and 'text'.")
        sys.exit(1)
        
    with zipfile.ZipFile(template_path, 'r') as zin:
        with zipfile.ZipFile(output_path, 'w') as zout:
            for item in zin.infolist():
                content = zin.read(item.filename)
                
                # Fix the content types signature to valid DOCX
                if item.filename == '[Content_Types].xml':
                    content_str = content.decode('utf-8')
                    content_str = content_str.replace(
                        'application/vnd.openxmlformats-officedocument.wordprocessingml.template.main+xml',
                        'application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml'
                    )
                    content = content_str.encode('utf-8')
                    
                # Inject paragraphs into the Document body
                elif item.filename == 'word/document.xml':
                    content_str = content.decode('utf-8')
                    sect_pr_idx = content_str.find('<w:sectPr')
                    start_marker = '<w:t>Heading One</w:t>'
                    marker_idx = content_str.find(start_marker)
                    
                    if marker_idx != -1:
                        p_start_idx = content_str.rfind('<w:p ', 0, marker_idx)
                        p_start_idx2 = content_str.rfind('<w:p>', 0, marker_idx)
                        actual_p_start = max(p_start_idx, p_start_idx2)
                        
                        if actual_p_start != -1 and sect_pr_idx != -1:
                            new_paragraphs = "".join([create_element_raw(b.get("style", "Normal"), b.get("text", "")) for b in content_data])
                            content_str = content_str[:actual_p_start] + new_paragraphs + content_str[sect_pr_idx:]
                            content = content_str.encode('utf-8')
                            
                zout.writestr(item, content)

    print(f"Document successfully created at {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Word Docx from Delta Template")
    parser.add_argument("--template", required=True, help="Path to delta-word-template.dotx")
    parser.add_argument("--output", required=True, help="Path for generated .docx file")
    parser.add_argument("--content", required=True, help="Path to JSON file containing the content blocks")
    args = parser.parse_args()
    
    generate_document(args.template, args.output, args.content)
