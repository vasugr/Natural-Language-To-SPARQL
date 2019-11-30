# Natural-Language-To-SPARQL
Translate a query in natural language to SPARQL query with an interactive web based interface.
<br>
Neural SPARQL Machines
Installation guide for spacey
pip install -U spacey
python -m venv .env
source .env/bin/activate
pip install spacey
<br>
Installation guide for flask

$ mkdir myproject
$ cd myproject
$ python3 -m venv venv
$ .venv/bin/activate
$ pip install Flask

<br>
Data preparation
Generation
To generate the training data, launch the following command.

mkdir data/monument_300
python generator.py --templates data/annotations_monument.csv  --output data/monument_300

<br>
Training
Now go back to the initial directory and launch train.sh to train the model. The first parameter is the prefix of the data directory and the second parameter is the number of training epochs.
sh train.sh data/monument_300 120000
This command will create a model directory called data/monument_300_model.

<br>
Inference
Predict the SPARQL sentence for a given question with a given model.
In this, we wil run back.py. After that go to http://localhost:5000/result on any web browser. This has front end. Enter your query and sparql sentence will be generated in next page.

<p>
  Execution of the application - Run back.py and then go to http://localhost:5000/ .
