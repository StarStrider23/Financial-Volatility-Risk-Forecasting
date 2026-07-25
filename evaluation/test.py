import numpy as np

# Kupiec test

def kupiec_test(violations, alpha=0.05):
    T = len(violations)
    x = sum(violations)
    p_hat = x/T
    LR = -2 * ( 
        (T - x) * np.log((1 - alpha) / (1 - p_hat)) + 
        x * np.log(alpha / p_hat) 
        )
    LR = float(LR)

    return LR

# Christoffersen test

def christofferesen_test(violations):

    violations = [int(x) for x in violations]

    N00 = N01 = N10 = N11 = 0

    for i in range(1, len(violations)):
        if violations[i-1] == 0 and violations[i] == 0:
            N00 += 1
        elif violations[i-1] == 0 and violations[i] == 1:
            N01 += 1
        elif violations[i-1] == 1 and violations[i] == 0:
            N10 += 1
        elif violations[i-1] == 1 and violations[i] == 1:
            N11 += 1

    # Transition probabilities
    pi0 = N01 / (N00 + N01) if (N00 + N01) > 0 else 0
    pi1 = N11 / (N10 + N11) if (N10 + N11) > 0 else 0
    
    # Unconditional probability
    pi = (N01 + N11) / (N00 + N01 + N10 + N11)

    # Likelihood under independence
    L_ind = ((1 - pi) ** (N00 + N10)) * (pi ** (N01 + N11))
    
    # Likelihood under Markov (dependence)
    L_dep = ((1 - pi0) ** N00) * (pi0 ** N01) * ((1 - pi1) ** N10) * (pi1 ** N11)
    
    LR = -2 * np.log(L_ind / L_dep)

    LR = float(LR)
    
    return LR, (N00, N01, N10, N11), (pi0, pi1, pi)