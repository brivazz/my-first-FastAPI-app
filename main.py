# Запуск сервера: python main.py или uvicorn main:main_app --reload --port 8000
import fastapi
import uvicorn
from starlette.staticfiles import StaticFiles

from api import motd
from api import digital_ocean_images
from services import digital_ocean_service
from views import home
from config import ENV_SECRET, DO_API_ACCESS_TOKEN


main_app = fastapi.FastAPI()


def configure_env_vars():
    if not ENV_SECRET:
        print("WARNING: environment variable ENV_SECRET not found")
        raise Exception("environment variable ENV_SECRET not found")
    else:
        home.secret = ENV_SECRET
    if not DO_API_ACCESS_TOKEN:
        print("WARNING: environment variable DO_API_ACCESS_TOKEN not found")
        raise Exception("environment variable DO_API_ACCESS_TOKEN not found")
    else:
        digital_ocean_service.do_api_token = DO_API_ACCESS_TOKEN


def configure():
    configure_routing()
    configure_env_vars()


def configure_routing():
    main_app.mount('/static', StaticFiles(directory='static'), name='static')
    main_app.include_router(motd.router)
    main_app.include_router(home.router)
    main_app.include_router(digital_ocean_images.router)


if __name__ == '__main__':
    configure()
    uvicorn.run(main_app, host='127.0.0.1', port=8000)
else:
    configure()
