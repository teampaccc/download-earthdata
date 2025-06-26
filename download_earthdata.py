import requests
import earthaccess
import argparse
import os

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='Download earthdata to output_dir using short_name, start, end, and bounding_box.')

# Add the command line arguments
## Example short names for TEMPO data:
# TEMPO_NO2_L2
# TEMPO_HCHO_L2
# TEMPO_O3TOT_L2
# TEMPO_NO2_L3
# TEMPO_HCHO_L3
# TEMPO_O3TOT_L3
## To find the short name for the product you want, search the CMR (https://cmr.earthdata.nasa.gov/search/site/) or use the Earthdata Search tool.

parser.add_argument('--short_name', type=str, help='Short name of the data -- search the CMR for this')
parser.add_argument('--start', type=str, help='Start date (YYYY-MM-DD)')
parser.add_argument('--end', type=str, help='End date (YYYY-MM-DD)')
parser.add_argument('--bounding_box', default=(-134,20,-45,60), help='Bounding box')
parser.add_argument('--output_dir', type=str, help='Output directory')

# Parse the command line arguments
args = parser.parse_args()

# Access the values of the command line arguments
short_name = args.short_name
start = args.start
end = args.end
bounding_box = args.bounding_box
output_dir = args.output_dir

# code to download data using the provided arguments

# Log in to Earthdata
earthaccess.login()

# Search for data
results = earthaccess.search_data(
    short_name=short_name,
    # bounding_box=bounding_box,
    temporal=(start, end),
)

# Check if output_dir exists; if not, create it
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Download the data
files = earthaccess.download(results, output_dir, threads=16)

print(f'Downloaded {len(files)} files to {output_dir}')
