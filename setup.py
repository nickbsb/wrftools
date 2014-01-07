from distutils.core import setup
from distutils.extension import Extension

setup(
      name = "wrftools",
      version = "1.0",
      author = "Kelton Halbert",
      author_email = "keltonhalbert@ou.edu",
      description = ("Functions for post processing WRF data"),
      license = "GPL V2",
      url = "https://github.com/keltonhalbert/wrftools",
      packages=['wrftools'],
      classifiers=["Development Status :: 3 - Alpha"]
      )