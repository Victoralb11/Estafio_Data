SELECT DISTINCT autor.nome
FROM livro
LEFT JOIN autor ON livro.autor = autor.codautor
LEFT JOIN editora ON livro.editora = editora.codeditora
LEFT JOIN endereco ON editora.endereco = endereco.codendereco
WHERE endereco.codendereco NOT IN (3657, 5030, 5173)
ORDER BY autor.nome;