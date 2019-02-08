CREATE TABLE SL_CLIENTES_ADIMPLENTES
( cliente_id INT NOT NULL,
  nome VARCHAR(500) NOT NULL,
  dia_vencimento VARCHAR(2),
  dt_cadastro DATE,
  dt_congelamento DATE,
  dt_desativacao DATE,
  dt_processamento DATE
);

CREATE TABLE SL_CLIENTES_INADIMPLENTES
( cliente_id INT NOT NULL,
  nome VARCHAR(500) NOT NULL,
  dia_vencimento VARCHAR(2),
  dt_cadastro DATE,
  dt_congelamento DATE,
  dt_desativacao DATE,
  dt_processamento DATE
)

CREATE TABLE SL_CLIENTES_RECEBIMENTOS
( cliente_id INT NOT NULL,
  recebimento_id INT NOT NULL, 
  dt_geracao DATE,
  dt_vencimento DATE,
  valor DECIMAL,
  dt_processamento DATE
);