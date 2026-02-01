# Blueprint Ingredients Website

A personal website showcasing all 40+ ingredients from Bryan Johnson's Blueprint supplements with meta-analysis research data from PubMed.

## Features

- **40+ Ingredients**: Complete list of all Blueprint supplement ingredients
- **Ingredient Details**: Each ingredient has its own page with:
  - Description and mechanism of action
  - Molecular formula
  - Blueprint dosage
  - Key benefits
  - Safety information (side effects, contraindications)
  - Research evidence table with meta-analysis data from PubMed
- **Clean Design**: Simple grid layout, no search/filter complexity
- **Responsive**: Works on mobile, tablet, and desktop

## Technology Stack

- Next.js 15 with App Router
- TypeScript
- Tailwind CSS
- shadcn/ui components
- Static export (no server required)

## Getting Started

### Prerequisites

- Node.js 18+
- npm or yarn

### Installation

```bash
cd blueprint-ingredients
npm install
```

### Development

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) to view the site.

### Build

```bash
npm run build
```

This creates a static export in the `dist/` folder.

### Serve Locally

```bash
npx serve dist
```

## Deployment

The site is configured for static export and can be deployed anywhere:

- **Vercel**: Connect GitHub repo and deploy
- **Netlify**: Drag and drop the `dist/` folder
- **GitHub Pages**: Copy `dist/` contents to `gh-pages` branch
- **Any static host**: Upload `dist/` folder contents

## Data

Ingredient data is stored in `data/ingredients.json`. Meta-analysis data is fetched from PubMed's free E-utilities API during build time.

## License

Personal use only.
