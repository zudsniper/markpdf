from setuptools import setup, find_packages

setup(
    name="markpdf",
    version="0.1.0",
    author="Jason McElhenney",
    author_email="me@zod.tf",
    description="A tool to populate markdown files with YAML metadata and convert to PDF",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://gh.zod.tf/markpdf",
    packages=find_packages(),
    install_requires=[
        "pyyaml",
        "jinja2",
        "markdown",
        "pdfkit",
        "loguru",
        "colorama"
    ],
    entry_points={
        'console_scripts': [
            'markpdf=markpdf:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)
