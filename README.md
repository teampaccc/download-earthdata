This script can be used to download data from NASA Earthdata  using the [`earthaccess`](https://github.com/nsidc/earthaccess) Python client. You can specify a dataset short name, date range, lat-lon range, and output directory to retrieve relevant files.

## Usage example

```bash
python download_earthdata.py \
  --short_name TEMPO_NO2_L2 \
  --start 2024-05-01 \
  --end 2024-05-10 \
  --bounding_box (-134,20,-45,60) \ 
  --output_dir ./data
```


## Requirements

Install dependencies:

```bash
pip install earthaccess requests
```

## Authentication
The script uses earthaccess.login() which will prompt you for credentials on first use, or use environment variables / keychain if already configured.