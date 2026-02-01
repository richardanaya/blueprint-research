# Design: Blueprint Ingredients Meta-Analysis Website

## Context

This website will showcase 40+ ingredients from Blueprint supplements with meta-analysis data from PubMed. The application needs to be fast, beautiful, and provide reliable research-backed information. All data will be sourced from PubMed's E-utilities API.

**Technology Stack Decision**: Next.js 15 with App Router, TypeScript, Tailwind CSS, deployed on Vercel. This provides:
- Server-side rendering for SEO and fast initial loads
- API routes for PubMed integration without separate backend
- Type safety throughout the stack
- Modern React patterns with Server Components

## Goals / Non-Goals

**Goals:**
- Create a fast, beautiful website showcasing all Blueprint ingredients
- Display meta-analysis data with proper citations from PubMed
- Provide benefit ratings based on clinical evidence
- Ensure mobile-responsive design
- Deploy to production with CI/CD

**Non-Goals:**
- User authentication or accounts
- E-commerce or purchasing functionality
- Real-time data updates (daily cache is sufficient)
- Admin dashboard for content management

## Decisions

### Decision 1: Static Site Generation vs Server-Side Rendering
**Choice**: Use Static Site Generation (SSG) with Incremental Static Regeneration (ISR)
**Rationale**: Ingredient data changes infrequently. ISR allows daily updates without full rebuilds while maintaining fast page loads.

### Decision 2: PubMed API Integration Strategy
**Choice**: Server-side API calls during build time, cached for 24 hours
**Rationale**: PubMed API has rate limits. Caching prevents hitting limits and improves performance. Fallback to static data if API unavailable.

### Decision 3: Database vs Static JSON
**Choice**: Static JSON files for ingredient data, Supabase optional for caching meta-analysis results
**Rationale**: Ingredient data is relatively static. JSON files are fast and don't require database management. Supabase can cache expensive PubMed queries.

### Decision 4: Component Architecture
**Choice**: Shadcn/ui components with custom styling
**Rationale**: Pre-built accessible components speed development. Tailwind CSS allows rapid custom styling.

### Decision 5: State Management
**Choice**: React Server Components + URL state for filters
**Rationale**: Minimal client-side state needed. URL-based filtering allows shareable links and back-button support.

## Risks / Trade-offs

**[Risk]** PubMed API rate limits or downtime → **Mitigation**: Implement caching layer with Redis/Supabase, fallback to static snapshot data

**[Risk]** Large bundle size with 40+ ingredient pages → **Mitigation**: Use dynamic imports for ingredient detail pages, lazy load meta-analysis tables

**[Risk]** SEO challenges with client-side rendered meta-analysis data → **Mitigation**: Pre-render summary data server-side, load detailed analysis client-side

**[Risk]** Scientific accuracy of benefit ratings → **Mitigation**: Transparent methodology, show confidence levels, link to source studies

**[Trade-off]** Freshness vs Performance: Daily ISR provides balance but data may be up to 24 hours stale

## Migration Plan

1. **Phase 1**: Build ingredient directory and profile pages with static data
2. **Phase 2**: Integrate PubMed API for meta-analysis lookup
3. **Phase 3**: Add search, filter, and rating system
4. **Phase 4**: Performance optimization and SEO
5. **Phase 5**: Deploy to Vercel with CI/CD

**Rollback**: Deploy to separate branch/preview URL first. Rollback by reverting git commit.

## Open Questions

1. Should we implement user contribution features for crowd-sourced reviews?
2. Do we need pagination for the meta-analysis results table?
3. Should we add a comparison tool to compare multiple ingredients?
