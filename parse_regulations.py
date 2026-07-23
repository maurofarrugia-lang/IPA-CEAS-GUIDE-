#!/usr/bin/env python3
"""
EU Asylum Pact Regulations Parser
Extracts articles and content from regulation HTML
"""

import re
import json
from typing import Dict, List, Any

def parse_article(text: str, reg_id: str) -> List[Dict[str, Any]]:
    """Parse articles from regulation text"""
    articles = []
    
    # Pattern for article headings and content
    # Articles are typically numbered and contain structured content
    article_pattern = r'Article\s+(\d+[a-z]?)\s*\n([^\n]+?)(?=\nArticle|\Z)'
    
    matches = re.finditer(article_pattern, text, re.IGNORECASE | re.DOTALL)
    
    for match in matches:
        article_num = match.group(1)
        title_and_content = match.group(2).strip()
        
        # Try to separate title from content
        lines = title_and_content.split('\n', 1)
        title = lines[0].strip() if lines else ""
        content = lines[1].strip() if len(lines) > 1 else title_and_content
        
        articles.append({
            "article_number": article_num,
            "title": title[:200],  # Limit title length
            "content": content[:5000],  # Limit content length
            "regulation_id": reg_id,
            "keywords": extract_keywords(content)
        })
    
    return articles

def extract_keywords(text: str) -> List[str]:
    """Extract important keywords from text"""
    # Common legal and asylum-related terms
    important_terms = [
        'asylum', 'refugee', 'protection', 'application', 'border', 'screening',
        'procedure', 'applicant', 'international protection', 'third-country',
        'member state', 'detention', 'minor', 'unaccompanied', 'interview',
        'decision', 'appeal', 'Dublin', 'Eurodac', 'fingerprint', 'biometric',
        'reception', 'vulnerability', 'family', 'relocation', 'return',
        'admissibility', 'subsidiary protection', 'persecution', 'safe country'
    ]
    
    keywords = []
    text_lower = text.lower()
    
    for term in important_terms:
        if term in text_lower:
            keywords.append(term)
    
    return keywords[:10]  # Limit to 10 keywords

# Sample regulations data structure
regulations_data = {
    "regulations": [
        {
            "id": "2024_1348",
            "title": "Asylum Procedure Regulation",
            "short_title": "APR",
            "number": "2024/1348",
            "adopted": "2024-05-14",
            "entry_force": "2024-06-11",
            "application": "2026-06-12",
            "eur_lex_url": "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32024R1348",
            "description": "Establishing a common procedure for international protection in the Union",
            "articles": []
        },
        {
            "id": "2024_1356",
            "title": "Screening Regulation",
            "short_title": "Screening",
            "number": "2024/1356",
            "adopted": "2024-05-14",
            "entry_force": "2024-06-11",
            "application": "2026-06-12",
            "eur_lex_url": "https://eur-lex.europa.eu/eli/reg/2024/1356/oj/eng",
            "description": "Introducing the screening of third-country nationals at the external borders",
            "articles": []
        },
        {
            "id": "2024_1358",
            "title": "Eurodac Regulation",
            "short_title": "Eurodac",
            "number": "2024/1358",
            "adopted": "2024-05-14",
            "entry_force": "2024-06-11",
            "application": "2026-06-12",
            "eur_lex_url": "https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:L_202401358",
            "description": "On the establishment of 'Eurodac' for the comparison of biometric data",
            "articles": []
        },
        {
            "id": "2024_1351",
            "title": "Asylum and Migration Management Regulation",
            "short_title": "AMMR",
            "number": "2024/1351",
            "adopted": "2024-05-14",
            "entry_force": "2024-06-11",
            "application": "2026-06-12",
            "eur_lex_url": "https://eur-lex.europa.eu/eli/reg/2024/1351/oj",
            "description": "On asylum and migration management (Dublin IV and solidarity)",
            "articles": []
        },
        {
            "id": "2024_1347",
            "title": "Qualification Regulation",
            "short_title": "QR",
            "number": "2024/1347",
            "adopted": "2024-05-14",
            "entry_force": "2024-06-11",
            "application": "2026-06-12",
            "eur_lex_url": "https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:L_202401347",
            "description": "Standards for qualification as beneficiaries of international protection",
            "articles": []
        },
        {
            "id": "2024_1346",
            "title": "Reception Conditions Directive",
            "short_title": "RCD",
            "number": "2024/1346",
            "adopted": "2024-05-14",
            "entry_force": "2024-06-11",
            "application": "2026-06-12",
            "eur_lex_url": "https://eur-lex.europa.eu/eli/dir/2024/1346/oj/eng",
            "description": "Standards for the reception of applicants for international protection",
            "articles": []
        },
        {
            "id": "2024_1359",
            "title": "Crisis Regulation",
            "short_title": "Crisis",
            "number": "2024/1359",
            "adopted": "2024-05-14",
            "entry_force": "2024-06-11",
            "application": "2026-06-12",
            "eur_lex_url": "https://eur-lex.europa.eu/eli/reg/2024/1359/oj/eng",
            "description": "Addressing situations of crisis and force majeure in migration and asylum",
            "articles": []
        }
    ],
    "euaa_guidelines": [
        {
            "id": "evidence_assessment",
            "title": "Practical Guide on Evidence and Risk Assessment",
            "category": "Examination",
            "url": "https://euaa.europa.eu/publications/practical-guide-evidence-assessment",
            "related_regulations": ["2024_1348"],
            "publication_date": "2024-01"
        },
        {
            "id": "personal_interview",
            "title": "Practical Guide on Personal Interview",
            "category": "Examination",
            "url": "https://euaa.europa.eu/publications/practical-guide-personal-interview",
            "related_regulations": ["2024_1348"],
            "publication_date": "2014-10"
        },
        {
            "id": "qualification",
            "title": "Practical Guide on Qualification for International Protection",
            "category": "Examination",
            "url": "https://euaa.europa.eu/publications/practical-guide-qualification-international-protection",
            "related_regulations": ["2024_1347"],
            "publication_date": "2018-04"
        },
        {
            "id": "registration",
            "title": "Practical Guide on Registration and Lodging",
            "category": "Access",
            "url": "https://euaa.europa.eu/publications/practical-guide-registration-and-lodging-applications-international-protection",
            "related_regulations": ["2024_1348"],
            "publication_date": "2025-12"
        },
        {
            "id": "dublin",
            "title": "Guidance on Dublin Procedure",
            "category": "Dublin",
            "url": "https://euaa.europa.eu/publications/guidance-dublin-procedure",
            "related_regulations": ["2024_1351"],
            "publication_date": "2020-03"
        }
    ]
}

# Save the database
with open('/home/user/asylum-app/database.json', 'w', encoding='utf-8') as f:
    json.dump(regulations_data, f, indent=2, ensure_ascii=False)

print("Database created successfully!")
print(f"Total regulations: {len(regulations_data['regulations'])}")
print(f"Total EUAA guidelines: {len(regulations_data['euaa_guidelines'])}")
