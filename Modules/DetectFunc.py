import pandas as pd 
import xml.etree.ElementTree as Xet
import Modules.Functions as Func


#Start Detection 

def getHostDetections(DRESPONSEXML, ScanDateforSQL):

    tree = Xet.parse(DRESPONSEXML)
    root = tree.getroot()
    Data = root.find("RESPONSE")
    Hosts  = Data.find("HOST_LIST")
    rows=[]

    index = 0
    for host in Hosts:
            print("Detactions: creating host ",str(index))
            id = Func.tryToGetAttribute(host,"ID")
            ip_address = Func.tryToGetAttribute(host,"IP")
            tracking = Func.tryToGetAttribute(host,"TRACKING_METHOD")
            network_id = Func.tryToGetAttribute(host,"NETWORK_ID")
            operating_system = Func.tryToGetAttribute(host,"OS")
            dns = Func.tryToGetAttribute(host,"DNS")
            dnsObj1 =  host.find("DNS_DATA/HOSTNAME")
            hostname = Func.tryToGetAttribute(dnsObj1,"HOSTNAME")
            dnsObj2 =  host.find("DNS_DATA/DOMAIN")
            domin = Func.tryToGetAttribute(dnsObj2,"DOMAIN")
            dnsObj3 =  host.find("DNS_DATA/FQDN")
            fqdn = Func.tryToGetAttribute(dnsObj3,"FQDN")
            qg_hostId = Func.tryToGetAttribute(host,"QG_HOSTID")
            last_scan_datetime = Func.tryToGetAttribute(host,"LAST_SCAN_DATETIME")
            last_vm_scan_date = Func.tryToGetAttribute(host,"LAST_VM_SCANNED_DATE")
            last_vm_auth_scan_date = Func.tryToGetAttribute(host,"LAST_VM_AUTH_SCANNED_DATE")
            last_pc_scan_date = Func.tryToGetAttribute(host,"LAST_PC_SCANNED_DATE")
            
            #
            try:
                detections =  host.findall("DETECTION_LIST/DETECTION")
            except:
                detections = False
                print("failed to get detections for host " + id + " With index " + index )

            if(detections):
                for detection in detections:
                    print("Detactions: procecing host detection ",str(index))
                    qid= Func.tryToGetAttribute(detection,"QID")
                    type = Func.tryToGetAttribute(detection,"TYPE")
                    severity = Func.tryToGetAttribute(detection,"SEVERITY")
                    ssl = Func.tryToGetAttribute(detection,"SSL")
                    status = Func.tryToGetAttribute(detection,"STATUS")
                    first_found_datetime = Func.tryToGetAttribute(detection,"FIRST_FOUND_DATETIME")
                    last_fond_datetime = Func.tryToGetAttribute(detection,"LAST_FOUND_DATETIME")
                    times_found = Func.tryToGetAttribute(detection,"TIMES_FOUND")
                    last_test_datetime = Func.tryToGetAttribute(detection,"LAST_TEST_DATETIME")
                    last_update_datetime = Func.tryToGetAttribute(detection,"LAST_UPDATE_DATETIME")
                    last_fixed_datetime = Func.tryToGetAttribute(detection,"LAST_FIXED_DATETIME")
                    is_ignored = Func.tryToGetAttribute(detection,"IS_IGNORED")
                    is_disabed = Func.tryToGetAttribute(detection,"IS_DISABLED")
                    last_processsed_datetime = Func.tryToGetAttribute(detection,"LAST_PROCESSED_DATETIME")
                    rows.append ({
                        'SCANDATEFORSQL' : ScanDateforSQL,
                        'HOST_ID': id,
                        'IP_ADDRESS': ip_address,
                        'TRACKING_METHOD': tracking,
                        'NETWORK_ID': network_id,
                        'OPERATING_SYSTEM': operating_system,
                        'DNS_NAME': dns,
                        'NETBIOS_NAME': hostname,
                        'DOMAIN': domin,
                        'QG_HOSTID': qg_hostId,
                        'LAST_SCAN_DATETIME': last_scan_datetime,
                        'LAST_VM_SCANNED_DATE': last_vm_scan_date,
                        'LAST_VM_AUTH_SCANNED_DATE': last_vm_auth_scan_date,
                        'LAST_PC_SCANNED_DATE' : last_pc_scan_date,
                        'QID' : qid,
                        'TYPE' :type ,
                        'FQDN' : fqdn	,
                        'SSL'	: ssl,
                        'STATUS' : status,
                        'SEVERITY' : severity,
                        'FIRST_FOUND_DATETIME' : first_found_datetime,
                        'LAST_FOUND_DATETIME' : last_fond_datetime,
                        'LAST_TEST_DATETIME' : last_test_datetime,
                        'LAST_UPDATE_DATETIME' : last_update_datetime,
                        'LAST_FIXED_DATETIME' : last_fixed_datetime,
                        'IGNORED' : is_ignored,
                        'DISABLED' : is_disabed,
                        'TIMES_FOUND' : times_found,
                        'LAST_PROCESSED_DATETIME': last_processsed_datetime
                            })
                index+=1
            else:
                print("no detections found for host " + str(id))
                index+=1

    return rows

                
             




