from flask import Flask, request
from flask_cors import CORS
from Evolution import Evolution
from Problem import Problem
from time import time
from threading import Thread
import json
app = Flask(__name__, static_url_path='')
CORS(app)

def runParallelEvolutions(threads_number=2):
    print(f"Runing {threads_number} paralel evolutions")
    evolutions, evolution_threads = [], []
    for h in range(threads_number):
        evolutions.append(Evolution())
        evolution_threads.append(Thread(target=evolutions[h].runEvolutionLoop))
        evolution_threads[h].start()
    for evolution_thread in evolution_threads:
        if evolution_thread.isAlive():
            evolution_thread.join()
    best_of_them_all = evolutions[0]
    for evolution in evolutions:
        print(f"Verifying evolution best fit with fitness score of {evolution.best_fit.fitness_score}")
        best_of_them_all = evolution if evolution.best_fit.fitness_score > best_of_them_all.best_fit.fitness_score else best_of_them_all
    return best_of_them_all

@app.route("/get-fittest", methods=["POST"])
def getFittest():
    if request.method == "POST":
        problem = json.loads(request.form["problem"])
        print(f"PROBLEMA: {problem} {type(problem).__name__}")
        if not len(problem) or type(problem).__name__ != "list":
            problem = None
        tiempo = time()
        Problem(problem) 
        evolution = runParallelEvolutions(4)
        solution = evolution.best_fit
        tiempo = time() - tiempo
        return {"solution": {
            "fitness": solution.fitness_score,
            "genes": solution.genoma,
            "needed_generations": evolution.GenerationsNeed,
            "tiempo": tiempo,
            "problem": evolution.getProblem()
        }}

if __name__ == "__main__":
    app.run()