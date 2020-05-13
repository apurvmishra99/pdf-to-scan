#! /usr/bin/env python
# Copyright (c) 2020 apurv
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT


import os
import subprocess
from pathlib import Path
import click


def check_dependencies():
    # Check paths to ImageMagick and Ghostscript. 
    # Assuming it's kept in /usr/local/bin or /usr/bin in
    # Mac + Homebrew and linux distros.

    GHOSTSCRIPT_PATH = [os.path.exists(candidate) for candidate in ['/usr/local/bin/gs', '/usr/bin/gs']]
    CONVERT_PATH = [os.path.exists(candidate) for candidate in ['/usr/local/bin/convert', '/usr/bin/convert']]
    
    if not any(CONVERT_PATH):
        raise Exception('Check ImageMagick installation.')
    if not any(GHOSTSCRIPT_PATH):
        raise Exception('Check GhostScript installation.')
    
@click.command()
@click.argument(
    "file_name",
    type=click.Path(exists=True)
)
def convert(file_name):
    check_dependencies()
    try:
        orig_file = Path(file_name)
        output_path = Path(f"{file_name.split('.')[0]}_.pdf")
        output_path_final = Path(f"{file_name.split('.')[0]}.pdf")
        cmd = ['convert', '-density', '150', orig_file, '-colorspace', 'gray', '-linear-stretch', '3.5%x10%',
            '-blur', '0x0.5', '-attenuate', '0.25', '+noise', 'Gaussian', '-rotate', '0.5', output_path]
        subprocess.call(cmd, shell=False)
        cmd_gs = ['gs', '-dSAFER', '-dBATCH', '-dNOPAUSE', '-dNOCACHE', '-sDEVICE=pdfwrite', '-sColorConversionStrategy=LeaveColorUnchanged', '-dAutoFilterColorImages=true',
                '-dAutoFilterGrayImages=true', '-dDownsampleMonoImages=true', '-dDownsampleGrayImages=true', '-dDownsampleColorImages=true', f'-sOutputFile={output_path_final}', output_path]
        subprocess.call(cmd_gs, shell=False)
        click.secho("File processed and saved", fg="green")
    except Exception as e:
        print(e)
        
if __name__ == "__main__":
    convert()
