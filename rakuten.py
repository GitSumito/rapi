import os
import requests
import sys

def kick_rakten_api():
    
    REQUEST_URL = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706"
 
    # generate parameter
    search_param = set_api_parameter()
    response = requests.get(REQUEST_URL, search_param)
    result = response.json()
 
    print(result)
    item = result["Items"][0]["Item"]
    print(item["itemPrice"])
 
def set_api_parameter():
    app_id = os.getenv('RAKUTEN')
    args = sys.argv
    product = args[1]
    parameter = {
          "format"        : "json"
        , "keyword"       : [product]
        , "applicationId" : [app_id]
        , "availability"  : 1
        , "hits"          : 1
        , "sort"          : "+itemPrice"
        }
    return parameter
 
kick_rakten_api()
