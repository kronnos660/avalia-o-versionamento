let saldo: number = 1000;

function sacar(valor: number): void {
  if (valor > saldo) {
    console.log("Saldo insuficiente!");
  } else {
    saldo -= valor;
    console.log(`Saque realizado. Saldo atual: ${saldo}`);
  }
}

function depositar(valor: number): void {
  saldo += valor;
  console.log(`Depósito realizado. Saldo atual: ${saldo}`);
}

// Testes
sacar(200);
depositar(500);
sacar(1500);