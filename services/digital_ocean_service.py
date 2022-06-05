from typing import Optional
import httpx


do_api_token: Optional[str] = None


async def get_droplet_images_async():
    url = "https://api.digitalocean.com/v2/images?type=distribution"
    # если не сработает, то поднять любой сервер например:
    # url = "http://127.0.0.1:8000/api/v1/test.png"
    url_headers = {'Authorization': 'Bearer' + do_api_token}

    async with httpx.AsyncClient() as client:
        resp = await client.get(url, headers=url_headers)
    data = resp.json()
    # droplet_images = data['images']
    droplet_images = data['message']
    return droplet_images
