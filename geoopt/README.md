# geoopt

## `layers`

**Experimental**

Pytorch layers useable in torch models. All layers inherit from `torch.nn.Module`

* Lorentz Model -- Fully Connected Layer, Batch Normalization
* Proper Velocity -- Multinomial Logistic Regression, Fully Connected Layer, Gyrogroup Batch Normalization
* Stereographic Model -- Distances to Stereographic Hyperplanes

## `linalg`

Linear algebra operations implemented using torch.jit and torch tensor operations.

Operations on symmetric matrices.

```py
__all__ = [
    "svd",
    "qr",
    "sym",
    "extract_diag",
    "matrix_rank",
    "expm",
    "trace",
    "block_matrix",
    "sym_funcm",
    "sym_expm",
    "sym_logm",
    "sym_sqrtm",
    "sym_invm",
    "sym_inv_sqrtm1",
    "sym_inv_sqrtm2",
]
```

## `manifolds`

Manifold base class, manifold concrete implementations.

All manifolds are implemented as `torch.nn.Module` subclasses and are to be used as a component
of a pytorch model.

All related math functions can be found under `manifolds/<xxx>/math.py`.

* Stereographic Manifold, Poincare Ball, Sphere Projection
* Birkhoff Polytope
* Euclidean
* Product Manifold, Stereographic Product Manifold
* Scaled Manifold -- scale all distances on an existing manifold
* Sphere
* Sphere Exact (-- retraction is an exact exponential map)
* Stiefel -- Canonical (default), Euclidean, Eclidean Exact (-- retraction is an exact exponential map)
* Symmetric Positive Definite Manifold
* Siegel Manifold (Bounded Domain, Upper Half, Riemannian Metric, Finsler One Metric, Finsler Infinity Metric, Finsler Minimum Entropy, Finsler Weighted Sum)

```py
ball = geoopt.Stereographic(-1)

layer = torch.nn.Sequential(
    Distance2StereographicHyperplanes(2, 10, ball=ball),
    torch.nn.Linear(10, 32),
    torch.nn.ReLU(),
    torch.nn.Linear(32, 64),
)
input = ball.random_normal(100, 2)
```

## `optim`

Pytorch optimizers

* Riemannian Adam
* Riemannian Line Search
* Riemannian Stochastic Gradient Descent
* Sparse Riemannian Stochastic Gradient Descent -- lazy version for sparse gradients

## `sampler`

Samplers, implemented as optimizers for reasons beyond my current comprehension

* Riemannian Hamiltonian Monte-Carlo
* Riemannian Stochastic Gradient Langevin Dynamics
* Stochastic Gradient Riemannian Hamiltonian Monte-Carlo
