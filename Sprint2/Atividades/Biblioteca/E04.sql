select autor.nome,autor.nascimento,autor.codautor, count(livro.cod) as quantidade
from autor
left join livro on autor.codautor = livro.autor
GROUP by autor.nome,autor.nascimento,autor.codautor
ORDER by autor.nome asc 