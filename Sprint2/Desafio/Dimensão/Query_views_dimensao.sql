CREATE VIEW vw_clientes AS
SELECT 
    id_cliente, 
    nome_cliente, 
    cidade_cliente, 
    estado_cliente, 
    pais_cliente
FROM 
    clientes;

CREATE VIEW vw_carros AS
SELECT 
    id_carro, 
    marca_carro, 
    modelo_carro, 
    ano_carro, 
    id_combustivel
FROM 
    carros; 

CREATE VIEW vw_vendedores AS
SELECT 
    id_vendedor, 
    nome_vendedor, 
    estado_vendedor
FROM 
    vendedores; 


CREATE VIEW vw_combustivel AS
SELECT 
    id_combustivel, 
    tipo_combustivel
FROM 
    combustivel; 

CREATE VIEW vw_locacoes AS
SELECT 
    id_locacao, 
    id_cliente, 
    id_carro, 
    id_vendedor, 
    data_locacao, 
    qtd_diaria, 
    vlr_diaria
FROM 
    locacoes;
