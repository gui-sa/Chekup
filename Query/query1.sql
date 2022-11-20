select PEDIDO.id_cliente as id, SUM(PEDIDO.quantidade) as total
from PEDIDO
where PEDIDO.datat >= '2021-01-01'
group by id
order by total desc
limit 10

