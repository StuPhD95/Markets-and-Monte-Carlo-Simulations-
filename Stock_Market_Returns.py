import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def discrete_GBM(n_RW=50, n_years=10, mu=0.07, sigma=0.15, annual_step_size=12):
    dt = 1/annual_step_size
    n_steps = n_years * annual_step_size
    returns = np.random.normal(loc=((1+ mu)**dt), scale= sigma*np.sqrt(dt), size=(n_steps,n_RW))
    returns = pd.concat([pd.DataFrame(np.ones((1,n_RW))), pd.DataFrame(returns)], ignore_index=True)
    return pd.DataFrame(returns)

S_0 = 100 # initial price

RW = discrete_GBM()
wealth_index = S_0*RW.cumprod()

# Plot
wealth_index.plot(legend = False, figsize = (12,6))
plt.xlabel('Time (months)')
plt.ylabel('Portfolio value ($)')
plt.title('Simulated Portfolio Value Paths Under Geometric Brownian Motion')
