import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="pdf-to-scan-apurvmishra99",
    version="0.0.1",
    author="Apurv Mishra",
    author_email="me@apurvmishra.com",
    description="A small script to make your pdfs seem handscanned",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/apurvmishra99/pdf-to-scan",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
)