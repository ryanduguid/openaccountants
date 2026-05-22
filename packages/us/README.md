# United States — Tax Skills Index

> **Do not upload this entire folder.** Pick your state below and upload all files from that state's package.

US tax is layered: federal rules apply everywhere, but state obligations depend on where you live or have nexus. Each state package below bundles federal skills **plus** that state's specific rules, so you only load what's relevant.

## Pick Your State

| Code | State | Package | Notes |
|------|-------|---------|-------|
| AL | Alabama | [`us-al`](../us-al/) | Income + sales tax |
| AK | Alaska | [`us-ak`](../us-ak/) | No state income tax, no sales tax |
| AZ | Arizona | [`us-az`](../us-az/) | Income + sales tax |
| AR | Arkansas | [`us-ar`](../us-ar/) | Income + sales tax |
| CA | California | [`us-ca`](../us-ca/) | Full guided flow with intake + return assembly |
| CO | Colorado | [`us-co`](../us-co/) | Income + sales tax |
| CT | Connecticut | [`us-ct`](../us-ct/) | Income + sales tax |
| DC | District of Columbia | [`us-dc`](../us-dc/) | Income + sales tax |
| DE | Delaware | [`us-de`](../us-de/) | Income + gross receipts tax |
| FL | Florida | [`us-fl`](../us-fl/) | No income tax; sales tax + annual report |
| GA | Georgia | [`us-ga`](../us-ga/) | Income + sales tax |
| HI | Hawaii | [`us-hi`](../us-hi/) | Income + sales tax (GET) |
| IA | Iowa | [`us-ia`](../us-ia/) | Income + sales tax |
| ID | Idaho | [`us-id`](../us-id/) | Income + sales tax |
| IL | Illinois | [`us-il`](../us-il/) | Income + sales + estimated tax |
| IN | Indiana | [`us-in`](../us-in/) | Income + sales tax |
| KS | Kansas | [`us-ks`](../us-ks/) | Income + sales tax |
| KY | Kentucky | [`us-ky`](../us-ky/) | Income + sales tax |
| LA | Louisiana | [`us-la`](../us-la/) | Income + sales tax |
| MA | Massachusetts | [`us-ma`](../us-ma/) | Income + sales tax |
| MD | Maryland | [`us-md`](../us-md/) | Income + sales tax |
| ME | Maine | [`us-me`](../us-me/) | Income + sales tax |
| MI | Michigan | [`us-mi`](../us-mi/) | Income + sales tax |
| MN | Minnesota | [`us-mn`](../us-mn/) | Income + sales tax |
| MO | Missouri | [`us-mo`](../us-mo/) | Income + sales tax |
| MS | Mississippi | [`us-ms`](../us-ms/) | Income + sales tax |
| MT | Montana | [`us-mt`](../us-mt/) | Income tax only (no sales tax) |
| NC | North Carolina | [`us-nc`](../us-nc/) | Income + sales tax |
| ND | North Dakota | [`us-nd`](../us-nd/) | Income + sales tax |
| NE | Nebraska | [`us-ne`](../us-ne/) | Income + sales tax |
| NH | New Hampshire | [`us-nh`](../us-nh/) | Interest & dividends tax (repealed 2025) |
| NJ | New Jersey | [`us-nj`](../us-nj/) | Income + sales tax |
| NM | New Mexico | [`us-nm`](../us-nm/) | Income + sales tax (GRT) |
| NV | Nevada | [`us-nv`](../us-nv/) | No income tax; sales + commerce tax |
| NY | New York | [`us-ny`](../us-ny/) | Income + sales + NYC UBT + estimated tax + LLC fee |
| OH | Ohio | [`us-oh`](../us-oh/) | Income + sales + CAT |
| OK | Oklahoma | [`us-ok`](../us-ok/) | Income + sales tax |
| OR | Oregon | [`us-or`](../us-or/) | Income tax only (no sales tax) |
| PA | Pennsylvania | [`us-pa`](../us-pa/) | Income + sales tax |
| RI | Rhode Island | [`us-ri`](../us-ri/) | Income + sales tax |
| SC | South Carolina | [`us-sc`](../us-sc/) | Income + sales tax |
| SD | South Dakota | [`us-sd`](../us-sd/) | No income tax; sales tax |
| TN | Tennessee | [`us-tn`](../us-tn/) | No income tax; sales tax |
| TX | Texas | [`us-tx`](../us-tx/) | No income tax; sales + franchise tax |
| UT | Utah | [`us-ut`](../us-ut/) | Income + sales tax |
| VA | Virginia | [`us-va`](../us-va/) | Income + sales tax |
| VT | Vermont | [`us-vt`](../us-vt/) | Income + sales tax |
| WA | Washington | [`us-wa`](../us-wa/) | No income tax; sales + B&O tax |
| WI | Wisconsin | [`us-wi`](../us-wi/) | Income + sales tax |
| WV | West Virginia | [`us-wv`](../us-wv/) | Income + sales tax |
| WY | Wyoming | [`us-wy`](../us-wy/) | No income tax; sales tax |

## What's in Each State Package

Every state package includes:

- **US workflow base** — the execution framework for US tax work
- **Federal skills** — Schedule C, SE tax, QBI, 1099-NEC, estimated tax, retirement, health insurance, bookkeeping
- **Federal orchestrator** — return assembly and global router
- **State-specific skills** — income tax, sales tax, and any specialty taxes for that state

California (`us-ca`) additionally includes a complete guided intake and return assembly flow.

## For Contributors

Source files live under `skills/` — do not edit files in `packages/` directly.
To improve a state's skills, edit `skills/us-states/[code]/` and run `scripts/build-packages.py`.

---

*OpenAccountants — open-source tax computation skills*
*info@openaaccountants.com*
