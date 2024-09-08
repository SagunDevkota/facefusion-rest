
from flask import Flask,request, send_from_directory, abort
from globals import update_globals
from facefusion.core import conditional_process
import checklist
import tempfile
import os

app = Flask(__name__)
UPLOAD_DIRECTORY = "outputs/"

@app.route("/swap-face",methods=['post'])
def swap_face():
    files = request.files
    source = files.get('file_source',None)
    destination = files.get('file_destination',None)
    if(not (source and destination)):
        return {"error":"file_source and file_destination images not found"}, 400
    with tempfile.NamedTemporaryFile(delete=False,suffix=f'.{source.filename.split(".")[-1]}') as temp_source:
        source_path = temp_source.name
        source.save(temp_source)

    with tempfile.NamedTemporaryFile(delete=False,suffix=f'.{destination.filename.split(".")[-1]}') as temp_destination:
        destination_path = temp_destination.name
        destination.save(temp_destination)
    update_globals(source_path,destination_path)
    file_path = conditional_process()
    os.remove(source_path)
    os.remove(destination_path)
    return {"file_url":file_path[1:]}, 200

@app.route('/outputs/<filename>')
def serve_file(filename):
    file_path = os.path.join(UPLOAD_DIRECTORY, filename)
    if not os.path.isfile(file_path):
        abort(404)
    return send_from_directory(UPLOAD_DIRECTORY, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5500,debug=False)