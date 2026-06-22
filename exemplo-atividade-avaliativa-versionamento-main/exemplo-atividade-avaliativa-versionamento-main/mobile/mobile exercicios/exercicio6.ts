interface AlunoEscola {
    nome: string;
    faltas: number;
  }
  
  const aluno: AlunoEscola = {
    nome: "João",
    faltas: 0
  };
  
  function adicionarFalta(): void {
    aluno.faltas += 1;
    console.log(`Faltas: ${aluno.faltas}`);
  
    if (aluno.faltas >= 4) {
      console.log("⚠️ Risco de Reprovação");
    }
  }
  
  // Testes
  adicionarFalta();
  adicionarFalta();
  adicionarFalta();
  adicionarFalta();