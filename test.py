from search_engines import Google
from pathlib import Path
import requests


engine = Google()
results = engine.search("ASUG09LZAS pdf manual", pages=1)
links = results.links()

print(links)

for idx, link in enumerate(links):

    if ".pdf" in link:
        print(f'found pdf at {link}')
        response = requests.get(link, stream=True)
        filename = Path(f'downloads/res-{idx}.pdf')
        filename.write_bytes(response.content)
