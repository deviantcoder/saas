import requests
from pathlib import Path


def download_to_local(url: str, out_path: Path, parent_mkdir: bool=True):
    """
    Downloads a file from the given URL and saves it to the specified local path.
    Args:
        url (str): The URL of the file to download.
        out_path (Path): The local file path where the downloaded file will be saved.
        parent_mkdir (bool, optional): If True, create parent directories if they do not exist. Defaults to True.
    Raises:
        ValueError: If out_path is not a valid pathlib.Path object.
    Returns:
        bool: True if the download was successful, False otherwise.
    """

    if not isinstance(out_path, Path):
        raise ValueError(f'{out_path} must be a valid pathlib.Path object')
    
    if parent_mkdir:
        out_path.parent.mkdir(parents=True, exist_ok=True)
    
    try:
        response = requests.get(url)
        response.raise_for_status()

        out_path.write_bytes(response.content)
        return True
    except requests.RequestException as e:
        print(f'Failed to download {url}: {e}')
        return False
