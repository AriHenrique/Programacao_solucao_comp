# Aula de Programação e Soluções Computacionais (UNA-Aimorés)

<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/devicons/devicon@v2.15.1/devicon.min.css">

Guia de estudos das aulas do semestre 2023/01 UNA — Aimorés. Todos os exercícios são obrigatórios na linguagem "Python", determinada pelo professor responsável, entretanto, resolvi fazer também na linguagem "Rust", uma vez que já havia aprendido a linguagem python. Decidi refazer tudo usando uma outra linguagem que busco aprender e aprimorar, transformando os exercícios de python em rust. Toda a documentação das respectivas linguagens estão lincadas nos ícones.

## <a href="https://docs.python.org/3/"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width=40 align='sub'/></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href='https://devdocs.io/rust/'><img style="background-color: white" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/rust/rust-plain.svg" width=40 align='text-top'/></a>

Bons estudos!

# Aula dia 24/02

Calcule o salario bruto de acordo com o valor da hora e quantidade de horas trabalhadas

## Python <a href="https://docs.python.org/3/"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width=30 align='text-top'/></a>

```python
print('Hello World')
print('Aula dia 24/02/2023')

while True:
    try:
        print("\nCALCULADORA DE SALARIO\n")

        valor_horas = float(input("informe o valor da hora trabalhada: "))
        horas_trabalhadas = float(input("\ninforme quantas horas foram trabalhadas: "))

        total_liquido = valor_horas * horas_trabalhadas

        print(f"TOTAL A RECEBER SERÁ {total_liquido:.2f}")
        break
    except ValueError:
        loop = input("digite apenas números, deseja continuar?(Y/n)").lower()
        if loop[0] == 'y':
            continue
        else:
            print("FIM")
            break
```

## Rust <a href='https://devdocs.io/rust/'><img style="background-color: white" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/rust/rust-plain.svg" width=30 align='text-top'/></a>


```rust
use std::io;

fn main() {
    println!("\nCALCULADORA DE SALARIO\n");

    let valor_horas: f64 = loop {
        println!("informe o valor da hora trabalhada: ");
        let input = get_input();
        match input.parse() {
            Ok(num) => break num,
            Err(_) => {
                println!("Digite apenas números.");
                continue;
            }
        }
    };

    let horas_trabalhadas: f64 = loop {
        println!("\ninforme quantas horas foram trabalhadas: ");
        let input = get_input();
        match input.parse() {
            Ok(num) => break num,
            Err(_) => {
                println!("Digite apenas números.");
                continue;
            }
        }
    };

    let total_liquido = valor_horas * horas_trabalhadas;

    println!("TOTAL A RECEBER SERÁ {:.2}", total_liquido);

    fn get_input() -> String {
        let mut input = String::new();
        io::stdin()
            .read_line(&mut input)
            .expect("Erro ao ler a entrada");
        input.trim().to_string()
    }
}
```

# Aula dia 27/02

## Python <a href="https://docs.python.org/3/"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width=30 align='text-top'/></a>


```python
number1 = 30
number2 = 40

resultado = number1+number2

print(resultado)
```

1) Implemente um programa python que leia o nome de usuario e o dominio, produza a saida usuario@email

2) Implemente um programa python que solicite ao usuario o valor de um produto. Considere uma taxa de 0.1 ao mes exiba o valor total em um periodo de 12 meses.

```python
# 1

nome = input("Digite o seu nome: ")
dominio = input("\nAgora digite o domínio: ")

print(f"{nome}@{dominio}")

# 2
while True:
    try:
        valor_produto = float(input("Digite o valor do produto: "))

        total = valor_produto + ((valor_produto * 0.1) * 12)

        print(f"O valor total do produto será R${total:.2f}")
        break
    except ValueError:
        print("\nDigite apenas numeros\n")
        continue
```

## Rust <a href='https://devdocs.io/rust/'><img style="background-color: white" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/rust/rust-plain.svg" width=30 align='text-top'/></a>

```rust
fn main() {
    let number1 = 30;
    let number2 = 40;

    let result = number1+number2;

    println!("{}", result);
}
```

```rust
use std::io;

fn get_input() -> String {
        let mut input = String::new();
        io::stdin()
            .read_line(&mut input)
            .expect("Erro ao ler a entrada");
        input.trim().to_string()
}


fn exercice_1(){
    
    // exercice 1

    println!("Digite o seu nome: ");
    let mut nome = String::new();
    io::stdin().read_line(&mut nome).expect("Falha ao ler a entrada do usuário");
    nome = nome.trim().to_string();

    println!("Agora digite o dominio: ");
    let mut dominio = String::new();
    io::stdin().read_line(&mut dominio).expect("Falha ao ler a entrada do usuário");
    dominio = dominio.trim().to_string();
    println!("{}@{}", nome, dominio);
}


fn exercice_2(){

    // exercice 1

    let valor_produto: f32 = loop {
        println!("Digite o valor do produto: ");
        let valor_produto = get_input();
        break match valor_produto.parse() {
            Ok(num) => num,
            Err(_) => {
                println!("Valor inválido! Digite apenas numeros");
                continue;
            }
        }    
    };

    let total = valor_produto + (valor_produto * 0.1 * 12.0);

    println!("O total é: {:.2}", total);
}


fn main() {
    exercice_1();
    exercice_2();
}
```

# Aula dia 03/03

## Python <a href="https://docs.python.org/3/"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width=30 align='text-top'/></a>

```py
import math as mt


def verificar_float(variavel):
    """Funcao para verificar se o que o usuario digitou e um numero ou nao.
       Ao inves de usar o "try, except", de forma para aproveitar este tratamento
       em todos os "inputs" do script
    """
    variavel = variavel.replace(',', '.', 1)
    while True:
        if variavel.replace(".", "", 1).isdigit():
            return float(variavel)
        else:
            _loop = input("Infomer apenas números. Deseja Continuar?(Y/n): ").lower()
            if _loop[0] == "y" or _loop == "s":
                variavel = input("Informe novemente os dados: ").replace(',', '.', 1)
                continue
            else:
                print("\nNao foi possivel concluir o programa\n\nFim")
                quit()


print('1) Faça um programa que mostre a mensagem "Alo mundo" na tela.\n')

print("Hello World\n")

print('2) Faça um programa que peça um  número e então mostre a mensagem "O número informado foi [numero]\n')

number = verificar_float(input("Digite um número: "))
print(f'\nO número digitado foi {number}\n')

print('3) Faça um programa que peça dois números e imprima a soma.\n')

number_1 = verificar_float(input("Informe o primeiro número: "))
number_2 = verificar_float(input("Agora informe o segundo: "))

print(f'\nA soma dos dois números é {number_1 + number_2:.2f}\n')

print('4) Faça um programa que peça as 4 notas bimestrais e mostre a média\n')

nota_1 = verificar_float(input("Infomer a nota do seu primeiro semestre: "))
nota_2 = verificar_float(input("Infomer a nota do seu primeiro semestre: "))
nota_3 = verificar_float(input("Infomer a nota do seu primeiro semestre: "))
nota_4 = verificar_float(input("Infomer a nota do seu primeiro semestre: "))

print(f'\nA média dos 4 bimestres é {(nota_1 + nota_2 + nota_3 + nota_4) / 4:.2f}\n')

print('5) Faça um programa que converta metros para centímetros\n')

convert = verificar_float(input("Informe quantos metros deseja converter em cm: "))
print(f'\n{convert * 100:.2f} cm\n')

print('6) Faça um programa que peça o raio de um círculo, calcule e mostre sua área.\n')

raio = verificar_float(input("Informe o raio: "))
print(f'\nA área deste círculo é {mt.pi * raio ** 2:.2f}\n')

print('7) Faça um programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário\n')

area = verificar_float(input("Informe o valor de um dos lados do QUADRADO: "))
print(f'\nO dobro da área do quadrado é {area ** 2 * 2:.2f}\n')

print('8) Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e '
      'mostre o total do seu salário no referido mês.\n')

valor_horas = verificar_float(input("informe o valor da hora trabalhada: "))
horas_trabalhadas = verificar_float(input("\ninforme quantas horas foram trabalhadas: "))
print(f"\nTOTAL A RECEBER SERÁ R$ {valor_horas * horas_trabalhadas:.2f}\n")

print('9) Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus '
      'Celsius.\n')

temperatura_f = verificar_float(input("Digite a temperatura em Farenheit: "))
print(f'{temperatura_f:.1f}F equivale a {round((temperatura_f - 32) * (5 / 9)):.1f}C\n')

print("10) Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.\n")

temperatura_c = verificar_float(input("Digite a temperatura em Celsius: "))
print(f'{temperatura_c:.1f}C equivale a {round(temperatura_c * (9 / 5) + 32):.1f}F\n')

print('11) Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:\n'
      'a. o produto do dobro do primeiro com metade do segundo.\n'
      'b. a soma do tiplo do primeiro com o terceiro.\n'
      'c. o terceiro elevado ao cubo.\n')

num_int = int(verificar_float(input("Digite o primeiro numero inteiro: ")))
num_int_2 = int(verificar_float(input("Digite o segundo numero inteiro: ")))
num_float = verificar_float(input("Digite um valor real (Ex: 10.51): "))

print(f'\nA = {num_int * 2 * (num_int_2 / 2):.2f}')
print(f'B = {3 * num_int + num_float:.2f}')
print(f'C = {num_float ** 3:.2f}\n')

print('12) Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, '
      'usando a seguinte formula:\n(72.7*altura) - 58\n')

altura = verificar_float(input("Informe a sua altura em metros (Ex: 1.75m): "))
print(f'\nO peso ideal para a altura de {altura}m é {72.7 * altura - 58:.1f}kg\n')

print("13) Tendo como dado de entrada a altura (m) de uma pessoa, construa um algoritmo que calcule seu peso ideal, "
      "utilizando as seguintes fórmulas:\n"
      "a. Para homens: (72.7*m) - 58\n"
      "b. Para mulheres: (62.1*m) - 44.7\n")

while True:
    tipo = input("Gostaria de calcular para homem ou mulher? ").lower()
    if tipo[0] == 'h':
        altura = verificar_float(input("Informe a altura em metros (Ex: 1.75m): "))
        print(f'\nO peso ideal para a altura de {altura}m de um HOMEM é {72.7 * altura - 58:.1f}kg\n')
        break
    elif tipo[0] == 'm':
        altura = verificar_float(input("Informe a altura em metros (Ex: 1.75m): "))
        print(f'\nO peso ideal para a altura de {altura}m de uma MULHER é {62.1 * altura - 44.7:.1f}kg\n')
        break
    else:
        loop = input('Tipo de sexo informado inválido. Deseja continuar?(Y/n): ').lower()
        if loop[0] == 'y':
            continue
        else:
            print("\nNao foi possivel concluir o programa\n\nFim")
            break

print("14. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu \n"
      "trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do \n"
      "estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que vocè \n"
      "faça um programa quilos além do limite e na variavel multa o valor da multa que João devera pagar. Imprima os \n"
      "dados do programa com as mensagens adequadasS.")

pescaria_dia = verificar_float(input("\nQuantos kg foram pescados hoje? "))

if pescaria_dia > 50:
    print(f"\nVoce excedeu o limite exigido para sua pesca, o total da multa sera de R${((pescaria_dia - 50) * 4):.2f}")
else:
    print("\nNao ha multas a serem aplicadas")

print(
    '\n15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e\n'
    'mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,\n'
    '8% para o INSS e 5% para o Sindicato, taça um programa que nos dê:\n\n'
    'A. Salaro bruto.\n'
    'B. Quanto pagou ao INSS.\n'
    'C. Quanto pagou ao sindicato.\n'
    'D. O salário líquido.\n'
    'E. Calcule os descontos e o salário líquido, conforme a tabela abaixo:\n')


def tabela(salario=0.0):
    _ir = salario * 0.11
    _inss = salario * 0.08
    _sindicato = salario * 0.05

    a = len(f'   |+ Salario Bruto : R${salario:.2f}|')
    b = len(f'   |= Salario Liquido : R${salario - _ir - _inss - _sindicato:.2f}|')
    if max(a, b) % 2 == 0:
        c = max(a, b) - 1
    else:
        c = max(a, b)
    print(f'E: +{" -" * ((c // 2) - 1)} +')
    print(f'   | + Salario Bruto : R${salario:.2f}'.ljust(c, " "), ' |')
    print(f'   | - IR (11%) : R${_ir:.2f}'.ljust(c, " "), ' |')
    print(f'   | - INSS (8%) : R${_inss:.2f}'.ljust(c, " "), ' |')
    print(f'   | - Sindicato (5%) : R${_sindicato:.2f}'.ljust(c, " "), ' |')
    print(f'   | = Salario Liquido : R${salario - _ir - _inss - _sindicato:.2f}'.ljust(c, " "), '|')
    print(f'   +{" -" * ((c // 2) - 1)} +')


topo_base = f'+{" -" * 11} +'
print(topo_base)
print(f'|+ Salario Bruto : R$'.ljust(len(topo_base) - 2, " "), '|')
print(f'|- IR (11%) : R$'.ljust(len(topo_base) - 2, " "), '|')
print(f'|- INSS (8%) : R$'.ljust(len(topo_base) - 2, " "), '|')
print(f'|- Sindicato (5%) : R$'.ljust(len(topo_base) - 2, " "), '|')
print(f'|= Salario Liquido : R$'.ljust(len(topo_base) - 2, " "), '|')
print(topo_base)

print('\nObs.: Salario Bruto - Descontos = Salario Liquido')

valor_hora = verificar_float(input('Informe o valor por hora trabalhada: '))
horas_trabalhadas = verificar_float(input('Informe quantas horas foram trabalhadas: '))
salario_bruto = valor_hora * horas_trabalhadas
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05

print(f'\nA: R${salario_bruto:.2f}')
print(f'B: R${inss:.2f}')
print(f'C: R${sindicato:.2f}')
print(f'D: R${salario_bruto - ir - inss - sindicato:.2f}')
tabela(salario_bruto)

print(
    '\n16. Faça um programa para uma loja de tintas. O programa devera pedir o tamanho em metros quadrados da area a ser\n'
    'pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em\n'
    'latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o\n'
    'preço total.\n')

_metros_quadrados = verificar_float(input("Digite quantos metros² quer pintar? "))
total_tinta = _metros_quadrados / 3

print(
    f'\nVoce precisara de {mt.ceil(total_tinta / 18)} lata(s) de tinta, o total gasto sera de R${mt.ceil(total_tinta / 18) * 80}')

print(
    '\n17. Faça um Programa para uma loja de tintas. O programa deverà pedir o tamanho em metros quadrados da área a\n'
    'ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é\n'
    'vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.\n'
    'Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:\n\n'
    'Comprar apenas latas de 18 litros;\n'
    'Comprar apenas galões de 3,6 litros;\n'
    'Misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os\n'
    'valores para cima, isto é, considere latas cheias\n')

metros_quadrados = verificar_float(input("Digite quantos metros² quer pintar? "))

area_lata = 18 * 6
area_galao = 3.6 * 6
apenas_latas = mt.ceil(metros_quadrados / area_lata)
apenas_galao = mt.ceil(metros_quadrados / area_galao)

print(f'\nSe for usar apenas latas, irá precisar de {apenas_latas} lata(s) = R${apenas_latas * 80:.2f}')
print(f'Se for usar apenas galões, irá precisar de {apenas_galao} galão(es) = R${apenas_galao * 25:.2f}')

metros_incremental = metros_quadrados * 1.1
inteiro = int(metros_incremental)
sobra = float(metros_incremental % inteiro)

custo_beneficio = 108 * 0.6

print(f'Caso queira o melhor custo-benefício com uma margem de 10% de folga a mais na área informada\n'
      f'(de {metros_quadrados} metros² para --> {metros_incremental:.2f} metros²) ')
if metros_incremental <= custo_beneficio:
    print(
        f'Voce vai precisar de apenas {mt.ceil(metros_incremental / area_galao)} galao = R${mt.ceil(metros_incremental / area_galao) * 25:.2f}')
elif (metros_incremental <= 108) and metros_incremental > custo_beneficio:
    print('Voce vai gastar apenas 1 lata = R$80.00')
else:
    total_latas = int(metros_incremental // area_lata)
    total_sobra = (metros_incremental / area_lata) % total_latas
    galao = 0

    if total_sobra > 0.6:
        total_latas += 1
    else:
        if total_sobra <= 0.2:
            galao = 1
        elif total_sobra > 0.4:
            galao = 3
        else:
            galao = 2

    print(f'Voce vai gastar {total_latas} lata(s) e {galao} galao(es) = R${(total_latas * 80) + (galao * 25)}')

print(
    '\n18. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet\n'
    '(em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).\n')

tamanho = verificar_float(input('Qual o tamanho do arquivo? (em MB): '))
velocidade = verificar_float(
    input('Qual a velocidade da internet? (em Mbps, valor normal informado pelas provedoras): '))

print(f"\nLevara um tempo de {mt.ceil(tamanho / (velocidade / 8))}seg "
      f"(ou aproximadamente {(tamanho / (velocidade / 8)) / 60:.1f}min) para completar o download do arquivo")
```

## Rust <a href='https://devdocs.io/rust/'><img style="background-color: white" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/rust/rust-plain.svg" width=30 align='text-top'/></a>

```rust
use std::io::{self, Write};

fn verificar_float(variavel: String) -> f64 {
    let mut variavel = variavel.replace(",", ".");
    loop {
        if variavel.replace(".", "").chars().all(char::is_numeric) {
            return variavel.parse().unwrap();
        } else {
            let mut _loop = String::new();
            println!("Infomer apenas números. Deseja Continuar?(Y/n): ");
            io::stdout().flush().unwrap();
            io::stdin().read_line(&mut _loop).unwrap();
            _loop = _loop.trim().to_lowercase();
            if _loop.starts_with("y") || _loop == "s" {
                println!("Informe novemente os dados: ");
                io::stdout().flush().unwrap();
                variavel.clear();
                io::stdin().read_line(&mut variavel).unwrap();
                variavel = variavel.trim().replace(",", ".");
                continue;
            } else {
                println!("\nNao foi possivel concluir o programa\n\nFim");
                std::process::exit(1);
            }
        }
    }
}

fn input(prompt: &str) -> String {
    println!("{}", prompt);
    let mut buffer = String::new();
    io::stdout().flush().unwrap();
    io::stdin().read_line(&mut buffer).unwrap();
    buffer.trim().to_owned()
}

fn main() {
    println!("1) Faça um programa que mostre a mensagem 'Alo mundo' na tela.\n");

    println!("Hello World\n");

    println!("2) Faça um programa que peça um  número e então mostre a mensagem 'O número informado foi [numero]'\n");

    let number = verificar_float(String::from(&input("Digite um número: "))); 
    println!("\nO número digitado foi {}\n", number);

    println!("3) Faça um programa que peça dois números e imprima a soma.\n");
    let number_1 = verificar_float(String::from(&input("Informe o primeiro número: ")));  
    let number_2 = verificar_float(String::from(&input("Agora informe o segundo: ")));
    println!("\nA soma é {}", number_1 + number_2);

    println!("4) Faça um programa que peça as 4 notas bimestrais e mostre a média\n");

    let nota_1 = verificar_float(String::from(&input("Infomer a nota do seu primeiro semestre: "))); 
    let nota_2 = verificar_float(String::from(&input("Infomer a nota do seu primeiro semestre: "))); 
    let nota_3 = verificar_float(String::from(&input("Infomer a nota do seu primeiro semestre: "))); 
    let nota_4 = verificar_float(String::from(&input("Infomer a nota do seu primeiro semestre: "))); 

    println!("\nA média dos 4 bimestres é {:.2}\n",(nota_1 + nota_2 + nota_3 + nota_4) / 4.0);

    println!("5) Faça um programa que converta metros para centímetros\n");

    let convert = verificar_float(String::from(&input("Informe quantos metros deseja converter em cm: "))); 
    println!("\n{:.2} cm\n", convert * 100.0);   

    println!("6) Faça um programa que peça o raio de um círculo, calcule e mostre sua área.\n");

    let raio = verificar_float(String::from(&input("Informe o raio: ")));
    println!("\nA área deste círculo é {:.2}\n", std::f64::consts::PI * raio.powi(2));

    println!("7) Faça um programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário\n");

    let area = verificar_float(String::from(&input("Informe o valor de um dos lados do QUADRADO: ")));
    println!("\nO dobro da área do quadrado é {:.2}\n", area.powi(2) * 2.0);

    println!("8) Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. \
            Calcule e mostre o total do seu salário no referido mês.\n");

    let valor_horas = verificar_float(String::from(&input("informe o valor da hora trabalhada: ")));
    let horas_trabalhadas = verificar_float(String::from(&input("\ninforme quantas horas foram trabalhadas: ")));
    println!("\nTOTAL A RECEBER SERÁ R$ {:.2}\n", valor_horas * horas_trabalhadas);

    println!("9) Faça um Programa que peça a temperatura em graus Farenheit, transforme \
            e mostre a temperatura em graus Celsius.\n");

    let temperatura_f = verificar_float(String::from(&input("Digite a temperatura em Farenheit: ")));
    println!("{:.1}F equivale a {:.1}C\n",temperatura_f,((temperatura_f - 32.0) * (5.0/9.0)).round());

    println!("10) Faça um Programa que peça a temperatura em graus Celsius, \
            transforme e mostre em graus Farenheit.\n");

    let temperatura_c = verificar_float(String::from(&input("Digite a temperatura em Celsius: ")));
    println!("{:.1}C equivale a {:.1}F\n", temperatura_c, (temperatura_c * (9.0/5.0) + 32.0).round());

    println!("11) Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:\n \
            a. o produto do dobro do primeiro com metade do segundo.\n \
            b. a soma do tiplo do primeiro com o terceiro.\n \
            c. o terceiro elevado ao cubo.\n"); 

    let num_int = verificar_float(String::from(&input("Digite o primeiro numero inteiro: ")));
    let num_int_2 = verificar_float(String::from(&input("Digite o segundo numero inteiro: ")));
    let num_float = verificar_float(String::from(&input("Digite um valor real (Ex: 10.51): ")));

    println!("\nA = {:.2}",num_int * 2.0 * (num_int_2 / 2.0));
    println!("B = {:.2}", 3.0 * num_int + num_float);
    println!("C = {:.2}\n", num_float.powi(3));

    println!("12) Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo \
            que calcule seu peso ideal, usando a seguinte formula:\n(72.7*altura) - 58\n");

    let altura = verificar_float(String::from(&input("Informe a sua altura em metros (Ex: 1.75m): ")));
    println!("\nO peso ideal para a altura de {}m é {:.1}kg\n", altura, 72.7 * altura - 58.0);

}
```