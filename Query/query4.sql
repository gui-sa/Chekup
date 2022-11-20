-- Algoritmo desenvolvera performance ruim, por conta dos recalculos... Porém, como é uma consulta unica lateral, preferi levar desta forma.
select PRODUTO.id, sum(PEDIDO.quantidade * PEDIDO.preco) as Receita, META.vendas, (sum(PEDIDO.quantidade * PEDIDO.preco) -  META.vendas) as Comparacao
from PEDIDO, PRODUTO, META
where ((PEDIDO.id_produto=PRODUTO.id)AND(PRODUTO.id=META.id)AND(META.data1 = '2021-05-01')AND(PEDIDO.datat>='2021-05-01')AND(PEDIDO.datat<'2021-06-01'))
group by PRODUTO.id
having Comparacao<0
order by Comparacao ASC
