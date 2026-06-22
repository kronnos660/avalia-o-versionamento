interface LancheProps {
    nome: string;
    preco: number;
    vegano: boolean;
  }
  
  const lanches: LancheProps[] = [
    { nome: "Hambúrguer Vegano", preco: 25, vegano: true },
    { nome: "X-Bacon", preco: 20, vegano: false },
    { nome: "Salada", preco: 15, vegano: true },
    { nome: "Cachorro-quente", preco: 18, vegano: false }
  ];
  
  function mostrarLanche(lanche: LancheProps): string {
    return `${lanche.nome} - R$ ${lanche.preco}`;
  }
  
  lanches
    .filter((lanche: LancheProps) => lanche.vegano)
    .map((lanche: LancheProps) => console.log(mostrarLanche(lanche)));