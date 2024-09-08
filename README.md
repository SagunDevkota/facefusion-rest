FaceFusion - REST
=================

> Next generation face swapper.


Installation
------------

1. Clone the repository
```
git clone https://github.com/SagunDevkota/facefusion-rest.git
```

2. Install requirements
```
pip install -r requirements.txt
```

3. Run REST Server
```
python3 app.py
```
for guardio UI follow installation guide at [facefusion](https://github.com/facefusion/facefusion).

## Usage
```curl
curl --location --request POST 'http://127.0.0.1:5500/swap-face' \
--form 'file_source=@"path_to_source_image"' \
--form 'file_destination=@"path_to_target_image"'
```
