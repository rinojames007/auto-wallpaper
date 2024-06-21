import random
import requests
from requests.exceptions import ConnectionError, Timeout, HTTPError
from cryptography.fernet import Fernet 
import logging

log_file = "wall.log"
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)s [%(levelname)s]: %(message)s',
                    handlers=[
                    logging.StreamHandler()
                    ])
logger = logging.getLogger("DailyWallpaper")

class DailyWallpaper:
    with open("secret.key", "rb") as file:
        key = file.read()

    fernetobj = Fernet(key)
    with open("key.txt", "rb") as encrypted_file:
        encrypted_access_key = encrypted_file.read()

    ACCESS_KEY: str = fernetobj.decrypt(encrypted_access_key).decode("utf-8")
    URL: str = "https://api.unsplash.com/search/photos"

    TOPICS: list[str] = [
        "Nature", "Wallpapers", "Architecture", "Interiors",
        "Travel", "Animals", "Architecture & interior",
        "Relax"
    ]

    HEADERS: dict[str, str] = {"Authorization": f"Client-ID {ACCESS_KEY}"}

    @classmethod
    def fetch_response(
        cls, url=URL, empty_request=False
    ) -> requests.Response | None:

        request_params: dict[str, str | int] = {
            "query": random.choice(cls.TOPICS),
            "per_page": 1,
            "page": random.randint(1, 100)
        }

        try:
            if empty_request:
                response: requests.Response = requests.get(url)
            else:
                response: requests.Response = requests.get(
                    url, headers=cls.HEADERS, params=request_params
                )

            return response if (response.status_code == 200) else None
        except (ConnectionError, Timeout, HTTPError):
            logger.error("No Connection")

    @classmethod
    def fetch_image(cls) -> bool:
        response_obj: requests.Response | None = cls.fetch_response()
        if not response_obj:
            logger.error("unsuccesful request")
            return False

        image_link: str = response_obj.json()["results"][0]["urls"]["full"]
        response_img: requests.Response | None = cls.fetch_response(
            url=image_link, empty_request=True)

        if not response_img:
            logger.warning("something wrong with the image")
            return False

        with open("pywall.jpg", "wb") as image_file:
            image_file.write(response_img.content)

        return True

d = DailyWallpaper.fetch_image()
logger.info("Successfully updated wallpaper") if d else logger.warning("Something fucked up")
