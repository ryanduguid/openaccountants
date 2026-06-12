#!/usr/bin/env node
// Inserts a "General reference only" disclaimer blockquote after the first H1
// in every skill markdown file under skills/. Idempotent: skips files that
// already contain the marker. Run with --apply to write; default is dry-run.
import { readFileSync, writeFileSync, readdirSync, statSync } from "node:fs";
import { join } from "node:path";

const ROOT = "skills";
const APPLY = process.argv.includes("--apply");
const MARKER = "General reference only";
const DISCLAIMER =
  "> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.";

function walk(dir, out = []) {
  for (const name of readdirSync(dir)) {
    const p = join(dir, name);
    const s = statSync(p);
    if (s.isDirectory()) walk(p, out);
    else if (name.endsWith(".md")) out.push(p);
  }
  return out;
}

const files = walk(ROOT);
let changed = 0,
  skipped = 0,
  noH1 = 0,
  nonSkill = 0;
let sample = null;

for (const f of files) {
  const text = readFileSync(f, "utf8");
  // Only real skills (YAML frontmatter). Category READMEs are covered by the
  // top-level README disclaimer.
  if (!text.startsWith("---")) {
    nonSkill++;
    continue;
  }
  if (text.includes(MARKER)) {
    skipped++;
    continue;
  }
  const lines = text.split("\n");
  const i = lines.findIndex((l) => /^#\s+\S/.test(l));
  if (i === -1) {
    noH1++;
    continue;
  }
  // Insert: blank, disclaimer, blank right after the H1 line.
  const next = [...lines.slice(0, i + 1), "", DISCLAIMER, "", ...lines.slice(i + 1)];
  // avoid double blank if the original line after H1 was already blank
  const out = next.filter((l, idx) => !(idx > 0 && next[idx - 1] === "" && l === ""));
  if (!sample) sample = { f, before: lines.slice(i, i + 3), after: out.slice(i, i + 4) };
  if (APPLY) writeFileSync(f, out.join("\n"));
  changed++;
}

console.log(`${APPLY ? "APPLIED" : "DRY RUN"} — ${files.length} md files`);
console.log(`  would change: ${changed}`);
console.log(`  already had disclaimer (skipped): ${skipped}`);
console.log(`  no H1 (skipped): ${noH1}`);
if (sample) {
  console.log(`\nSample: ${sample.f}`);
  console.log("  BEFORE:\n    " + sample.before.join("\n    "));
  console.log("  AFTER:\n    " + sample.after.join("\n    "));
}
