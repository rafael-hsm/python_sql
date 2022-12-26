# Estudo de Caso Faculdade

## Tabela Alunos
- Identificador de aluno (chave primária - tipo número)
- Nome (tipo texto)
- Data de nascimento (tipo data)
- Endereço (tipo texto)
- CPF (tipo número)

## Tabela Curso
- Identificador de curso (chave primária - tipo número)
- Nome (tipo texto)

## Tabela Notas
- Identificador de notas (chave primária - tipo número)
- Descrição da atividade
- Nota


## Números
### Inteiros
- TINYINT - número inteiro muito pequeno (tiny);
- SMALLINT - número inteiro pequeno;
- MEDIUMINT - número inteiro de tamanho médio;
- INT - número inteiro de tamanho comum;
- BIGINT - número inteiro de tamanho grande;

### Decimais:
- DECIMAL - número decimal, de ponto fixo;
- FLOAT - número de ponto flutuante de precisão simples (32 bits);
- DOUBLE - número de ponto flutuante de precisão dupla (64 bits);

## Texto
- CHAR - uma cadeia de caracteres (string), de tamanho fixo e não-binária;
- VARCHAR - uma string de tamanho variável e não-binária;
- TEXT - uma string não-binária e pequena;

## Data
- DATE - o valor referente a uma data no formato
"YYYY-MM-DD"
Por exemplo 1985-11-25

- TIME - um valor horário no formato:
"hh:mm:ss"

- DATETIME - o valor referente a uma data e hora no formato: "YYYY-MM-DD hh:mm:ss"
Exemplo: 2018-11-11 12:00:00

## Creating a table
```MySQL
CREATE TABLE IF NOT EXISTS cursos(
id_curso INT NOT NULL AUTO_INCREMENT,
PRIMARY KEY (id_curso));
```

## Alter table
```MySQL
ALTER TABLE alunos 
ADD COLUMN nome VARCHAR(100) NOT NULL AFTER id_aluno,
ADD COLUMN data_nascimento DATE NOT NULL AFTER nome,
ADD COLUMN endereco VARCHAR(255) NOT NULL AFTER data_nascimento,
ADD COLUMN cidade VARCHAR(100) NOT NULL AFTER endereco,
ADD COLUMN estado VARCHAR(2) NOT NULL AFTER cidade,
ADD COLUMN cpf VARCHAR(11) NOT NULL AFTER estado;
```

## Insert Values
```MySQL
INSERT INTO alunos
VALUES (DEFAULT, 'Rafael Meireles', '1990-03-29', 'Rua dos Bobos, n° 0', 'ENCANTADO', 'MS', '12345678911');
```

## Update Values
```MySQL
UPDATE alunos
SET nome = 'Rafael Henrique'
WHERE nome = 'Rafael Meireles'
```

## Delete value

```MySQL
DELETE FROM alunos
WHERE id_aluno = 1;
```

## Making search
```MySQL
SELECT *
FROM alunos
```

```MySQL
SELECT cidade, data_nascimento, cpf
FROM alunos
WHERE cidade = 'ENCANTADO'
ORDER BY nome;
```