CREATE TABLE SL_CLIENTES_ADIMPLENTES
( id INT NOT NULL,
  nome VARCHAR(50) NOT NULL,
  dia_vencimento VARCHAR(2),
  dt_cadastro DATE,
  dt_congelamento DATE,
  dt_desativacao DATE,
  dt_processamento DATE
);