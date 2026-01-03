from rest_framework.routers import DefaultRouter
from loja.views.produto import ProdutoViewSet
from loja.views.marca import MarcaViewSet

router = DefaultRouter()

router.register(r'produtos', ProdutoViewSet)
router.register(r'marcas', MarcaViewSet)

urlpatterns = router.urls