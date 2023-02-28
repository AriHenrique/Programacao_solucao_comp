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
                println!("Valor inválido para o produto!");
                continue;
            }
        };    
    };

    let total = valor_produto + (valor_produto * 0.1 * 12.0);

    println!("O total é: {:.2}", total);
}


fn main() {
    exercice_1();
    exercice_2();
}