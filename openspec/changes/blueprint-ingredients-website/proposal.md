# Proposal: Blueprint Ingredients Meta-Analysis Website

## Why

Blueprint supplements by Bryan Johnson contain over 40 clinically-backed ingredients with specific dosages, but consumers lack a centralized, research-backed resource to understand the scientific evidence behind each ingredient's benefits. A comprehensive website with meta-analysis data and benefit ratings will empower users to make informed decisions about their supplement regimen.

## What Changes

- Create a modern, responsive website showcasing all Blueprint supplement ingredients
- Build individual ingredient pages with meta-analysis research lookup
- Implement benefit tables with clinically relevant dosages, ratings (1-10), impact levels, and source citations
- Design a beautiful, intuitive user interface with search and filter capabilities
- Integrate PubMed API for real-time meta-analysis data retrieval
- Support mobile and desktop responsive layouts
- Deploy to production environment (Vercel or similar)

## Capabilities

### New Capabilities
- `ingredient-directory`: Comprehensive listing of all Blueprint ingredients with search/filter
- `ingredient-profile-page`: Individual ingredient pages with detailed research information
- `meta-analysis-integration`: PubMed API integration for retrieving meta-analysis data
- `benefit-rating-system`: Algorithmic rating of benefits based on clinical evidence
- `responsive-ui`: Mobile-first responsive design with modern aesthetics
- `search-filter`: Full-text search and category filtering for ingredients

### Modified Capabilities
- *No existing capabilities to modify*

## Impact

- **Frontend**: React/Next.js application with TypeScript
- **Backend**: Next.js API routes for PubMed integration
- **Database**: Optional PostgreSQL for caching meta-analysis results
- **APIs**: NCBI E-utilities API for PubMed searches
- **Deployment**: Vercel for serverless deployment
- **Styling**: Tailwind CSS with modern design system
