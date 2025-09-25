CREATE TABLE vendedores (
    id_vendedor INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_vendedor TEXT NOT NULL,
    sexo_vendedor TEXT,
    estado_vendedor TEXT NOT NULL
);
INSERT INTO vendedores (nome_vendedor, sexo_vendedor, estado_vendedor)
SELECT DISTINCT
    nomeVendedor,
    sexoVendedor,
    estadoVendedor
FROM tb_locacao;

