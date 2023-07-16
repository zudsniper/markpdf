#!/usr/bin/python3
# markpdf.py v1.3.3
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
import sys

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
    parser.add_argument('--darkmode', action='store_true', help='Output a "dark mode" version of the document')
    parser.add_argument('-f', '--font', default='JetBrains Mono', help='Font to use in the PDF document')
    args = parser.parse_args()

    # Read the input file
    with open(args.input, 'r') as file:
        file_content = file.read()

    # Separate the YAML metadata from the rest of the Markdown content
    pattern = re.compile(r'^---\\n(.+?)\\n---\\n(.+)', re.DOTALL)
    match = pattern.match(file_content)
    if match:
        yaml_metadata_str, markdown_content = match.groups()
        yaml_metadata = yaml.safe_load(yaml_metadata_str)
    else:
        logger.warning(f"{Fore.YELLOW}No metadata found in the markdown file.{Style.RESET_ALL}")
        markdown_content = file_content  # Set markdown_content to the entire file content if no metadata is found
        yaml_metadata = {}  # Set yaml_metadata to an empty dictionary if no metadata is found

    # If a metadata file is provided, use it as the yaml_metadata
    if args.metadata:
        logger.info(f"{Fore.WHITE}metadata YAML file provided, reading values from it.{Style.RESET_ALL}")
        with open(args.metadata, 'r') as file:
            yaml_metadata = yaml.safe_load(file)

    # Render the template
    for key, value in yaml_metadata.items():
        if value is None:
            logger.warning(f"{Fore.YELLOW}No value found for variable '{key}'. Setting it to '____________'.{Style.RESET_ALL}")
            yaml_metadata[key] = '____________'
    template = Template(markdown_content)
    rendered_markdown = template.render(yaml_metadata)

    # Convert markdown to HTML
    html = markdown.markdown(rendered_markdown)

    # If dark mode is enabled, add a CSS style for dark mode
    if args.darkmode:
        html = f"<style>body,html {{ background-color: #2b2b2b; color: #a9b7c6; font-family: '{args.font}'; }}</style>{html}"
        #html = f"<style>body {{ background-color: #2b2b2b; color: #a9b7c6; }}</style>{html}"

    # Convert HTML to PDF
    pdfkit.from_string(html, args.output)
    logger.info(f"{Fore.GREEN}PDF has been successfully generated at {args.output}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
