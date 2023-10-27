import numpy as np
import scipy.stats as stats

def corrcheck(x, y):
    correlation_coefficient = np.corrcoef(np.array(x) if not isinstance(x, np.ndarray) else x, np.array(y) if not isinstance(y, np.ndarray) else y)[0, 1]
    n = len(y)
    df = n - 2
    t_statistic = correlation_coefficient * np.sqrt(df / (1 - correlation_coefficient**2))
    alpha = 0.05
    critical_region = stats.t.ppf(1 - alpha/2, df)
    if np.abs(t_statistic) > critical_region:
        return f"The correlation is statistically significant(Correlation coefficient of {correlation_coefficient})"
    else:
        return f"The correlation is not statistically significant(Correlation coefficient of {correlation_coefficient})."