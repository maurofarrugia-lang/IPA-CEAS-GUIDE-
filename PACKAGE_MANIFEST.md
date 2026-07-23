# Package Manifest (Case Law Enabled v3)

## New in v3
- Added **Search on EUAA (query)** button: opens EUAA Case Law search results for the typed query.
- Added **EUAA Quarterly Overview of Asylum Case Law** section with search + theme filtering.

## Data fields
- `case_law[].euaa_url` should be the **exact EUAA case page** or a permanent link (e.g., viewcaselaw.aspx?CaseLawID=...).
- `euaa_case_law_publications[]` stores quarterly overview issues with `url` and `pdf_url`.

## Quick test
1. Open the site.
2. Go to **📚⚖️ EUAA Case Law**.
3. Type a query (e.g., detention) and click **🔎 Search on EUAA (query)**.
4. Scroll to **📰 EUAA Quarterly Overview** and search by themes.
