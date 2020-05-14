import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="pdf-to-scan",
    version="0.0.3",
    author="Apurv Mishra",
    author_email="me@apurvmishra.com",
    description="A small script to make your pdfs seem handscanned",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/apurvmishra99/pdf-to-scan",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'ghostscript',
        'Wand'
    ],
    entry_points='''
        [console_scripts]
        pdf-to-scan=pdf_to_scan.make_pdfs_look_scanned:convert
    ''',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)