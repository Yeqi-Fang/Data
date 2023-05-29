from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl
mpl.rcParams["font.family"] = "SimHei"

# Open the FITS file
hdulist = fits.open('glg_tte_b0_bn230512269_v00.fits')

# Access the data in the primary HDU (Header Data Unit)
data = hdulist[1].data

# Optionally, access the header information
header = hdulist[1].header
header