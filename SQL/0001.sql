CREATE TABLE SL_CLI_ADIMPLENTES
( cliente_id INT NOT NULL,
  nome VARCHAR(500) NOT NULL,
  dia_vencimento VARCHAR(2),
  dt_cadastro DATE,
  dt_congelamento DATE,
  dt_desativacao DATE,
  dt_processamento DATE
);

CREATE TABLE SL_CLI_INADIMPLENTES
( cliente_id INT NOT NULL,
  nome VARCHAR(500) NOT NULL,
  dia_vencimento VARCHAR(2),
  dt_cadastro DATE,
  dt_congelamento DATE,
  dt_desativacao DATE,
  dt_processamento DATE
)

CREATE TABLE SL_CLI_INADIMPLENTES_RECEBIMENTOS
( cliente_id INT NOT NULL,
  recebimento_id INT NOT NULL, 
  dt_geracao DATE,
  dt_vencimento DATE,
  valor DECIMAL,
  dt_processamento DATE
);

CREATE TABLE SL_CLI_RECEBIMENTOS_ENCARGOS
( recebimento_id INT NOT NULL,
  dias_atraso INT,
  valor_corrigido DECIMAL,
  dt_processamento DATE
);

CREATE TABLE SL_METRICAS
( dt_real DATE,
  conquistadas FLOAT,
  desativadas FLOAT,
  liquido FLOAT,
  clientes_conquistados INT,
  clientes_reativados INT,
  clientes_desativados INT,
  assinaturas_conquistadas INT,  
  migracao_conquistadas INT,
  migracao_assinaturas_conquistadas INT,
  assinaturas_desativadas INT,
  migracao_desativadas INT,
  migracao_assinaturas_desativadas INT,
  assinaturas_contraidas INT,
  assinaturas_expandidas INT,
  conquistadas_liquido FLOAT,
  desativadas_liquido FLOAT,
  clientes INT,
  assinaturas INT,
  ticket DECIMAL,
  churn_mrr FLOAT,
  grow_mrr FLOAT,
  churn FLOAT,
  grow FLOAT,
  mrr FLOAT,
  ltv FLOAT,
  lt FLOAT,
  churn_corrigido FLOAT,
  churn_corrigido_valor FLOAT,
  arr FLOAT,
  boleto INT,
  cartao_credito INT,
  debito_auto INT,
  net_mrr FLOAT,
  net_mrr_percentual FLOAT, 
  dt_processamento DATE
);