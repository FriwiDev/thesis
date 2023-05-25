# Testbed Images
This folder is dedicated to creating and managing LXC/LXD images for our testbed solution.
The `setup.sh` script can be used to install LXC and LXD, but will be invoked automatically by the scripts below.
All scripts require root privileges on the build system.

### Creating images
To build one specific component, use `./build_X.sh`, replacing `X` with the component name.
To build all components, use `./build_all.sh`.
The scripts will build and install the image locally, as well as export it to the `export` folder in `.tar.gz` format.
They will pack the python packages from the `src` folder into images, alongside their python and system dependencies.

### Import images
Place all images you wish to import in the `export` folder.
Run `./import_all.sh` to import the provided images in the local LXC/LXD environment.
Selective importing is supported by providing/not providing a specific file.
The script will inform the user about which images were provided and imported successfully.
