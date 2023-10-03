import requests
import base64
from datetime import timedelta, date
import re

def filter_xml_chars(text):
    # Define a regular expression pattern to match special XML characters
    pattern = re.compile(r'[&<>"\']')
    # Use the sub() method to replace the matched characters with their escaped versions
    text = pattern.sub(lambda m: {'&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&apos;'}[m.group(0)], text)
    return text

def tryToGetAttribute(Object,inputString):
    try:
        output = Object.find(inputString).text
    except:
        output = "Null"
    return output

def tryToGetObj(Object,inputString):
    try:
        output = Object.find(inputString)
    except:
        output = "Null"
    return output

def getToken(USERNAME,PASSWORD):
    AuthStringRaw = USERNAME+":"+PASSWORD
    base64_bytes = AuthStringRaw.encode("ascii")
    authtoken = base64.b64encode(base64_bytes)
    base64_authtoken = authtoken.decode("ascii")
    return base64_authtoken

def getSearchTime(delta):
    today = date.today()
    lastweek_date = today - timedelta(days=delta)
    DateForSearch=lastweek_date.strftime("%Y-%m-%dT%H:%M:%SZ")
    return DateForSearch

def getStempTime():
    today = date.today()
    dt_string = today.strftime("%Y-%m-%dT%H:%M:%SZ")
    return dt_string


##Override - Delete - remove the False=True option
def getXmlHeader(USERNAME={},PASSWORD={}):
    headers = {
    "Content-Type": "application/xml",
    "Accept": "application/xml",
    "X-Requested-With": "QualysPostman",
    "Authorization": "Basic "+getToken(USERNAME,PASSWORD)
    }
    return headers



def getHeader(USERNAME,PASSWORD):
    headers = {
    "X-Requested-With": "QualysPostman",
    "Authorization": "Basic "+getToken(USERNAME,PASSWORD)
    }
    return headers



#Used to Post requests
def postRequest(URL,payload,headers,files=[]):
    print("POSTING to "+ URL)
    try:
        response = requests.request("POST", URL, headers=headers, data=payload, files=files)
    except:
        print("Failed to send request to API")
        return str(response.status_code)
    else:
        return  response


def getRequest(URL,payload,headers,files=[]):
    print("POSTING to "+ URL)
    try:
        response = requests.request("GET", URL, headers=headers, data=payload, files=files)
    except:
        print("Failed to send request to API")
    else:
        return  response


