# ♛ `markpdf.py` ♕
_easily convert markdown to pdf -- **including variables** provided in the header of the file or within a separate provided `metadata.yaml` file_  

## Installation

### Administrator Privileged Dependency 
🔴 **`wkhtmltopdf` is REQUIRED**  
Installation process varies based on OS. 
- Linux (debian based)
`sudo apt-get install wkhtmltopdf -y`  

- MacOS 
`brew install wkhtmltopdf`  

- Windows
idk use WSL  
nah probably just `scoop get wkhtmltopdf`  

### Other Requirements
- `Python3.9` or greater

- All `pip` package dependencies
```sh
$ python3 -m pip install -r requirements.txt
```

from here, you should be able to run the script via 
```sh
$ python3 markpdf.py -o <output_pdf_name> -i <input_markdown_name> [-m <metadata_yaml_file>] 
```

> _I don't see why this is actually required..._  
  
After this, install `setuptools`  
```sh
$ python3 -m pip install setuptools
```

---  

## Usage

To place variables into the your pdf, use this format: 
```
{{ variable_name }}
```
variables with this name and **yaml metadata counterparts of the same name** will be populated with their values when the script generates a pdf. 

---  

### cool