import random
from typing import List
import requests
from . import utils
from log import logger

api_logger = logger.getLogger(__name__)


class ImageBoard():
    def __init__(self, base_url: str, filter_id: str = "", api_key: str = "") -> None:
        self.base_url = str(base_url)
        self.filter_id = str(filter_id)
        self.api_key = str(api_key)

    def search_images(self, query: str):
        try:
            response = requests.get(f'{self.base_url}/api/v1/json/search/images{query}')
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as error:
            logger.error(error)
            return {"error_message": error}
    
    def random_image(self, tags: List[str] | str, filter_id: str = "", api_key: str = "") -> dict:
        """takes a list of tags or string of tags separated by commas to find images"""
        if isinstance(tags, list):
            tags = ','.join(tags)
        params = {
                "q": tags,
                "per_page": "1",
            }
        get_pages = self.search_images(utils.form_query(params))
        max_page = int(get_pages["total"])
        params["page"] = random.randint(1, max_page)
        if self.api_key:
            params["key"] = str(self.api_key)
        if self.filter_id:
            params["filter_id"] = str(self.filter_id)
        if api_key:
            params["key"] = str(api_key)
        if filter_id:
            params["filter_id"] = str(filter_id)
        return self.search_images(utils.form_query(params))

    def search_user(self, user_id: str):
        try:
            response = requests.get(f'{self.base_url}/api/v1/json/search/user/{user_id}')
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as error:
            api_logger.error(error)
            return {"error_message": error}

        

