// Copyright 2026 Ryan Duguid
// SPDX-License-Identifier: AGPL-3.0-only

import assert from 'node:assert/strict';
import test from 'node:test';

import { frankingAccount } from './index.mjs';

const input = {
  year: '2025-26', entity: 'public', rate: '30', opening: '0', rdForward: '0',
  events: [], distributions: [],
};

test('ATO EKW example applies the offset reduction only to the attributable deficit', () => {
  const result = frankingAccount({
    ...input, opening: '10000',
    events: [
      { date: '2025-10-28', type: 'payg_instalment', amount: '125000' },
      { date: '2025-11-15', type: 'income_tax_refund', amount: '60000' },
      { date: '2026-02-28', type: 'payg_instalment', amount: '125000' },
      { date: '2026-03-31', type: 'streaming_determination', amount: '20000' },
      { date: '2026-04-28', type: 'payg_instalment', amount: '250000' },
    ],
    distributions: [{ date: '2025-09-30', amount: '1190000', credit: '510000' }],
  });
  assert.equal(result.credits, '500000.00');
  assert.equal(result.fdt, '80000.00');
  assert.equal(result.reduction, '18000.00');
  assert.equal(result.offset, '62000.00');
  assert.equal(result.labelK, '20000.00');
});

test('ATO Salomon example computes over-franking tax against the first distribution', () => {
  const result = frankingAccount({
    ...input, entity: 'private', opening: '1000',
    distributions: [
      { date: '2025-08-01', amount: '700', credit: '120' },
      { date: '2026-03-01', amount: '500', credit: '214.29' },
    ],
  });
  assert.equal(result.periods[0].benchmark, '40.00');
  assert.equal(result.distributions[1].maximum, '214.29');
  assert.equal(result.oft, '128.57');
  assert.equal(result.closing, '665.71');
  assert.equal(result.due, '2026-07-31');
});

test('public benchmark resets in January and records a significant variation', () => {
  const result = frankingAccount({
    ...input, opening: '1000',
    distributions: [
      { date: '2025-08-01', amount: '700', credit: '300' },
      { date: '2025-11-01', amount: '700', credit: '150' },
      { date: '2026-01-01', amount: '700', credit: '0' },
    ],
  });
  assert.equal(result.distributions[1].underFrankingDebit, '150.00');
  assert.deepEqual(result.periods.map(row => row.benchmark), ['100.00', '0.00']);
  assert.equal(result.variation, true);
  assert.equal(result.required, true);
  assert.equal(result.closing, '400.00');
});

test('late refunds retain actual year-end figures and each added deficit', () => {
  const result = frankingAccount({
    ...input, opening: '10', rdForward: '2',
    events: [
      { date: '2026-09-30', type: 'income_tax_refund', amount: '8' },
      { date: '2026-07-01', type: 'income_tax_refund', amount: '10' },
      { date: '2026-07-31', type: 'income_tax_refund', amount: '16', rdPart: '3' },
    ],
  });
  assert.equal(result.yearEndBalance, '10.00');
  assert.equal(result.closing, '-11.00');
  assert.equal(result.yearEndRdDeferral, '2.00');
  assert.equal(result.rdCarried, '5.00');
  assert.equal(result.fdtFromRefunds, '11.00');
  assert.equal(result.required, true);
  assert.equal(result.due, null);
  assert.deepEqual(result.refunds.map(({ date, taken, fdtAdded, dueOtherwise }) => [date, taken, fdtAdded, dueOtherwise]), [
    ['2026-07-31', true, '3.00', '2026-08-14'],
    ['2026-09-30', true, '8.00', '2026-10-14'],
    ['2026-07-01', false, null, null],
  ]);
});

test('the next year uses the actual refund date and credits incremental FDT once', () => {
  const refund = { date: '2026-07-18', type: 'income_tax_refund', amount: '105', rdPart: '5' };
  const first = frankingAccount({ ...input, opening: '50', events: [refund] });
  assert.equal(first.fdtFromRefunds, '50.00');
  const second = frankingAccount({
    ...input, year: '2026-27', opening: first.yearEndBalance, rdForward: first.yearEndRdDeferral,
    events: [
      { date: '2026-07-17', type: 'payg_instalment', amount: '10' },
      refund,
      { date: refund.date, type: 'prior_year_refund_fdt', amount: first.fdtFromRefunds },
    ],
  });
  assert.deepEqual(second.ledger.map(({ balance }) => balance), ['60.00', '-40.00', '10.00']);
  assert.equal(second.yearEndRdDeferral, '5.00');
  assert.equal(second.fdt, '0.00');
});

test('ordinary annual deadline and further-return window are separately identified', () => {
  const result = frankingAccount({
    ...input,
    events: [
      { date: '2026-06-30', type: 'streaming_determination', amount: '1' },
      ...['2026-07-17', '2026-07-18', '2026-08-01'].map(date => ({
        date, type: 'income_tax_refund', amount: '1',
      })),
    ],
  });
  assert.equal(result.due, '2026-07-31');
  assert.deepEqual(result.refunds.map(({ dueWithReturn, withinFurtherReturnWindow }) => [dueWithReturn, withinFurtherReturnWindow]), [
    ['2026-07-31', false], ['2026-07-31', true], [null, false],
  ]);
});

test('R&D deferral absorbs later PAYG and leaves the excess as a credit', () => {
  const result = frankingAccount({
    ...input,
    events: [
      { date: '2025-08-01', type: 'income_tax_refund', amount: '45', rdPart: '45' },
      { date: '2025-11-01', type: 'payg_instalment', amount: '36' },
      { date: '2026-02-01', type: 'income_tax_paid', amount: '30' },
    ],
  });
  assert.equal(result.debits, '0.00');
  assert.equal(result.credits, '21.00');
  assert.equal(result.rdCarried, '0.00');
});

test('large ledger totals keep the last cent in JSON', () => {
  const events = Array.from({ length: 100 }, () => ({
    date: '2025-07-01', type: 'payg_instalment', amount: '1000000000000',
  }));
  events.push({ date: '2025-07-02', type: 'payg_instalment', amount: '0.01' });
  const result = JSON.parse(JSON.stringify(frankingAccount({ ...input, events })));
  assert.equal(result.closing, '100000000000000.01');
  assert.equal(result.ledger.at(-1).balance, result.closing);
});

test('invalid or incomplete inputs stop the worksheet', () => {
  assert.throws(() => frankingAccount(null), /supply an object/);
  assert.throws(() => frankingAccount({ ...input, year: '2027-28' }), /income year/);
  assert.throws(() => frankingAccount({ ...input, determination: 'false' }), /must be a boolean/);
  assert.throws(() => frankingAccount({ ...input, periodsSince: '2' }), /both lastBenchmark and periodsSince/);
  assert.throws(() => frankingAccount({ ...input, taxBefore: '900' }), /both taxBefore and offsetForward/);
  assert.throws(() => frankingAccount({ ...input, events: [{ date: '2026-07-01', type: 'dmt_refund', amount: '10' }] }), /Event 1: enter a date/);
  assert.throws(() => frankingAccount({ ...input, events: [{ date: '2026-02-30', type: 'income_tax_refund', amount: '10' }] }), /Event 1: enter a date/);
  assert.throws(() => frankingAccount({ ...input, events: [{ date: '2026-10-01', type: 'income_tax_refund', amount: '10' }] }), /Event 1: enter a date/);
  assert.throws(() => frankingAccount({ ...input, events: [{ date: '2025-07-01', type: 'constructor', amount: '10' }] }), /Event 1: choose what it is/);
  assert.throws(() => frankingAccount({ ...input, distributions: [{ date: '2025-07-01', amount: '10', credit: '0.001' }] }), /Distribution 1’s franking credit/);
  assert.throws(() => frankingAccount({ ...input, distributions: [{ date: '2025-07-01', amount: '10', credit: '0', frankable: false }] }), /unknown field frankable/);
});
