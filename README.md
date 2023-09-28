# Qualys Export QIDs to Blob Storage 

Qualys HostAsset and VM API parser
Parse the Detection and Hostasset API output

## Requirments

1. python 3.8+
2. [pip package manager](https://pip.pypa.io/en/stable/installation/)

### Install packages with pip: -r requirements.txt
pip install -r requirements.txt
### Edit config
Rename the file config.xml.sample to config.xml
Change the **BASE_URL** to the correct platform. See [platform-identification](https://www.qualys.com/platform-identification/)
Change the **USERNAME** and **PASSWORD** information

SQL Will work, but the driver needs to be detected by the user.
In most cases please just keep the flag **USE_SQL** set to ***false***

## Release Notes
1.0.0 - Initial release;
