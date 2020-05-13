#! /usr/bin/env python

import os
import subprocess
from pathlib import Path
import click


@click.command()
@click.argument(
    "file_name",
    type=click.Path(exists=True)
)
def convert(file_name):
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
    except Exception as e:
        print(e)
        
if __name__ == "__main__":
    convert()
