#!/usr/bin/env python3
"""Build self-contained standalone HTML with the full database embedded."""
import json

with open('/home/user/refine/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('/home/user/refine/complete_database.json.txt', 'r', encoding='utf-8') as f:
    db = json.loads(f.read())

# Inject embedded DB + a loadDatabase override BEFORE the main script opens.
inject_block = (
    '<script>\n'
    '/* Auto-generated: full database embedded for offline double-click use */\n'
    'const EMBEDDED_DATABASE = ' + json.dumps(db, ensure_ascii=False, separators=(',', ':')) + ';\n'
    '</script>\n'
)
# Place it just before the main scoped script
final_html = html.replace(
    '    <script>\n    /* =========================================================',
    inject_block + '    <script>\n    /* ========================================================='
)

# Refactor loadDatabase to prefer the embedded DB, fall back to fetch()
old_loader = (
    '    async function loadDatabase() {\n'
    '        try {\n'
    "            const response = await fetch('complete_database.json');\n"
    '            database = await response.json();\n'
    '            displayRegulations(database.regulations);\n'
    '            displayGuidelines(database.euaa_guidelines);\n'
    '            displayProtectionIndex(database.protection_index.categories);\n'
    '            renderCaseFlowTable(buildFlowRows(database));\n'
    '            initializeCaseLawFilters(database.case_law || []);\n'
    '            initializePublications(database.euaa_case_law_publications || []);\n'
    '        } catch (error) {\n'
    "            console.error('Error loading database:', error);\n"
    "            const flowBody = document.getElementById('flowTableBody');\n"
    "            if (flowBody) flowBody.innerHTML = '<tr><td colspan=\"4\" class=\"no-results\"><h3>Error loading database</h3><p>Please check the console for details.</p></td></tr>';\n"
    '        }\n'
    '    }\n'
)
new_loader = (
    '    async function loadDatabase() {\n'
    '        try {\n'
    '            if (typeof EMBEDDED_DATABASE !== "undefined") {\n'
    '                database = EMBEDDED_DATABASE;\n'
    '            } else {\n'
    "                const response = await fetch('complete_database.json');\n"
    '                database = await response.json();\n'
    '            }\n'
    '            displayRegulations(database.regulations);\n'
    '            displayGuidelines(database.euaa_guidelines);\n'
    '            displayProtectionIndex(database.protection_index.categories);\n'
    '            renderCaseFlowTable(buildFlowRows(database));\n'
    '            initializeCaseLawFilters(database.case_law || []);\n'
    '            initializePublications(database.euaa_case_law_publications || []);\n'
    '        } catch (error) {\n'
    "            console.error('Error loading database:', error);\n"
    "            const flowBody = document.getElementById('flowTableBody');\n"
    "            if (flowBody) flowBody.innerHTML = '<tr><td colspan=\"4\" class=\"no-results\"><h3>Error loading database</h3><p>Please check the console for details.</p></td></tr>';\n"
    '        }\n'
    '    }\n'
)
final_html = final_html.replace(old_loader, new_loader)

with open('/home/user/refine/index-standalone.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print('Built standalone:', len(final_html), 'bytes')
