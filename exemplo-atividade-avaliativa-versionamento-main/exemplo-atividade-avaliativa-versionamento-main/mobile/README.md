# 💻 Desenvolvimento com TypeScript

## 📝 Descrição do Projeto/Atividade

Este projeto reúne uma série de exercícios desenvolvidos em TypeScript com o objetivo de praticar conceitos fundamentais da linguagem. Foram implementadas atividades envolvendo estruturas de repetição, arrays, interfaces, funções, filtros de dados e manipulação de estados.

Os exercícios incluem:

* Geração da tabuada de um número.
* Exibição de itens de um inventário.
* Filtragem de lanches veganos.
* Filtragem de veículos por valor.
* Simulação de operações bancárias.
* Controle de faltas de um aluno.

---

## 🧠 Reflexão de Aprendizado

### 1. O que aprendi?

Com esta atividade aprendi conceitos importantes de TypeScript, como:

* Declaração de variáveis com tipagem.
* Utilização de loops (`for` e `for...of`).
* Criação e utilização de interfaces.
* Manipulação de arrays.
* Uso dos métodos `filter()` e `map()`.
* Criação de funções tipadas.
* Controle de estados utilizando variáveis.
* Organização e reutilização de código.

Além disso, desenvolvi uma melhor compreensão sobre como o TypeScript aumenta a segurança do código por meio da tipagem estática.

### 2. Para que serve (Por que aprendi)?

Aprender TypeScript é importante porque ele é amplamente utilizado no desenvolvimento web moderno, especialmente em aplicações React, Angular e Node.js.

Essa tecnologia ajuda a:

* Reduzir erros durante o desenvolvimento.
* Tornar o código mais organizado.
* Facilitar a manutenção de sistemas.
* Melhorar a produtividade da equipe.
* Criar aplicações mais seguras e confiáveis.

No mercado de trabalho, o TypeScript é uma das linguagens mais requisitadas para desenvolvimento front-end e back-end.

---

## 🛠️ Tecnologias e Ferramentas Utilizadas

* TypeScript
* Node.js
* Visual Studio Code

---

## 💻 Demonstração e Como Rodar

### Código Relevante Comentado

```typescript
interface CarroProps {
  modelo: string;
  valor: number;
}

const carros: CarroProps[] = [
  { modelo: "Onix", valor: 60000 },
  { modelo: "Civic", valor: 120000 }
];

// Filtra apenas veículos abaixo de R$ 65.000
carros
  .filter((carro) => carro.valor < 65000)
  .map((carro) =>
    console.log(`Veículo: ${carro.modelo} - R$ ${carro.valor}`)
  );
```

**Explicação:**

* A interface define a estrutura do objeto.
* O array armazena vários carros.
* O método `filter()` seleciona apenas os carros abaixo do valor definido.
* O método `map()` percorre os resultados exibindo as informações.

---

## 🚀 Instruções para Executar

1. Instale o Node.js.
2. Instale o TypeScript:

```bash
npm install -g typescript
```

3. Compile o arquivo:

```bash
tsc exercicio1.ts
```

4. Execute o arquivo gerado:

```bash
node exercicio1.js
```

Repita o processo para os demais exercícios.

---

## 📚 Conclusão

A atividade permitiu aplicar na prática os principais conceitos de TypeScript, fortalecendo conhecimentos em programação, lógica computacional e manipulação de dados. Esses fundamentos são essenciais para o desenvolvimento de aplicações modernas e para a evolução profissional na área de Desenvolvimento de Sistemas.
