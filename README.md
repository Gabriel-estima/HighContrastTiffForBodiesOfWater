
# Basic guide to use the archives in this repository (for debian/ubuntu users)

## Dependencies that should be installed before starting:

- some basic python dependencies: python3, pip (used to interpret and install packages for python)
- using pip, install "numpy" and "pillow": 'pip install pillow' and 'pip install numpy' (python packages used for image processing)
- dependency that modifies tiff/tif files metadata: 'sudo apt install libimage-exiftool-perl' (used to retrieve geographical metadata from base tiff images) 

#### Obs.: Extra file => "google-earth-pro" to verify that the resulting images were correctly rendered and have the right geographical metadata

## Using the scripts here provided to create high contrast images that differentiate "inundated" from "dry" land: 

1. After installing all dependencies, the "\bin" folder should be added to the PATH variable of the system. This will ensure that all scripts are accessible where needed.

2. To generate the most adequate high contrast images, the scripts should be run on the base images "VV - decibel gamma0" and "VH - decibel gamma0", that can be found on the download tab on the site: [Copernicus Browser](https://browser.dataspace.copernicus.eu) 

3. After installing the .zip archive that contains the base images in an empty folder, such as "\images\\*" present in the provided files, execute the "mergeGeoAll" script. This command extracts all the images from the .zip file in the directory, creates the high contrast image from the base images, recreates the geographical metadata information and, in the end, removes the base images that were extracted (unless the "-k" flag is used to keep the extracted files) 

#### Obs2.: Inside the base files lie two example images that are the expected result from the implemented algorithm with their respective base .zip files 

## Example of usage:
- Base images:
    - VV image: ![VV](https://github.com/Gabriel-estima/HighContrastTiffForBodiesOfWater/assets/117593727/bf001c9c-b8cb-44eb-92cb-96ace31912d6)
    - VH image: ![VH](https://github.com/Gabriel-estima/HighContrastTiffForBodiesOfWater/assets/117593727/0a6e3c8c-2cf8-499c-b371-5e10800d4b89)
- Expected result:

![RES](https://github.com/Gabriel-estima/HighContrastTiffForBodiesOfWater/assets/117593727/87ef56a0-4f00-42bd-8796-31ecee66b53c)



