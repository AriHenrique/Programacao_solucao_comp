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