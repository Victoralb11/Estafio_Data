 CREATE TABLE dim_clientes (
    id_cliente INTEGER PRIMARY KEY,
    nome_cliente TEXT,
    cidade_cliente TEXT,
    estado_cliente TEXT,
    pais_cliente TEXT
);
------------------------------------------------------------------------------------------------------------------------------------
CREATE TABLE dim_carros (
    id_carro INTEGER PRIMARY KEY,
    marca_carro TEXT,
    modelo_carro TEXT,
    ano_carro INTEGER,
    id_combustivel INTEGER,
    FOREIGN KEY (id_combustivel) REFERENCES combustivel(id_combustivel)
);
-------------------------------------------------------------------------------------------------------------------------------------
CREATE TABLE dim_vendedores (
    id_vendedor INTEGER PRIMARY KEY,
    nome_vendedor TEXT,
    estado_vendedor TEXT
);
---------------------------------------------------------------------------------------------------------------------------------------
CREATE TABLE dim_combustivel (
    id_combustivel INTEGER PRIMARY KEY,
    tipo_combustivel TEXT
);
---------------------------------------------------------------------------------------------------------------------------------------
PRAGMA foreign_keys = ON;

CREATE TABLE fato_locacoes (
    id_locacao INTEGER PRIMARY KEY,
    id_cliente INTEGER,
    id_carro INTEGER,
    id_vendedor INTEGER,
    id_combustivel INTEGER,
    data_locacao DATE,
    qtd_diaria INTEGER,
    vlr_diaria DECIMAL(10, 2),

    FOREIGN KEY (id_cliente) REFERENCES dim_clientes(id_cliente),
    FOREIGN KEY (id_carro) REFERENCES dim_carros(id_carro),
    FOREIGN KEY (id_vendedor) REFERENCES dim_vendedores(id_vendedor),
    FOREIGN KEY (id_combustivel) REFERENCES dim_combustivel(id_combustivel)
);
