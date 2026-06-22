interface CarroProps {
    modelo: string;
    valor: number;
  }
  
  function mostrarCarro(carro: CarroProps): void {
    console.log(`Veículo: ${carro.modelo} - R$ ${carro.valor}`);
  }
  
  const carros: CarroProps[] = [
    { modelo: "Onix", valor: 60000 },
    { modelo: "Civic", valor: 120000 },
    { modelo: "Gol", valor: 55000 },
    { modelo: "HB20", valor: 65000 }
  ];
  
  carros
    .filter((carro: CarroProps) => carro.valor < 65000)
    .map((carro: CarroProps) => mostrarCarro(carro));