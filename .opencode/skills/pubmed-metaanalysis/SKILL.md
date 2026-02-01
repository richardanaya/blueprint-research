---
name: pubmed-metaanalysis
description: Search PubMed for meta-analyses on a given medical topic using NCBI E-utilities API
license: MIT
compatibility: opencode
metadata:
  audience: researchers
  domain: medical-research
---

## What I Do

Search PubMed for meta-analyses and systematic reviews on medical topics using the NCBI E-utilities API. I help you:

- Find meta-analyses on specific medical conditions, treatments, or interventions
- Retrieve article titles, authors, publication dates, and abstracts
- Filter results to focus on systematic reviews and meta-analyses only

## When to Use Me

Use this skill when you need to:
- Look up meta-analyses on a medical topic
- Find systematic reviews for evidence-based research
- Get an overview of aggregated research on a health topic

## How to Search PubMed for Meta-Analyses

### Step 1: Search for Article IDs

Use the NCBI ESearch API to find meta-analyses. The key is adding the `meta-analysis[pt]` publication type filter.

**Base URL:**
```
https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi
```

**Required Parameters:**
- `db=pubmed` - Search the PubMed database
- `term=<SEARCH_QUERY>+AND+meta-analysis[pt]` - Your search term + meta-analysis filter
- `retmax=20` - Number of results to return (adjust as needed)
- `retmode=json` - Return JSON format

**Example Search URL:**
```
https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=diabetes+treatment+AND+meta-analysis[pt]&retmax=20&retmode=json
```

**Alternative Filters:**
- `systematic+review[pt]` - For systematic reviews
- `(meta-analysis[pt]+OR+systematic+review[pt])` - For both types

### Step 2: Fetch Article Details

Use the NCBI ESummary or EFetch API to get article details using the IDs from Step 1.

**ESummary (for basic info):**
```
https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id=<ID1>,<ID2>,<ID3>&retmode=json
```

**EFetch (for full abstract):**
```
https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=<ID1>,<ID2>,<ID3>&rettype=abstract&retmode=text
```

### Step 3: Parse and Present Results

From ESummary JSON response, extract:
- `title` - Article title
- `authors` - List of authors (use first author + "et al." for brevity)
- `pubdate` - Publication date
- `source` - Journal name
- `uid` - PubMed ID (PMID)

### Complete Example Workflow

1. **Search for meta-analyses on "hypertension treatment":**
   ```
   https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=hypertension+treatment+AND+meta-analysis[pt]&retmax=10&retmode=json
   ```

2. **Get details for returned IDs (e.g., 12345678,23456789):**
   ```
   https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id=12345678,23456789&retmode=json
   ```

3. **Get full abstracts:**
   ```
   https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=12345678,23456789&rettype=abstract&retmode=text
   ```

## Search Tips

### Effective Search Terms
- Use MeSH terms when possible (e.g., `"Diabetes Mellitus, Type 2"[Mesh]`)
- Combine terms with `AND` or `OR`
- Use quotes for exact phrases: `"cognitive behavioral therapy"`

### Common Filters
| Filter | Description |
|--------|-------------|
| `meta-analysis[pt]` | Meta-analyses only |
| `systematic+review[pt]` | Systematic reviews only |
| `review[pt]` | All review articles |
| `free+full+text[filter]` | Only free full-text articles |
| `humans[mh]` | Human studies only |
| `english[la]` | English language only |

### Date Filtering
Add date range to search:
- `2020:2024[dp]` - Publication date range
- `"last 5 years"[dp]` - Relative date

**Example with date filter:**
```
term=cancer+immunotherapy+AND+meta-analysis[pt]+AND+2020:2024[dp]
```

## Output Format

When presenting results, use this format:

```
### Meta-Analyses Found: [N] results

1. **[Title]**
   - Authors: [First Author] et al.
   - Journal: [Journal Name], [Year]
   - PMID: [ID] | Link: https://pubmed.ncbi.nlm.nih.gov/[ID]/

2. **[Title]**
   ...
```

## Rate Limits

- NCBI allows ~3 requests per second - be mindful of this when making multiple searches
- Always URL-encode search terms with special characters
