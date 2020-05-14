#! /usr/bin/env python
# Copyright (c) 2020 apurv
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import os
import sys
import subprocess
from pathlib import Path
import click
import locale
import ghostscript
from wand.image import Image

    
@click.command()
@click.argument(
    "file_name",
    type=click.Path(exists=True)
)
def convert(file_name):
    try:
        orig_file = Path(file_name).resolve()
        output_path = Path(f"{file_name.split('.')[0]}_.pdf").resolve()
        output_path_temp = Path(f"{file_name.split('.')[0]}__.pdf").resolve()
        with Image(filename=str(orig_file), resolution=150) as img:
            img.transform_colorspace('gray')
            img.linear_stretch(black_point=0.035, white_point=0.1)
            img.blur(radius=0, sigma=0.5)
            img.noise(noise_type='gaussian', attenuate=0.25)
            img.rotate(0.5)
            img.save(filename=str(output_path))    
        
        cmd_gs = ['gs', '-dSAFER', '-dBATCH', '-dNOPAUSE', '-dNOCACHE', '-sDEVICE=pdfwrite', '-sColorConversionStrategy=LeaveColorUnchanged', '-dAutoFilterColorImages=true',
                '-dAutoFilterGrayImages=true', '-dDownsampleMonoImages=true', '-dDownsampleGrayImages=true', '-dDownsampleColorImages=true', f'-sOutputFile={str(output_path_temp)}', str(output_path)]
        encoding = locale.getpreferredencoding()
        cmd_gs = [a.encode(encoding) for a in cmd_gs]
        ghostscript.Ghostscript(*cmd_gs)
        os.remove(str(output_path_temp))
        click.secho("File processed and saved", fg="green")
    except Exception as e:
        print(e)
        
if __name__ == "__main__":
    convert()
