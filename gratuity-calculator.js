/**
 * UAE End of Service Gratuity Calculator
 * ----------------------------------------
 * Calculates end-of-service gratuity (EOSB) for private sector employees
 * in the United Arab Emirates, based on Federal Decree-Law No. 33 of 2021.
 *
 * Rules implemented:
 * - Minimum 1 full year of continuous service required to qualify.
 * - Gratuity is calculated on "basic salary" only (excluding allowances).
 * - First 5 years: 21 days' basic salary per year of service.
 * - Beyond 5 years: 30 days' basic salary per additional year.
 * - Partial years are pro-rated.
 * - Total gratuity capped at 2 years' total salary.
 *
 * For the full interactive version, see:
 * https://uaecalculators.ae/gratuity-calculator/
 */

/**
 * @param {number} basicSalary - Monthly basic salary in AED (excluding allowances)
 * @param {number} yearsOfService - Total continuous years of service (decimals allowed)
 * @returns {{
 *   yearsOfService: number,
 *   dailyWage: number,
 *   gratuityFirst5Years: number,
 *   gratuityAfter5Years: number,
 *   totalGratuity: number,
 *   capped: boolean
 * }}
 */
function calculateGratuity(basicSalary, yearsOfService) {
  if (basicSalary <= 0) {
    throw new Error("Basic salary must be greater than 0.");
  }
  if (yearsOfService < 1) {
    throw new Error(
      "Employee is not eligible for gratuity. Minimum 1 full year of continuous service is required."
    );
  }

  // Daily wage = (basic monthly salary * 12) / 365
  const dailyWage = (basicSalary * 12) / 365;

  let gratuityFirst5Years;
  let gratuityAfter5Years;

  if (yearsOfService <= 5) {
    gratuityFirst5Years = yearsOfService * 21 * dailyWage;
    gratuityAfter5Years = 0;
  } else {
    gratuityFirst5Years = 5 * 21 * dailyWage;
    const remainingYears = yearsOfService - 5;
    gratuityAfter5Years = remainingYears * 30 * dailyWage;
  }

  let totalGratuity = gratuityFirst5Years + gratuityAfter5Years;

  // Common ceiling: gratuity should not exceed 2 years' total salary
  const maxCap = basicSalary * 12 * 2;
  const capped = totalGratuity > maxCap;
  if (capped) {
    totalGratuity = maxCap;
  }

  const round2 = (n) => Math.round(n * 100) / 100;

  return {
    yearsOfService,
    dailyWage: round2(dailyWage),
    gratuityFirst5Years: round2(gratuityFirst5Years),
    gratuityAfter5Years: round2(gratuityAfter5Years),
    totalGratuity: round2(totalGratuity),
    capped,
  };
}

// Example usage
const result = calculateGratuity(10000, 7);

console.log("UAE End of Service Gratuity Calculation");
console.log("----------------------------------------");
console.log(`Years of service:         ${result.yearsOfService}`);
console.log(`Daily wage (AED):         ${result.dailyWage}`);
console.log(`Gratuity (first 5 yrs):   AED ${result.gratuityFirst5Years}`);
console.log(`Gratuity (after 5 yrs):   AED ${result.gratuityAfter5Years}`);
console.log(`Total gratuity payable:   AED ${result.totalGratuity}`);
console.log(`Capped at 2-year limit:   ${result.capped}`);
console.log("\nFor the full calculator with live inputs, visit:");
console.log("https://uaecalculators.ae/gratuity-calculator/");

// Export for use in Node.js or bundlers
if (typeof module !== "undefined" && module.exports) {
  module.exports = { calculateGratuity };
}
