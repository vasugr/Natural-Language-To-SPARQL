# Natural-Language-To-SPARQL
Translate a query in natural language to SPARQL query with an interactive web based interface.

Go to `Untitled1.ipynb` 

The below steps are optional 


## Neural SPARQL Machines

Create a virtual env - 
```bash
python -m venv .env
source .env/bin/activate
```

Install requirements - 
```bash
pip install spacey
```
```bash
pip install Flask
```

### Data preparation

To generate the training data, execute the following commands

```bash
mkdir data/monument_300
```
```bash
python generator.py --templates data/annotations_monument.csv  --output data/monument_300
```
### Training
Now go back to the initial directory and launch train.sh to train the model. The first parameter is the prefix of the data directory and the second parameter is the number of training epochs.
```bash
sh train.sh data/monument_300 120000
```
This command will create a model directory called data/monument_300_model.

## Inference
Predict the SPARQL sentence for a given question with a given model.

### Execution of the application - 
In this, we wil run back.py. After that go to http://localhost:5000/result on any web browser. This has front end. Enter your query and sparql sentence will be generated in next page.
