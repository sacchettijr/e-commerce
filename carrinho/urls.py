from django.contrib.auth.decorators import login_required
from django.urls import path
from carrinho.views import PublicoCarrinhoView, CreateCarrinhoItemView


urlpatterns = [
	path('', login_required(PublicoCarrinhoView.as_view()), name='publico_carrinho'),
	path('adicionar/<slug:slug>', login_required(CreateCarrinhoItemView.as_view()), name='publico_create_carrinho_item')
]
