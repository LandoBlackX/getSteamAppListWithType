import json
import os
from pathlib import Path

input_file = Path(os.path.dirname(os.path.dirname(__file__))) / 'data' / 'output.json'
output_file = Path(os.path.dirname(os.path.dirname(__file__))) / 'data' / 'Listwithnogame.json'

with open(input_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

filtered_data = {k: v for k, v in data.items() if v not in ["game", "demo","video","movie","advertising","mod"]}

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(filtered_data, f, ensure_ascii=False, indent=4)
