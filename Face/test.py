import httplib, urllib, base64

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'cd8b879914c442788232a9a6f8fe67bc',
}

params = urllib.urlencode({
})

personGroupId = 'xinchen'

body = {
        "name":'Xin Chen',
        "userData":"nothing"
        }

string = "/face/v1.0/persongroups/"+personGroupId
print (string)

try:
    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("PUT", string, str(body), headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
