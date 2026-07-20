"""
UAE End of Service Gratuity Calculator
----------------------------------------
Calculates end-of-service gratuity (EOSB) for private sector employees
in the United Arab Emirates, based on Federal Decree-Law No. 33 of 2021.

Rules implemented:
- Employees must complete at least 1 full year of continuous service to
  qualify for gratuity.
- Gratuity is calculated on the "basic salary" only (excluding housing,
  transport, and other allowances).
- For the first 5 years of service: 21 days' basic salary per year.
- For each additional year beyond 5: 30 days' basic salary per year.
- Partial years are calculated on a pro-rata basis.
- Total gratuity is capped at 2 years' total salary (a common
  contractual/legal ceiling referenced in UAE labour guidance).

For the full interactive version with live AED formatting, contract-type
handling, and unlimited/limited contract nuances, see:
https://uaecalculators.ae/gratuity-calculator/
"""

from dataclasses import dataclass


@dataclass
class GratuityResult:
    years_of_service: float
    daily_wage: float
    gratuity_first_5_years: float
    gratuity_after_5_years: float
    total_gratuity: float
    capped: bool


def calculate_gratuity(basic_salary: float, years_of_service: float) -> GratuityResult:
    """
    Calculate UAE end-of-service gratuity.

    Args:
        basic_salary: Monthly basic salary in AED (excluding allowances).
        years_of_service: Total continuous years of service (can be a
            decimal, e.g. 3.5 for 3 years 6 months).

    Returns:
        GratuityResult with a full breakdown of the calculation.

    Raises:
        ValueError: if inputs are invalid or service is under 1 year.
    """
    if basic_salary <= 0:
        raise ValueError("Basic salary must be greater than 0.")
    if years_of_service < 1:
        raise ValueError(
            "Employee is not eligible for gratuity. "
            "Minimum 1 full year of continuous service is required."
        )

    # Daily wage = (basic monthly salary * 12) / 365
    daily_wage = (basic_salary * 12) / 365

    if years_of_service <= 5:
        first_5_years_gratuity = years_of_service * 21 * daily_wage
        after_5_years_gratuity = 0.0
    else:
        first_5_years_gratuity = 5 * 21 * daily_wage
        remaining_years = years_of_service - 5
        after_5_years_gratuity = remaining_years * 30 * daily_wage

    total_gratuity = first_5_years_gratuity + after_5_years_gratuity

    # Common ceiling: gratuity should not exceed 2 years' total salary
    max_cap = basic_salary * 12 * 2
    capped = total_gratuity > max_cap
    if capped:
        total_gratuity = max_cap

    return GratuityResult(
        years_of_service=years_of_service,
        daily_wage=round(daily_wage, 2),
        gratuity_first_5_years=round(first_5_years_gratuity, 2),
        gratuity_after_5_years=round(after_5_years_gratuity, 2),
        total_gratuity=round(total_gratuity, 2),
        capped=capped,
    )


if __name__ == "__main__":
    # Example: employee with AED 10,000 basic salary, 7 years of service
    result = calculate_gratuity(basic_salary=10000, years_of_service=7)

    print("UAE End of Service Gratuity Calculation")
    print("----------------------------------------")
    print(f"Years of service:         {result.years_of_service}")
    print(f"Daily wage (AED):         {result.daily_wage}")
    print(f"Gratuity (first 5 yrs):   AED {result.gratuity_first_5_years}")
    print(f"Gratuity (after 5 yrs):   AED {result.gratuity_after_5_years}")
    print(f"Total gratuity payable:   AED {result.total_gratuity}")
    print(f"Capped at 2-year limit:   {result.capped}")
    print("\nFor the full calculator with live inputs, visit:")
    print("https://uaecalculators.ae/gratuity-calculator/")
