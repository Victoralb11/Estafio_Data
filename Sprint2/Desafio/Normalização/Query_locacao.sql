CREATE TABLE locacoes (
    id_locacao INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cliente INTEGER,
    id_carro INTEGER,
    id_vendedor INTEGER,
    data_locacao DATE NOT NULL,
    hora_locacao TIME NOT NULL,
    qtd_diaria INTEGER NOT NULL,
    vlr_diaria REAL NOT NULL,
    data_entrega DATE NOT NULL,
    hora_entrega TIME NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
    FOREIGN KEY (id_carro) REFERENCES carros(id_carro),
    FOREIGN KEY (id_vendedor) REFERENCES vendedores(id_vendedor)
);
INSERT INTO locacoes (id_cliente, id_carro, id_vendedor, data_locacao, hora_locacao, qtd_diaria, vlr_diaria, data_entrega, hora_entrega)
SELECT 
    (SELECT id_cliente FROM clientes WHERE nome_cliente = tb_locacao.nomeCliente AND cidade_cliente = tb_locacao.cidadeCliente),
    (SELECT id_carro FROM carros WHERE marca_carro = tb_locacao.marcaCarro AND modelo_carro = tb_locacao.modeloCarro),
    (SELECT id_vendedor FROM vendedores WHERE nome_vendedor = tb_locacao.nomeVendedor),
    dataLocacao, 
    horaLocacao, 
    qtdDiaria, 
    vlrDiaria, 
    dataEntrega, 
    horaEntrega
FROM tb_locacao;