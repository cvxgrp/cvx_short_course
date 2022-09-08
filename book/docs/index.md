# CVX Short Course

ypically the steps you always takes are:

```bash
git clone <repo>
cd <repo>
pip install virtualenv #(if you don't already have virtualenv installed)
virtualenv .venv        #to create your new environment (called '.venv' here)
source .venv/bin/activate #to enter the virtual environment
pip install -r requirements.txt #to install the requirements in the current environment
```

In order to verify you have successfully installed cvxpy and its dependencies
please run (from with the virtual environment) 

```bash
python test.py 
```

## Example tutorial schedule

1. Convex optimization overview
* Mathematical optimization
* Convex optimization
* Solvers & modeling languages
* CVXPY example
* Real-world applications

2. Hello world
* Participants will install CVXPY and solve their first convex optimization problem. Participants will get experience
with basic CVXPY syntax.
* [Hello world exercise](docs/exercises/hello_world)
* [Extra exercise](docs/exercises/Lasso.ipynb)

3. Constructive convex analysis
* Mathematically define convex, concave, and affine functions. Give many examples.
* Introduce the composition rule for convex, concave, and affine functions, which generates the grammar for
CVXPY.
* Introduce Disciplined Convex Programming (DCP).
* Learn how to construct convex optimization problems using DCP in CVXPY.

4. DCP exercises
* Participants will solve their first convex optimization problem with CVXPY, getting experience with basic CVXPY
syntax./
* [DCP exercise](docs/exercises/DCP_analysis.ipynb)
* [DCP site](https://dcp.stanford.edu/)
* [DCP quiz](https://dcp.stanford.edu/quiz)

5. Applications of convex optimization
* Present applications in finance, machine learning, vehicle control, and risk analysis.
* For each application, the instructors will give a motivating overview, and participants will then code up and solve
a problem arising in the application using CVXPY. Concretely, exercises will consist of notebooks with missing
sections, which the participants need to fill in with code constructing and solving a CVXPY problem.
* [Simple portfolio optimization](docs/exercises/13.3)
* [Portfolio rebalancing](docs/exercises/13.21.ipynb)
* [Multiple risk models](https://github.com/cvxgrp/cvx_short_course/blob/master/exercises/13.22.ipynb)

* [Risk budget allocation](https://github.com/cvxgrp/cvx_short_course/blob/master/exercises/13.20.ipynb)

* [Energy storage](https://github.com/cvxgrp/cvx_short_course/blob/master/exercises/16.9.ipynb)

* [Vehicle scheduling](https://github.com/cvxgrp/cvx_short_course/blob/master/exercises/3.20.ipynb)

* [Flux balance analysis](https://github.com/cvxgrp/cvx_short_course/blob/master/exercises/17.3.ipynb)




6. If extra time, survey of advanced features
* Quasiconvex programming.
* Log-log convex programming.
* Differentiation through problems.
* Code generation.

7. Conclusion
* Recap.
* References for next steps in learning about and applying convex optimization.

```{nb-exec-table}
```