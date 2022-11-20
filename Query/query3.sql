-- Algoritmo desenvolvera performance ruim, por conta dos recalculos... Porém, como é uma consulta unica lateral, preferi levar desta forma.
select PRODUTO.id, ((sum(PEDIDO.quantidade * PEDIDO.preco)-(sum(PEDIDO.quantidade * PEDIDO.preco) * GRUPO.imposto)-sum(PEDIDO.quantidade * PEDIDO.custo))/((sum(PEDIDO.quantidade * PEDIDO.preco)-(sum(PEDIDO.quantidade * PEDIDO.preco) * GRUPO.imposto)))) as MargemAbsoluta 
from PEDIDO, PRODUTO, GRUPO
where ((PEDIDO.id_produto=PRODUTO.id)AND(PRODUTO.grupo=GRUPO.nome)AND(PEDIDO.datat >= '2021-01-01'))
group by PRODUTO.id
order by MargemAbsoluta DESC
limit 10
