import random
import requests
from typing import Dict, List
from philomena.exceptions import PhilomenaAPIException
from philomena.endpoints import endpoints, Endpoint

def _form_params(
        filter_id: str=None,
        key: str=None,
        page: str=None,
        per_page: str=None,
        q: str=None,
        sd: str=None,
        sf: str = None) -> Dict | None:
    """returns Philomina compatible params dict if params are provided"""
    params = {}
    for param, value in locals().items(): # not sure if this is a good way to do this... oh well
        if value:
            params[param] = value
    if params["params"]:
        params.pop("params")
    return params if params else None

def _format_tags(tags: List[str] | str):
    """turns tags passed as list into single params compatible string"""
    if isinstance(tags, list):
        return ','.join(tags)
    if isinstance(tags, str):
        return tags
    raise ValueError("tags must be a list of strings or a string")

class ImageBoard():
    """Philamina API Wrapper"""
    def __init__(self, base_url: str, filter_id: str = None, api_key: str = None) -> None:
        self.base_url = base_url
        self.filter_id = filter_id
        self._api_key = api_key

    def _req(self, method: str, endpoint: str, params: Dict = None, data: Dict = None) -> dict:
        """base request method"""
        url = f'{self.base_url}{endpoint}'
        try:
            response = requests.request(method=method, url=url, params=params, data=data, timeout=10)
            return response.json()
        except requests.exceptions.RequestException as error:
            raise PhilomenaAPIException(f"Request to {self.__class__.__name__} failed with following error:\n {error}") from error

    def _get(self, endpoint: str, params: Dict = None) -> dict:
        """get request method"""
        return self._req(method="GET", endpoint=endpoint, params=params)

    def _post(self, endpoint: str, params: Dict = None, data: Dict = None) -> dict:
        """post request method"""
        return self._req(method="POST", endpoint=endpoint, params=params, data=data)

    def search_images(
            self,
            tags: List[str] | str,
            endpoint: Endpoint=endpoints["search_images"],
            image_count=1,
            page=1) -> dict:
        """returns images by tags in json format"""
        tags = _format_tags(tags)
        params = _form_params(filter_id=self.filter_id, key=self._api_key, page=page, per_page=image_count, q=tags)
        return self._get(endpoint=endpoint.path, params=params)

    def random_image(self, tags: List[str] | str):
        """returns random image by tag"""
        fetched_data = self.search_images(tags=tags)
        max_pages = int(fetched_data["total"])
        return self.search_images(tags=tags, page=random.randint(1, max_pages))

