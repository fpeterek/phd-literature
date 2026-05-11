
hierarchical_c = 1.68     # 840.775647 / 500
hierarchical_cuda = 2.19  # 21.88 / 10

tm_c = (61, 9)
tm_cuda = (5, 3)

conv_c = (403, 539)
conv_cuda = (14, 9)

cair = 'https://github.com/cair'
artem_hnilov = 'https://github.com/BooBSD'
aphoulady = 'https://github.com/adrianphoulady'

# Simulators

warehouse = f'{cair}/deep-warehouse'
rts_game = f'{cair}/deep-rts'

# Implementations

# Main repo with a basic overview, basic implementation,
# links to other sources and repositories, etc.
tm = f'{cair}/TsetlinMachine'

# Unified, as in a comprehensive repository that appears to be behind
# the other repositories and has not been updated for a year
tmu = f'{cair}/tmu'

tm_c = f'{cair}/TsetlinMachineC'
tm_py_bindings = f'{cair}/pyTsetlinMachine'
tm_cuda = f'{cair}/PyTsetlinMachineCUDA'
tm_bitwise_op = f'{cair}/fast-tsetlin-machine-with-mnist-demo'
tm_bitwise_cuda = f'{cair}/fast-tsetlin-machine-in-cuda-with-imdb-demo'

# Also includes convolutional, regression, weighted
parallel_tm = f'{cair}/pyTsetlinMachineParallel'

# Very fast
fuzzy_pattern = f'{artem_hnilov}/Tsetlin.jl'

# Fewer clauses, smaller models
weighted_tm = f'{aphoulady}/weighted-tsetlin-machine-cpp'

# Includes CUDA
graph_tm = f'{cair}/GraphTsetlinMachine'

hierarch_c = f'{cair}/HierarchicalTsetlinMachine'
hierarch_cuda = f'{cair}/PyHierarchicalTsetlinMachineCUDA'

# Tsetlin Machines in NLP
logical_transformer = f'{cair}/LogicalTransformer'

sparse_coalesced = f'{cair}/PySparseCoalescedTsetlinMachineCUDA'

recently_updated = [
    hierarch_cuda, graph_tm, sparse_coalesced, hierarch_c,
    tm_c, warehouse
]
