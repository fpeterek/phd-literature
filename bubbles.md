## BubbleML

* Dataset
* Boiling water
* Either in a pool (i.e. reactor cooling) or moving through a tube (i.e. GPU cooling)
* Can be visualized, used to train optical flow models
* Dataset is generated using Flash-X simulator

## Flash-X

* Written in Fortran 90
* I was unable to compile the project

## OpenFOAM

* FOSS CFD software
* Written in C++
* Has a custom configuration language
* [Naval Hydro Pack](https://openfoam-extend.sourceforge.net/OpenFOAM_Workshops/OFW11_2016_Guimaraes/special.html) -- wave modelling

```
The Naval Hydro Pack extends the capabilities of foam-extend in naval hydrodynamics CFD
applications, such as wave and current loading on fixed and floating ship hulls and off-shore
structures, coastal wave dynamics and wave scour simulations.
```

* Includes [bubble rising simulation](https://youtu.be/JYHhF25OTm0?si=HZUa6RyNLfA-dG-9&t=1993)
* PyFoamSetup
    * A Python library to setup OpenFOAM simulations
* Often brought up during internet discussions
* Probably the best option, though may be difficult to set up and get going

## Fluidsim

* [Python library](https://fluidsim.readthedocs.io/en/latest/)
* Has multiple [papers](https://openresearchsoftware.metajnl.com/articles/10.5334/jors.239) published about the library
* Promises to be performant (usage of Numpy, compiled code, etc.)

```
As a general CFD framework, fluidsim could be compared to OpenFOAM (a CFD framework based on
finite-volume methods). However, in contrast to OpenFOAM, the current version of fluidsim is highly
specialized in pseudo-spectral Fourier methods and it is not adapted for industrial CFD.
```

## CFDTool

* Matlab toolbox
* Also integrates OpenFOAM
* Commercial project (paid license)
* Can use multiple CFD solvers (one of them being OpenFOAM)

## FluidX3D

* Lattice Boltzmann Method
* Free for academic purposes
* Not available for commercial use without prior permission
* [Related paper](https://www.researchgate.net/publication/362275548_Accuracy_and_performance_of_the_lattice_Boltzmann_method_with_64-bit_32-bit_and_customized_16-bit_number_formats) studied the accuracy of LBM with floats of different width
* Implements rendering

## SPH-EXA

* Smooth particle hydrodynamics
* Lagrangian method
* C++20
* [Associated paper](https://dl.acm.org/doi/10.1145/3394277.3401855)

## Lethe

* [Paper](https://link.springer.com/article/10.1007/s40571-022-00478-6)
* And many others, often mentioned in papers during comparisons (Lethe paper mentions multiple)
