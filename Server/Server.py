from flask import Flask, request
from flask_cors import CORS
from Evolution import Evolution
from time import time
import json
app = Flask(__name__, static_url_path='')
CORS(app)

@app.route("/get-fittest", methods=["POST"])
def getFittest():
    if request.method == "POST":
        problem = json.loads(request.form["problem"])
        print(f"PROBLEMA: {problem} {type(problem).__name__}")
        if not len(problem) or type(problem).__name__ != "list":
            problem = None
        tiempo = time()
        evolution = Evolution(problem) 
        solution = evolution.runEvolutionLoop()
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