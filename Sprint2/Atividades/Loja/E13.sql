SELECT 
    tbvendas.cdpro,
    tbvendas.nmcanalvendas,
    tbvendas.nmpro,
    SUM(tbvendas.qtd) AS quantidade_vendas
FROM 
    tbvendas
WHERE 
    tbvendas.status = 'Concluído' 
GROUP BY 
    tbvendas.cdpro, tbvendas.nmcanalvendas, tbvendas.nmpro
HAVING 
    quantidade_vendas > 0  
ORDER BY 
    quantidade_vendas ASC
LIMIT 10;