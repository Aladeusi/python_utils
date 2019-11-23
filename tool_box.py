
from flask import Response
import json
import base64
from flask import  send_from_directory


##
# Devops operations
##
# Http static file server : to serve files over http protocol
# flask only
def serve_file(file_dir_physical_path,file_name):
        # print(file_name)
        # print(file_dir_physical_path)
        return send_from_directory(file_dir_physical_path, filename=file_name, as_attachment=True)
    

##
# Devops operations
##


# response wrapper function to standardize http responses
def responsify(status,message,data={}):
    code = int(status)
    a_dict = {"data":data,"message":message,"code":code}
    try:
        return Response(json.dumps(a_dict), status=code, mimetype='application/json')
    except:
        return Response(str(a_dict), status=code, mimetype='application/json')

# write base64 encoded file to path
def writeBase64ToFile(base64_string, write_to,file_extension):
    imgdata = base64.b64decode(base64_string)
    filename = write_to+file_extension  # I assume you have a way of picking unique filenames
    with open(filename, 'wb') as f:
        f.write(imgdata)
    return filename
    # f gets closed when you exit the with statement
    # Now save the value of filename to your database






































