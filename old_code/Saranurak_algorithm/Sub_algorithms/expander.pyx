cdef extern from "Algorithm-Engineering-Project/Saranurak_algorithm/Sub_algorithms/expander-decomposition/main.cpp":
    int expander_decomposition(int param1, double param2)

def run_expander(int param1, float param2):
    return expander_decomposition(param1, param2)
