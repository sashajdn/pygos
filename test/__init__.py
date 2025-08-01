class InterestCalculator:

    def __init__(self, capital, interest_as_perc):
        self.capital = capital
        self.interest_as_perc = interest_as_perc

    def after_n_years(self, n):
        return (self.capital * (1 + (self.interest_as_perc / 100))) ** n


if __name__ == "__main__":
    liquid_starting_capital = 200_000

    etf_ratio, savings_ratio = 0.8, 0.2
    assert etf_ratio + savings_ratio == 1

    etf = InterestCalculator(liquid_starting_capital * etf_ratio, 7)
    savings = InterestCalculator(liquid_starting_capital * savings_ratio, 5)

    years = 5

    etf_after_years = etf.after_n_years(years)
    savings_after_years = savings.after_n_years(years)

    total_capital_after_years = etf_after_years + savings_after_years
    diff = total_capital_after_years - liquid_starting_capital

    print(
        "started with: ",
        liquid_starting_capital,
        "ended with: ",
        total_capital_after_years,
        "diff: ",
        diff,
    )
