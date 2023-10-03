import pandas as pd 
import Modules.Functions as Func
import Config as Conf
import Modules.DetectFunc as Detect
from azure.storage.blob import BlockBlobService


####################Start######################
#This is hostasset API part                   #
###############################################


#get token
BASE = Conf.base
AzureBlob = Conf.StorageAccount
BlobKey = Conf.StorageKey
Container = Conf.Container
BlobName = Conf.BlobName


###################Start######################
#This is detection API part                   #
##############################################
URL = "/api/2.0/fo/asset/host/vm/detection/"
REQUEST_URL = Conf.base+URL
cols = ['SCANDATEFORSQL','HOST_ID','IP_ADDRESS','TRACKING_METHOD','NETWORK_ID','OPERATING_SYSTEM','DNS_NAME',\
'NETBIOS_NAME','DOMAIN','QG_HOSTID','LAST_SCAN_DATETIME','LAST_VM_SCANNED_DATE','LAST_VM_AUTH_SCANNED_DATE','LAST_PC_SCANNED_DATE','QID','TYPE',\
'FQDN','SSL','STATUS','SEVERITY','FIRST_FOUND_DATETIME','LAST_FOUND_DATETIME','LAST_TEST_DATETIME','LAST_UPDATE_DATETIME',\
'LAST_FIXED_DATETIME','IGNORED','DISABLED','TIMES_FOUND','LAST_PROCESSED_DATETIME']

payload={'action': 'list',
'status': 'New,Active,Fixed,Re-Opened',
'detection_updated_since': Conf.DateForSearch,
'show_asset_id':1,
'output_format': 'XML',
'truncation_limit': '1000000'}

header = Func.getHeader(Conf.USERNAME,Conf.PASSWORD)
response = Func.postRequest(REQUEST_URL,payload,header)

if (response.ok != True):
  print("Failed to get response from API")


with open(Conf.DRESPONSEXML, 'w', encoding="utf-8") as f:
    f.write(response.text)
    f.close()

rows = []
rows = Detect.getHostDetections(Conf.DRESPONSEXML, Conf.ScanDateforSQL)

df = pd.DataFrame(rows, columns=cols)

output =  df.to_csv(Conf.DETECTIONS,index=False, encoding="utf-8")

########
# Create a block blob service object
block_blob_service = BlockBlobService(AzureBlob, BlobKey)

block_blob_service.create_blob_from_path(Container, BlobName, Conf.DETECTIONS)