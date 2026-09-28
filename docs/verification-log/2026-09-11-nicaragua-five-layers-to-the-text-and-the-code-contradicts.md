# Nicaragua — five layers to the text, and the Code contradicts the guide

> Entry of 2026-09-11 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

The Digesto entry above said the database was live and the code was not yet
located. It is now, and the route is worth writing down because none of the five
steps was guessable from the one before it.

1. The search is a **POST to `/consultas/util/ws/proxy.php`** with
   `hddQueryType=getJuridicNorms` and the serialised form, returning JSON. The
   visible form offers only a norm number and date ranges — there is **no title
   field** — so the way in is a **date range**: the Código de Comercio is 1916 law,
   and 1914–1918 returns 1,219 records, among them *Código de Comercio de
   Nicaragua*, `registro` **"Vigente"**, published 20/10/1916.
2. Each record carries an `iunpid`, base64 of a numeric id — `MjkyOTI=` is 29292.
3. `shownorms.php?idnorm=…` renders the record: *Código N°. s/n*, materia *Empresa,
   Industria y Comercio*. It shows a TEXTO panel and a Download button.
4. **Both are empty.** `hasfileNorm` returns **false** for every `valordominio`,
   and `getVersionHtmlAccordion` returns nothing. The Digesto catalogues this code
   without attaching its text. **A record is not a document**, and stopping here
   would have produced a perfectly defensible "the database has it but does not
   serve it".
5. The text is in the **documentary collection**, reached by a different query —
   `getRddsByIunp` — which returns an `rddid` and a starting page, and
   `pdf.php?type=rdd&rdd=…` then serves **13.7 MB, 323 pages** with an OCR text
   layer. The Code begins at page 35.
