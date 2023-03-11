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

