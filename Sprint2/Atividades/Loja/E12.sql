SELECT 
    tbdependente.cddep,
    tbdependente.nmdep,
    tbdependente.dtnasc,
    SUM(tbvendas.vrunt * tbvendas.qtd) AS valor_total_vendas
FROM 
    tbdependente
JOIN 
    tbvendas ON tbdependente.cdvdd = tbvendas.cdvdd
WHERE 
    tbvendas.status = 'Concluído'
GROUP BY 
    tbdependente.cddep, tbdependente.nmdep, tbdependente.dtnasc, tbdependente.cdvdd
HAVING 
    valor_total_vendas > 0
ORDER BY 
    valor_total_vendas ASC
LIMIT 1;