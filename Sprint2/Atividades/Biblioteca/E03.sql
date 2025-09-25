select count(*) as quantidade, editora.nome, endereco.estado, endereco.cidade
from livro
join editora on livro.editora = editora.codeditora
join endereco on editora.endereco = endereco.codendereco
group by editora.nome, endereco.estado, endereco.cidade
order by quantidade desc
limit 5