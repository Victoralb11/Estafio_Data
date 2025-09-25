select autor.codautor, autor.nome, count(livro.cod) as quantidade_publicacoes
from livro
join autor on livro.autor = autor.codautor
group by autor.codautor, autor.nome
order by quantidade_publicacoes DESC 
limit 1
