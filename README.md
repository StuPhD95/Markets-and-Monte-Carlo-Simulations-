# Monte Carlo Simulations in Financial Models



**VaR_Monte_Carlo**

This project implements a Monte Carlo Value-at-Risk (VaR) model for a simple equally weighted portfolio. The portfolio consists of five exchange-traded funds (ETFs) stored in the tickers list:
- SPDR S&P 500 ETF Trust (SPY), 
- Vanguard Total Bond Market ETF (BND),
- SPDR Gold Shares (GLD),
- Invesco QQQ Trust (QQQ),
- Vanguard Total Stock Market ETF (VTI).

The model downloads historical price data, computes daily log returns and estimates the portfolio’s expected return and volatility using the historical covariance matrix. It then simulates possible future portfolio profit-and-loss outcomes over a 20-day holding period using normally distributed random shocks. The resulting histogram shows the distribution of simulated portfolio P&L. The red dashed vertical line represents the estimated VaR threshold. At the 95% confidence level, this is the loss level expected to be exceeded in only 5% of simulated scenarios. At the 99% confidence level, the VaR threshold moves further into the left tail, reflecting a more conservative estimate of downside risk. This provides a simple framework for estimating potential portfolio losses under historical volatility and normal return assumptions.

![Monte Carlo VaR histogram](Figures/VaR_95.png)

![Monte Carlo VaR histogram](Figures/VaR_99.png)


