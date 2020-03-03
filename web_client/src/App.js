import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component{
  state = {
    solution_data: {}
  }


  getSolutionContent = () => {
    const { solution_data } = this.state;
    console.log(solution_data);
    if(Object.keys(solution_data).length === 0)
    {
      return null;
    }
    return (
      <div id="solution-data">
        <div id="sd-fitness">Fitness: {solution_data.fitness}</div>
        <div id="sd-needed-gens">Generaciones requeridas: {solution_data.needed_generations}</div>
        <div id="sd-time">Tiempo: {solution_data.tiempo}</div>
        <div id="sd-genes">Genes: {solution_data.genes}</div>
        <div id="sd-problem">Problema: {solution_data.problem}</div>
      </div>
    )
  }

  handelStartBTNClick = e => {
    const problem_input = document.getElementById("problem");
    let problem;
    if(!/^\d+(\s\d+)*$/.test(problem_input.value))
    {
      problem = []
    }
    else 
    {
      problem = problem_input.value.split(" ");
      problem = problem.map(num => parseInt(num));
      console.log(problem);
    }
    const forma = new FormData();
    forma.append("problem", JSON.stringify(problem));
    const request = new Request("http://localhost:5000/get-fittest", {method: "POST", body: forma});
    fetch(request)
        .then(promise => promise.json())
        .then(response => {
          if(response.solution !== undefined)
          {
            this.setState({
              solution_data: response.solution
            })
          }
        })  
  }

  render()
  {
    const solution_content = this.getSolutionContent();
    return (
      <div className="App">
        <div id="title-bar">
          <h1>Algoritmos geneticos: Echauri SSP Inteligencia Artificial</h1>
        </div>
        <div id="input-problem-container">
          <div onClick={this.handelStartBTNClick} id="start-btn">Start</div>
          <input type="text" id="problem"/>
        </div>
        <div id="solution-container">
          {solution_content}
        </div>
      </div>
    );
  }
}

export default App;
