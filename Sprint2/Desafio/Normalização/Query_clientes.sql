CREATE TABLE clientes (
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_cliente TEXT NOT NULL,
    cidade_cliente TEXT NOT NULL,
    estado_cliente TEXT NOT NULL,
    pais_cliente TEXT NOT NULL
);
INSERT INTO clientes (nome_cliente, cidade_cliente, estado_cliente, pais_cliente)
SELECT DISTINCT
    nomeCliente,
    cidadeCliente,
    estadoCliente,
    paisCliente
FROM tb_locacao;