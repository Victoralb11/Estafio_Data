SELECT 
    tbvendas.estado,
    ROUND(AVG(tbvendas.vrunt * tbvendas.qtd), 2) AS gastomedio
FROM 
    tbvendas
WHERE 
    tbvendas.status = 'Concluído'
GROUP BY 
    tbvendas.estado
ORDER BY 
    gastomedio DESC;