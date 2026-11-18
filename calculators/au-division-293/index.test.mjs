import test from "node:test";
import assert from "node:assert/strict";
import { estimateDivision293 } from "./index.mjs";
import rules from "./rules.json" with { type: "json" };

const base = {
  incomeYear: "2026-27",
  taxableIncome: "0",
  assessableFhssReleasedAmount: "0",
  familyTrustDistributionAmounts: "0",
  reportableFringeBenefitsTotal: "0",
  netFinancialInvestmentLoss: "0",
  netRentalPropertyLoss: "0",
  superLumpSumZeroRateAmount: "0",
  lowTaxContributedAmounts: "0",
  excessConcessionalContributions: "0",
  definedBenefitInterest: false,
  constitutionallyProtectedFund: false,
  commonwealthJustice: false,
  departingAustraliaSuperannuationPayment: false,
};
const check = (changes = {}) => estimateDivision293({ ...base, ...changes });
const figures = ["incomeYear", "liable", "division293Income", "lowTaxContributions", "combinedAmount", "excessOverThreshold", "taxableContributions", "division293TaxEstimate"];
const stopped = (result, verdict, code) => {
  assert.equal(result.verdict, verdict);
  assert.deepEqual(result.reason_codes, [code]);
  for (const key of figures) assert.equal(result[key], null);
};

test("ATO example: Jan's $240,000 and $15,000 give $5,000 taxable and $750 tax", () => {
  for (const incomeYear of rules.supported_years) {
    const result = check({ incomeYear, taxableIncome: "240000", lowTaxContributedAmounts: "15000" });
    assert.equal(result.verdict, "estimate_calculated");
    assert.equal(result.division293Income, "240000.00");
    assert.equal(result.combinedAmount, "255000.00");
    assert.equal(result.excessOverThreshold, "5000.00");
    assert.equal(result.taxableContributions, "5000.00");
    assert.equal(result.division293TaxEstimate, "750.00");
    assert.equal(result.liable, true);
    assert.deepEqual(result.reason_codes, ["caller_attested_inputs", "liable"]);
    assert.doesNotThrow(() => JSON.stringify(result));
  }
});

test("$250,000.00 exactly is not over the threshold; each cent above is, rounded half away from zero", () => {
  const at = check({ taxableIncome: "230000", lowTaxContributedAmounts: "20000" });
  assert.equal(at.liable, false);
  assert.equal(at.taxableContributions, "0.00");
  assert.equal(at.division293TaxEstimate, "0.00");
  assert.deepEqual(at.reason_codes, ["caller_attested_inputs", "not_above_threshold"]);
  for (const [taxableIncome, taxable, tax] of [
    ["230000.01", "0.01", "0.00"], ["230000.03", "0.03", "0.00"], ["230000.04", "0.04", "0.01"],
    ["230000.10", "0.10", "0.02"], ["230000.30", "0.30", "0.05"], ["230001", "1.00", "0.15"],
  ]) {
    const result = check({ taxableIncome, lowTaxContributedAmounts: "20000" });
    assert.equal(result.taxableContributions, taxable, taxableIncome);
    assert.equal(result.division293TaxEstimate, tax, taxableIncome);
    assert.equal(result.liable, true);
  }
});

test("the taxable contributions are the lesser of the low tax contributions and the excess", () => {
  const result = check({ taxableIncome: "300000", lowTaxContributedAmounts: "20000" });
  assert.equal(result.excessOverThreshold, "70000.00");
  assert.equal(result.taxableContributions, "20000.00");
  assert.equal(result.division293TaxEstimate, "3000.00");
});

test("nil low tax contributions give no taxable contributions, whatever the income", () => {
  const result = check({ taxableIncome: "400000" });
  assert.equal(result.excessOverThreshold, "150000.00");
  assert.equal(result.taxableContributions, "0.00");
  assert.equal(result.liable, false);
  assert.deepEqual(result.reason_codes, ["caller_attested_inputs", "no_low_tax_contributions"]);
  const allExcess = check({ taxableIncome: "400000", lowTaxContributedAmounts: "40000", excessConcessionalContributions: "40000" });
  assert.equal(allExcess.lowTaxContributions, "0.00");
  assert.equal(allExcess.liable, false);
});

test("excess concessional contributions come off the low tax contributed amounts", () => {
  const result = check({ taxableIncome: "260000", lowTaxContributedAmounts: "40000", excessConcessionalContributions: "7500" });
  assert.equal(result.lowTaxContributions, "32500.00");
  assert.equal(result.combinedAmount, "292500.00");
  assert.equal(result.taxableContributions, "32500.00");
  assert.equal(result.division293TaxEstimate, "4875.00");
  stopped(check({ lowTaxContributedAmounts: "7499.99", excessConcessionalContributions: "7500" }), "unknown", "components_inconsistent");
});

test("Division 293 income adds and subtracts each surcharge income component, without super contributions", () => {
  const result = check({
    taxableIncome: "200000",
    assessableFhssReleasedAmount: "10000",
    familyTrustDistributionAmounts: "5000",
    reportableFringeBenefitsTotal: "20000",
    netFinancialInvestmentLoss: "3000",
    netRentalPropertyLoss: "7000",
    superLumpSumZeroRateAmount: "15000",
    lowTaxContributedAmounts: "50000",
    reportableSuperannuationContributions: "50000",
  });
  assert.equal(result.division293Income, "210000.00");
  assert.equal(result.combinedAmount, "260000.00");
  assert.equal(result.taxableContributions, "10000.00");
  assert.equal(result.division293TaxEstimate, "1500.00");
});

test("taxable income without the FHSS amount and with the family trust amounts is floored at nil only once", () => {
  assert.equal(check({ taxableIncome: "10000", assessableFhssReleasedAmount: "15000", familyTrustDistributionAmounts: "20000" }).division293Income, "15000.00");
  assert.equal(check({ taxableIncome: "10000", assessableFhssReleasedAmount: "15000" }).division293Income, "0.00");
  assert.equal(check({ assessableFhssReleasedAmount: "15000", reportableFringeBenefitsTotal: "1000" }).division293Income, "1000.00");
  stopped(check({ familyTrustDistributionAmounts: "1" }), "unknown", "taxable_income_indeterminate");
  assert.equal(check({ taxableIncome: "10000", superLumpSumZeroRateAmount: "20000" }).division293Income, "-10000.00");
});

test("each exclusion is refused when true and has no figure when not stated", () => {
  for (const [key, code] of [
    ["definedBenefitInterest", "defined_benefit_interest"],
    ["constitutionallyProtectedFund", "constitutionally_protected_fund"],
    ["commonwealthJustice", "commonwealth_justice"],
    ["departingAustraliaSuperannuationPayment", "departing_australia_payment"],
  ]) {
    stopped(check({ [key]: true }), "refused", code);
    stopped(check({ [key]: undefined }), "unknown", code);
    stopped(check({ [key]: "false" }), "unknown", code);
  }
});

test("unsupported years and malformed or missing amounts give no figure", () => {
  for (const incomeYear of ["2023-24", "2027-28", "2026/27", 2026, undefined]) stopped(check({ incomeYear }), "refused", "unsupported_year");
  for (const key of Object.keys(base).filter((name) => typeof base[name] === "string" && name !== "incomeYear")) {
    for (const value of [undefined, "", "-1", "1.234", "1e6", "01", 1000, "1,000"]) stopped(check({ [key]: value }), "unknown", "invalid_money");
  }
  for (const input of [null, [], "facts"]) stopped(estimateDivision293(input), "unknown", "invalid_input");
});

test("rules: the $250,000 threshold and the 15% rate", () => {
  assert.equal(rules.threshold, "250000");
  assert.equal(rules.rate_percent, 15);
});
