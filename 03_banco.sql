-- Banco de dados do projeto Schulz - Entrega 02
-- Estrutura para SQLite.

-- Ativa a verificação dos relacionamentos entre as tabelas.
PRAGMA foreign_keys = ON;

-- Cadastra as pessoas e os setores envolvidos nas medições.
CREATE TABLE IF NOT EXISTS responsaveis (
    id_responsavel INTEGER PRIMARY KEY,

    codigo TEXT NOT NULL UNIQUE
        CHECK (length(trim(codigo)) > 0),

    nome TEXT NOT NULL
        CHECK (length(trim(nome)) > 0),

    tipo TEXT NOT NULL
        CHECK (tipo IN ('PESSOA', 'SETOR')),

    ativo INTEGER NOT NULL DEFAULT 1
        CHECK (ativo IN (0, 1))
);

-- Cadastra os equipamentos que serão calibrados.
CREATE TABLE IF NOT EXISTS equipamentos (
    id_equipamento INTEGER PRIMARY KEY,

    codigo TEXT NOT NULL UNIQUE
        CHECK (length(trim(codigo)) > 0),

    descricao TEXT NOT NULL
        CHECK (length(trim(descricao)) > 0),

    fabricante TEXT,

    modelo TEXT,

    numero_serie TEXT,

    ativo INTEGER NOT NULL DEFAULT 1
        CHECK (ativo IN (0, 1))
);

-- Registra as leituras e seus vínculos com os cadastros.
CREATE TABLE IF NOT EXISTS medicoes (
    id_medicao INTEGER PRIMARY KEY,

    id_equipamento INTEGER NOT NULL,
    id_tecnico INTEGER NOT NULL,
    id_solicitante INTEGER NOT NULL,

    codigo_calibracao TEXT NOT NULL
        CHECK (length(trim(codigo_calibracao)) > 0),

    -- Verifica o formato. O programa deverá validar a data real.
    data_medicao TEXT NOT NULL
        CHECK (
            data_medicao GLOB
            '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'
        ),

    codigo_caracteristica TEXT NOT NULL
        CHECK (length(trim(codigo_caracteristica)) > 0),

    parametro TEXT NOT NULL
        CHECK (length(trim(parametro)) > 0),

    sequencia INTEGER NOT NULL
        CHECK (
            typeof(sequencia) = 'integer'
            AND sequencia > 0
        ),

    unidade TEXT NOT NULL
        CHECK (length(trim(unidade)) > 0),

    valor_nominal REAL NOT NULL
        CHECK (typeof(valor_nominal) IN ('integer', 'real')),

    tolerancia_inferior REAL NOT NULL
        CHECK (typeof(tolerancia_inferior) IN ('integer', 'real')),

    tolerancia_superior REAL NOT NULL
        CHECK (typeof(tolerancia_superior) IN ('integer', 'real')),

    valor_obtido REAL NOT NULL
        CHECK (typeof(valor_obtido) IN ('integer', 'real')),

    valor_original TEXT NOT NULL
        CHECK (length(trim(valor_original)) > 0),

    status TEXT NOT NULL DEFAULT 'PENDENTE'
        CHECK (
            status IN (
                'PENDENTE',
                'CONFORME',
                'NAO_CONFORME',
                'INDETERMINADO'
            )
        ),

    arquivo_origem TEXT NOT NULL
        CHECK (length(trim(arquivo_origem)) > 0),

    local_origem TEXT NOT NULL
        CHECK (length(trim(local_origem)) > 0),

    registrado_em TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,

    observacao TEXT,

    -- Liga a leitura ao equipamento cadastrado.
    FOREIGN KEY (id_equipamento)
        REFERENCES equipamentos (id_equipamento)
        ON DELETE RESTRICT,

    -- Liga a leitura ao técnico cadastrado.
    FOREIGN KEY (id_tecnico)
        REFERENCES responsaveis (id_responsavel)
        ON DELETE RESTRICT,

    -- Liga a leitura ao solicitante cadastrado.
    FOREIGN KEY (id_solicitante)
        REFERENCES responsaveis (id_responsavel)
        ON DELETE RESTRICT,

    CHECK (tolerancia_inferior <= tolerancia_superior),

    -- Evita registrar a mesma leitura duas vezes.
    UNIQUE (
        id_equipamento,
        codigo_calibracao,
        codigo_caracteristica,
        sequencia
    )
);