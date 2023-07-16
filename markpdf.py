#!/usr/bin/python3
# markpdf.py v1.1.0
# -----------------
#
# @zudsniper
import argparse
import re
import yaml
from jinja2 import Template
import markdown
import pdfkit
from loguru import logger
from colorama import Fore, Style

# ========= LOGGER ========= # 
# init logger 
logger.remove(0)

#logger.add(sys.stderr, format="{time:MMMM D, YYYY > HH:mm:ss!UTC-6} | [<level>{level}</level>]: {message}")

logger.add(sys.stderr, format="{time:HH:mm:ss} | [<level>{level}</level>]: {message}")

# ======= MAIN FUNC ======== # 

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', default='in.md', help='Input Markdown file (default: in.md)')
    parser.add_argument('-o', '--output', default='out.pdf', help='Output PDF file (default: out.pdf)')
    parser.add_argument('-m', '--metadata', help='Metadata YAML file')
    args = parser.parse_args()

    # Read the input file
    with open(args.input, 'r') as file:
        file_content = file.read()

    # Separate the YAML metadata from the rest of the Markdown content
    pattern = re.compile(r'^---\n(.+?)\n---\n(.+)', re.DOTALL)
    match = pattern.match(file_content)
    if match:
        yaml_metadata_str, markdown_content = match.groups()
        yaml_metadata = yaml.safe_load(yaml_metadata_str)
    else:
        logger.error(f"{Fore.RED}No metadata found in the markdown file.{Style.RESET_ALL}")

    # Render the template
    template = Template(markdown_content)
    rendered_markdown = template.render(yaml_metadata)

    # Convert markdown to HTML
    html = markdown.markdown(rendered_markdown)

    # Convert HTML to PDF
    pdfkit.from_string(html, args.output)
    logger.info(f"{Fore.GREEN}PDF has been successfully generated at {args.output}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
