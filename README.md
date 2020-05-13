# PDFtoScan

PDFtoScan uses the idea implemented in [baicunko's](https://github.com/baicunko/scanyourpdf) website to make your PDFs look like they were scanned in a CLI-based app.

## Installation

```console
$ pip install pdf-to-scan
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

PDF support in ImageMagick might be disabled be default on your os/distro. To fix this, comment out this line in `/etc/ImageMagick-6/policy.xml`

`<policy domain="coder" rights="none" pattern="PDF" />`

Using `<!-- --->`