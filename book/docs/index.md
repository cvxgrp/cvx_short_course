# CVX Short Course

## Convex optimization overview

   * Mathematical optimization
   * Convex optimization
   * Solvers & modeling languages
   * CVXPY example
   * Real-world applications

## [Hello world](hello.md)


## Constructive convex analysis
   * Mathematically define convex, concave, and affine functions. Give many examples.
   * Introduce the composition rule for convex, concave, and affine functions, which generates the grammar for
     CVXPY.
   * Introduce Disciplined Convex Programming (DCP).
   * Learn how to construct convex optimization problems using DCP in CVXPY.


## Applications of convex optimization

   * Present applications in finance, machine learning, vehicle control, and risk analysis.
   * For each application, the instructors will give a motivating overview, and participants will then code up and solve
   a problem arising in the application using CVXPY. Concretely, exercises will consist of notebooks with missing
   sections, which the participants need to fill in with code constructing and solving a CVXPY problem.
   * [Simple portfolio optimization](exercises/notebooks/13.3)
   * [Portfolio rebalancing](exercises/notebooks/13.21)
   * [Multiple risk models](exercises/13.22)
   * [Risk budget allocation](exercises/13.20)
   * [Energy storage](exercises/16.9)
   * [Vehicle scheduling](exercises/3.20)
   * [Flux balance analysis](exercises/17.3)


## Advanced features

   * Quasiconvex programming.
   * Log-log convex programming.
   * Differentiation through problems.
   * Code generation. 


## Conclusion

   * Recap.
   * References for next steps in learning about and applying convex optimization.

```{nb-exec-table}
```

## Local execution

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
please run (from with the virtual environment) 

```bash
python test.py 
```