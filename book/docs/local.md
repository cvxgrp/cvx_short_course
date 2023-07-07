# Local execution

You may prefer performing all experiments on your local machine.
For that purpose clone the repository and build a dedicated environment.

```bash
git clone <repo>
cd <repo>
pip install virtualenv           # if you don't already have virtualenv installed
virtualenv .venv                 # to create your new environment (called '.venv' here)
source .venv/bin/activate        # to enter the virtual environment
pip install -r requirements.txt  # to install the requirements in the current environment
```

In order to verify you have successfully installed cvxpy and its dependencies
please run (from within the virtual environment) 

```bash
python test.py 
```
