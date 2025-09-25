SELECT 
    tbvendedor.nmvdd AS vendedor,
    SUM(tbvendas.vrunt * tbvendas.qtd) AS valor_total_vendas,
    ROUND(SUM((tbvendas.vrunt * tbvendas.qtd) * (tbvendedor.perccomissao / 100.0)),2) AS comissao
FROM 
    tbvendedor
JOIN 
    tbvendas ON tbvendedor.cdvdd = tbvendas.cdvdd
WHERE 
    tbvendas.status = 'Concluído'
GROUP BY 
    tbvendedor.cdvdd, tbvendedor.nmvdd
ORDER BY 
    comissao DESC;