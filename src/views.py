from fastapi import Request, status, HTTPException
from fastapi.responses import RedirectResponse

from src.exceptions import SlugExpiredError
from src.settings import templates
from src.services import LinkGenerator, DetailRetriever


async def index_view(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


async def generate_link_view(request: Request):
    slug = await LinkGenerator(request.app.state.redis).do()
    return RedirectResponse(slug, status_code=status.HTTP_302_FOUND)


async def detail_view(request: Request):
    try:
        context = await DetailRetriever(request.app.state.redis, request.path_params['slug']).do()
    except SlugExpiredError:
        return templates.TemplateResponse('expired.html', {'request': request})

    return templates.TemplateResponse('detail.html', {'request': request, **context})
