import yfinance as yf

fiveYear = yf.Ticker('^FVX')
fiveYearYield = fiveYear.info['previousClose'] # Establishes Yield
fiveYearImpInfl = (1+fiveYearYield) ** 5 - 1# Calculates Implied Inflation

tenYear = yf.Ticker('^TNX')
tenYearYield = tenYear.info['previousClose']
tenYearImpInfl = (1+tenYearYield) ** 10 - 1

thirtyYear = yf.Ticker('^TYX')
thirtyYearYield = thirtyYear.info['previousClose']
thirtyYearImpInfl = (1+thirtyYearYield) ** 30 - 1



def get_real_return(yld, inflation_guess):
    return (yld - inflation_guess)

def get_imp_infl(yld, desired_return):
    return (yld - desired_return)
