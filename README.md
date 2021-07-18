# PythonTabelas
Desenha tabelas no terminal a partir de uma lista

```
Nomes       Valores      Adicional      
Nome A      50           80             
Nome B      80           -              
Nome C      150          -       
```

## Uso:

Existe 4 configurações, com separadores á esquerda ou no topo, ambos ou sem.

Exemplo:

Para criar um tabela basta instanciar o objeto da classe com a lista
```py
t = Tabela(tabela, None)
t.desenhaTabela()
```

O segundo parâmetro serve para passar a configuração da tabela: 0 - Sem, 1 - Esquerda, 2 - Topo, 3 - Ambos

#### Ambos
```
Nomes       | Valores      Adicional      
-----------------------------------------------
Nome A      | 50           80             
Nome B      | 80           -              
Nome C      | 150          -              
```

#### Sem
```
Nomes       Valores      Adicional      
Nome A      50           80             
Nome B      80           -              
Nome C      150          -       
```

#### Esquerda
```
Nomes       | Valores      Adicional      
Nome A      | 50           80             
Nome B      | 80           -              
Nome C      | 150          -        
```

#### Topo
```
Nomes       Valores      Adicional      
-----------------------------------------------
Nome A      50           80             
Nome B      80           -              
Nome C      150          -              
```



2021
