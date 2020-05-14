# PDFtoScan

PDFtoScan uses the idea implemented in [baicunko's](https://github.com/baicunko/scanyourpdf) website to make your PDFs look like they were scanned in a CLI-based app.

## Installation

```console
$ pip install pdf-to-scan
```


## Usage 

```console 
Usage: pdf-to-scan [OPTIONS] FILE_NAME

Options:
  --help  Show this message and exit.
```

## Example

```console
$ pdf-to-scan in.pdf
```

## Dependencies

The script requires `ghostscript` and `imagemagick` to run. 
These can be installed using,

### For Ubuntu
```console 
$ sudo apt-get install imagemagick
$ sudo apt-get install ghostscript
```

### For macOS
```console 
$ brew install imagemagick
$ brew install ghostscript
```

### For Windows
Check out this [link](https://imagemagick.org/script/download.php) for ImageMagick, and 
this [link](https://www.ghostscript.com/download/gsdnld.html) for ghostscript.

PDF support in ImageMagick might be disabled be default on your os/distro. To fix this, comment out this line in `/etc/ImageMagick-6/policy.xml`

`<policy domain="coder" rights="none" pattern="PDF" />`

Using `<!-- --->`
