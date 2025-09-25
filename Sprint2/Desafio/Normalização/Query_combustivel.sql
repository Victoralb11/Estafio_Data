CREATE TABLE combustivel (
    id_combustivel INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo_combustivel TEXT NOT NULL
);

INSERT INTO combustivel (tipo_combustivel)
SELECT DISTINCT tipoCombustivel
FROM tb_locacao;