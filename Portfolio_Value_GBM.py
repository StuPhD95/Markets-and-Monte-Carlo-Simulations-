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

mean_path = wealth_index.mean(axis=1)
lower_band = wealth_index.quantile(0.05, axis=1)
upper_band = wealth_index.quantile(0.95, axis=1)

plt.figure(figsize=(12, 6))
plt.plot(mean_path, label='Mean Portfolio Value')
plt.fill_between(
    wealth_index.index,
    lower_band,
    upper_band,
    alpha=0.2,
    label='5th–95th Percentile Range')
plt.xlabel('Time (months)')
plt.ylabel('Portfolio Value ($)')
plt.title('Mean Simulated Portfolio Value with 5th–95th Percentile Band')
plt.legend()
plt.show()
