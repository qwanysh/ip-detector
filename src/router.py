from fastapi import APIRouter

from src.views import index_view, generate_link_view, detail_view

router = APIRouter(prefix='')
router.add_route('/', index_view, methods=['GET'])
router.add_route('/generate', generate_link_view, methods=['POST'])
router.add_route('/{slug}', detail_view, methods=['GET'])
