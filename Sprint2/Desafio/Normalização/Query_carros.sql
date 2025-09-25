CREATE TABLE carros (
    id_carro INTEGER PRIMARY KEY AUTOINCREMENT,
    km INTEGER,
    classi_carro TEXT NOT NULL,
    marca_carro TEXT NOT NULL,
    modelo_carro TEXT NOT NULL,
    ano_carro INTEGER,
    id_combustivel INTEGER,
    FOREIGN KEY (id_combustivel) REFERENCES combustivel(id_combustivel)
);
INSERT INTO carros (km, classi_carro, marca_carro, modelo_carro, ano_carro, id_combustivel)
SELECT DISTINCT
    kmCarro,
    classiCarro,
    marcaCarro,
    modeloCarro,
    anoCarro,
    (SELECT id_combustivel FROM combustivel WHERE tipo_combustivel = tb_locacao.tipoCombustivel)
FROM tb_locacao;