from django.views.generic import TemplateView
from produto.models import ProdutoCategoria, Produto, ProdutoImagem


# VIEWS PUBLICAS
class PublicoIndex(TemplateView):
	template_name = 'publico/publico_index.html'
	
	def get_context_data(self, context=None, **kwargs):
		print('\n'*20 + '_'*80 + '\n\n VIEW: PublicoIndex')

		self.kwargs['categorias'] = ProdutoCategoria.objects.filter(ativo=True)  # Navbar
		return self.kwargs


class PublicoCategoriaView(TemplateView):
	template_name = 'publico/publico_produto_listagem.html'
	
	def get_context_data(self, context=None, **kwargs):
		print('\n'*20 + '_'*80 + '\n\n VIEW: PublicoCategoriaView')

		categoria_id = ProdutoCategoria.objects.get(slug=kwargs['slug']).pk
		self.kwargs['categoria_nome'] = ProdutoCategoria.objects.get(slug=kwargs['slug']).nome
		self.kwargs['produtos'] = Produto.objects.filter(categoria=categoria_id, ativo=True)
		self.kwargs['produtos_imagens'] = ProdutoImagem.objects.filter(padrao=True)
		
		return self.kwargs


class PublicoProdutoDetalheView(TemplateView):
	template_name = 'publico/publico_produto_detalhe.html'
	
	def get_context_data(self, context=None, **kwargs):
		print('\n'*20 + '_'*80 + '\n\n VIEW: PublicoProdutoDetalheView')

		produto = Produto.objects.get(slug=kwargs['slug'])
		self.kwargs['produto'] = produto
		self.kwargs['produtos_imagens'] = ProdutoImagem.objects.filter(produto=produto.pk, ativo=True)
		
		return self.kwargs

publico_index = PublicoIndex.as_view()
publico_categoria = PublicoCategoriaView.as_view()
publico_produto = PublicoProdutoDetalheView.as_view()
