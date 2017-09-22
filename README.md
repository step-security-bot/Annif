# Annif

*ANNotation Infrastructure using Finna: an automatic subject indexing tool using Finna as corpus*.

This repo contains a rewritten production version of Annif based on the [prototype](https://github.com/osma/annif).
A work in progress.

### Dependencies

Python 3.5+ and a locally installed [Elasticsearch](https://www.elastic.co/products/elasticsearch) instance. Using virtualenv for setting up an isolated environment is encouraged. Other dependencies are listed in requirements.txt.

### Installation and setup

Clone the repository.

Switch into the repository directory and create a virtualenv environment by running `virtualenv annif_env && source annif_env/bin/activate`.

Install dependencies by running `pip install -r requirements.txt`.

Set the `FLASK_APP` enviroment variable: `export FLASK_APP=annif.py`.

Run with the command `flask run`.

Run tests with the command `pytest`.
