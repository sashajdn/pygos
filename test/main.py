class InterestCalculator:

    def __init__(self, capital, interest_as_perc):
        self.capital = capital
        self.interest_as_perc = interest_as_perc

    def after_n_years(self, n):
        if n == 0:
            return self.capital

        return (1 + (self.interest_as_perc / 100)) * self.after_n_years(n - 1)


if __name__ == "__main__":
    liquid_starting_capital = 300_000

    etf_ratio, savings_ratio = 0.8, 0.2
    assert etf_ratio + savings_ratio == 1

    etf_expected_yoy = 7
    savings_expected_yoy = 5

    etf = InterestCalculator(liquid_starting_capital * etf_ratio, etf_expected_yoy)
    savings = InterestCalculator(
        liquid_starting_capital * savings_ratio, savings_expected_yoy
    )

    years = 10
    total_months = years * 12

    etf_after_years = etf.after_n_years(years)
    savings_after_years = savings.after_n_years(years)

    total_capital_after_years = etf_after_years + savings_after_years
    diff = total_capital_after_years - liquid_starting_capital

    max_monthly_spend = diff / total_months

    print("===================================")
    print("years: ", years)
    print("etf yoy", etf_expected_yoy)
    print("savings_yoy", savings_expected_yoy)
    print("etf_ratio: ", etf_ratio)
    print("savings_ratio: ", savings_ratio)
    print("years: ", years)
    print("===================================")

    print(
        "started with: ",
        liquid_starting_capital,
        "ended with: ",
        total_capital_after_years,
        "diff: ",
        diff,
    )

    print(
        "max_monthly_spend: ",
        max_monthly_spend,
        "total_capital_required_without_lost",
        liquid_starting_capital + diff,
    )
