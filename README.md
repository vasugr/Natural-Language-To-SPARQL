## Natural-Language-To-SPARQL
Translate a query in natural language to SPARQL query with an interactive web based interface.
# Neural SPARQL Machines
Installation guide for spacey
```bash
pip install -U spacey
```
```bash
python -m venv .env
source .env/bin/activate
```
```bash
pip install spacey
```
# Installation guide for flask

```bash
$ mkdir myproject
```
```bash
$ cd myproject
```
```bash
$ python3 -m venv venv
```
```bash
$ .venv/bin/activate
```
```bash
$ pip install Flask
```

# Data preparation
Generation
To generate the training data, launch the following command.

```bash
mkdir data/monument_300
```
```bash
python generator.py --templates data/annotations_monument.csv  --output data/monument_300
```
# Training
Now go back to the initial directory and launch train.sh to train the model. The first parameter is the prefix of the data directory and the second parameter is the number of training epochs.
```bash
sh train.sh data/monument_300 120000
```
This command will create a model directory called data/monument_300_model.
# Inference
Predict the SPARQL sentence for a given question with a given model.
In this, we wil run back.py. After that go to http://localhost:5000/result on any web browser. This has front end. Enter your query and sparql sentence will be generated in next page.
# Execution of the application - Run back.py and then go to http://localhost:5000/ .
