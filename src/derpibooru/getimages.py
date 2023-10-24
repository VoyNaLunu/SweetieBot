from typing import List
import requests

URL = "Https://derpibooru.org"


class GetImages():
    def __init__(self, base_url: str = URL) -> None:
        self.base_url = base_url

    def by_tags(self, tags: List[str]):
        base_url = self.base_url
        if not base_url:
            base_url = URL
        query = ','.join(tags)
        response = requests.get(f'{base_url}/api/v1/json/search/images?q={query}')
        return response.json()

