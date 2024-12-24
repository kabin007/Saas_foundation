import requests
from pathlib import Path


#function to download the static files
def download_to_local(url:str,dest_out_path:Path,parent_mkdir:bool=True):
        if not isinstance(dest_out_path,Path):
                raise ValueError(F"{dest_out_path} must be a valid pathlib.Path object")
        if parent_mkdir:
                dest_out_path.mkdir(parents=True,exist_ok=True)
    
        try:
            response=requests.get(url)
            response.raise_for_status()
            dest_out_path.write_bytes(response.content)
            return True
        except requests.RequestException as e:
               print(f'Failed to download {url} :{e}')
               return False