"""
Gets the names file from 'github.com/karpathy/makemore' repo.
"""
from pathlib import Path
import requests

r = requests.get(
    "https://github.com/karpathy/makemore/blob/master/names.txt?raw=true", timeout=60)

FILE_PATH = Path("./data")
FILE_NAME = "names.txt"

FILE_PATH.mkdir(exist_ok=True, parents=True)


with open(FILE_PATH/FILE_NAME, 'wb') as f:
    f.write(r.content)
