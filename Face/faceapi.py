# import http.client, urllib.request, urllib.parse, urllib.error, base64
import httplib, urllib, base64
import json
import io
import ast

''' to save in database: 
    personId, name, userData, personGroupId, persistedFaceId (use this to remove face added to person) 
'''


headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'cd8b879914c442788232a9a6f8fe67bc',
    'Process-Data': False
}


##### CREATE PERSON GROUP, GET PERSONID #####

def create_person(name, personGroupId):
    create_params = urllib.urlencode({
        'personGroupId': personGroupId
    })

    # CREATING PERSONGROUPID DOESN'T WORK FOR NOW
    string = "/face/v1.0/persongroups/"+personGroupId

    body = {
        "name":name,
        "userData":"nothing"
    }

    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("PUT", string, str(body), headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()

    body = {
        "name": name,
        "userData":"nothing"
    }

    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/face/v1.0/persongroups/{personGroupId}/persons?%s" % create_params, str(body), headers)
    response = conn.getresponse()
    data = response.read()
    conn.close()
    print('created person:\n'+str(data))

    json_data = json.loads(data)
    personId = json_data['personId']
    return personId

def add_face(image_url, personId, personGroupId):
    addface_params = urllib.urlencode({
        # Request parameters
        'personGroupId': personGroupId,
        'personId': personId

    })

    body = {
        "url": image_url ## USER'S SELFIE IMG_URL
    }

    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/face/v1.0/persongroups/{personGroupId}/persons/{personId}/persistedFaces?%s" % addface_params, str(body), headers)
    response = conn.getresponse()
    data = response.read()
    print('added face:\n'+str(data))
    conn.close()

    return True



##### CHECK IF PHOTO CONTAINS PERSON #####
# Use Detect to get faceIds of faces in each photo, call Verify.
# If verified, then use result from Detect to get location
def check_photo(image_url, personId, personGroupId):
    params = urllib.urlencode({
        # Request parameters
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
    })

    image_url = str(image_url)

    body = {
        'url': image_url
    }


    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/face/v1.0/detect?%s" % params, str(body), headers)
    response = conn.getresponse()
    data = response.read()
    print('checked photo:\n'+str(data))
    conn.close()

    json_data = json.loads(data)
    for entry in json_data:
        entry = str(entry)
        entry = ast.literal_eval(entry)
        print type(entry)
        faceId = str((entry['faceId']))
        if check_face(faceId, personId, personGroupId):
            coords = entry['faceRectangle']
            return (coords['top'], coords['left'], coords['width'], coords['height'])
    return None

def check_face(faceId, personId, personGroupId):
    params = urllib.urlencode({
    })

    faceId = str(faceId)
    personId = str(personId)
    personGroupId = str(personGroupId)

    body = {
        'faceId': faceId,
        'personId': personId,
        'personGroupId': personGroupId
    }

    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/face/v1.0/verify?%s" % params, str(body), headers)
    response = conn.getresponse()
    data = response.read()
    print('checked face:\n'+str(data))
    conn.close()

    json_data = json.loads(data)
    if json_data['isIdentical']:
        print ('true!')
        return True
    else:
        print ('false!')
        return False

def main():

    create_person('Jie Xun', 'jiexun')
    # add_face( , 'cd09435a-c73b-4df2-888a-31af70a8a2f1', 'jiarui')

    # name = 'Vladimr Putin'
    # personGroupId = 'putin'
    # selfie = 'http://i.telegraph.co.uk/multimedia/archive/03463/putin_3463140k.jpg'
    # photo = 'https://jafrianews.files.wordpress.com/2012/05/russian-president-putin-with-vladimir-putin-may-7-2012.jpg'
    # photo = 'http://i.telegraph.co.uk/multimedia/archive/03463/putin_3463140k.jpg'


    # urllib.urlretrieve(photo, 'photo.jpg')
    # with open("photo.jpg", "rb") as imageFile:
    #     f = imageFile.read()
    #     b = bytearray(f)

    # possible_coords = check_photo(photo, 'b00c6a39-7807-4cf2-9a04-6b41f2efcf18', personGroupId)
    # print (possible_coords)
    # print ('done!')

if __name__ == '__main__':
    main()
    #check_face('30d72dba-7049-485b-9421-5a64255d195c', 'b00c6a39-7807-4cf2-9a04-6b41f2efcf18', 'putin')
