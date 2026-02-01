#!/usr/bin/env python3
"""Generate a beautiful website from research.json"""

import json
from html import escape

# Load the research data
with open('research.json', 'r') as f:
    data = json.load(f)

ingredients = data['ingredients']
categories = data['categories']
products = data['products']

# Scientific monochromatic color scheme
category_colors = {
    'Vitamins': {'bg': '#f5f5f5', 'text': '#1a1a1a', 'border': '#d0d0d0'},
    'Minerals': {'bg': '#f0f0f0', 'text': '#1a1a1a', 'border': '#c8c8c8'},
    'Amino Acids': {'bg': '#f8f8f8', 'text': '#1a1a1a', 'border': '#d4d4d4'},
    'Antioxidants': {'bg': '#fafafa', 'text': '#1a1a1a', 'border': '#e0e0e0'},
    'Adaptogens': {'bg': '#f2f2f2', 'text': '#1a1a1a', 'border': '#cccccc'},
    'Probiotics': {'bg': '#f7f7f7', 'text': '#1a1a1a', 'border': '#d8d8d8'},
    'Polyphenols': {'bg': '#f3f3f3', 'text': '#1a1a1a', 'border': '#c5c5c5'},
    'Carotenoids': {'bg': '#f6f6f6', 'text': '#1a1a1a', 'border': '#d6d6d6'},
    'Other': {'bg': '#eeeeee', 'text': '#1a1a1a', 'border': '#bbbbbb'}
}

# Scientific confidence indicators (monochrome)
confidence_colors = {
    'High': '#1a1a1a',
    'Medium': '#666666',
    'Low': '#999999'
}

# Generate ingredient cards HTML
def generate_cards():
    cards_html = []
    for ing in ingredients:
        cat = ing['category']
        colors = category_colors.get(cat, category_colors['Other'])
        
        # Get first benefit description truncated
        first_benefit = ing['keyBenefits'][0] if ing['keyBenefits'] else ''
        
        # Calculate average rating
        ratings = [ev['rating'] for ev in ing['researchEvidence']]
        avg_rating = sum(ratings) / len(ratings) if ratings else 0
        
        # Generate star rating
        stars = '★' * int(round(avg_rating / 2)) + '☆' * (5 - int(round(avg_rating / 2)))
        
        # Products tags
        product_tags = ''.join([
            f'<span class="product-tag">{escape(p)}</span>' 
            for p in ing['products']
        ])
        
        card = f'''
        <div class="ingredient-card" data-category="{escape(cat)}" data-id="{ing['id']}" onclick="openModal({ing['id']})">
            <div class="card-header" style="background: linear-gradient(135deg, {colors['bg']}, white);">
                <span class="category-badge" style="background-color: {colors['bg']}; color: {colors['text']}; border: 1px solid {colors['border']};">
                    {escape(cat)}
                </span>
                <h3 class="card-title">{escape(ing['name'])}</h3>
                <p class="card-dosage">{escape(ing['blueprintDosage'])}</p>
            </div>
            <div class="card-body">
                <p class="card-description">{escape(ing['description'][:120])}...</p>
                <div class="card-rating">
                    <span class="stars">{stars}</span>
                    <span class="rating-value">{avg_rating:.1f}/10</span>
                </div>
                <div class="key-benefits">
                    {''.join([f'<span class="benefit-tag">{escape(b)}</span>' for b in ing['keyBenefits'][:3]])}
                </div>
                <div class="product-tags">
                    {product_tags}
                </div>
            </div>
        </div>
        '''
        cards_html.append(card)
    return '\n'.join(cards_html)

# Generate modal content for each ingredient
def generate_modals():
    modals_html = []
    for ing in ingredients:
        cat = ing['category']
        colors = category_colors.get(cat, category_colors['Other'])
        
        # Research evidence
        evidence_html = []
        for ev in ing['researchEvidence']:
            conf_color = confidence_colors.get(ev['confidence'], '#9ca3af')
            impact_color = '#1a1a1a' if ev['impact'] == 'High' else '#666666' if ev['impact'] == 'Medium' else '#999999'
            
            # Use URLs from the research evidence
            urls = ev.get('urls', [])
            if urls:
                ref_links = ' '.join([
                    f'<a href="{escape(url)}" target="_blank" class="ref-link">[{i+1}]</a>'
                    for i, url in enumerate(urls)
                ])
            else:
                ref_links = '<span class="no-refs">No references available</span>'
            
            evidence_html.append(f'''
            <div class="evidence-item">
                <div class="evidence-header">
                    <h4>{escape(ev['benefit'])}</h4>
                    <div class="evidence-metrics">
                        <span class="rating-badge">{ev['rating']}/10</span>
                        <span class="impact-badge" style="border-color: {impact_color}; color: {impact_color};">{ev['impact']} Impact</span>
                        <span class="confidence-badge" style="border-color: {conf_color}; color: {conf_color};">{ev['confidence']} Confidence</span>
                    </div>
                </div>
                <p class="evidence-description">{escape(ev['description'])}</p>
                <div class="evidence-footer">
                    <span class="dosage-info">Clinical dosage: <strong>{escape(ev['clinicalDosage'])}</strong></span>
                    <div class="refs">References: {ref_links}</div>
                </div>
            </div>
            ''')
        
        # Safety info
        safety = ing['safety']
        side_effects = ', '.join(safety['sideEffects']) if safety['sideEffects'] else 'None reported'
        contraindications = ', '.join(safety['contraindications']) if safety['contraindications'] else 'None'
        
        modal = f'''
        <div id="modal-{ing['id']}" class="modal">
            <div class="modal-content">
                <div class="modal-header" style="background: linear-gradient(135deg, {colors['bg']}, white);">
                    <button class="close-btn" onclick="closeModal({ing['id']})">&times;</button>
                    <span class="category-badge" style="background-color: {colors['bg']}; color: {colors['text']}; border: 1px solid {colors['border']};">
                        {escape(cat)}
                    </span>
                    <h2>{escape(ing['name'])}</h2>
                    <p class="molecular-formula">{escape(ing['molecularFormula'])}</p>
                    <p class="modal-dosage">Blueprint dosage: {escape(ing['blueprintDosage'])}</p>
                </div>
                <div class="modal-body">
                    <section class="info-section">
                        <h3>Description</h3>
                        <p>{escape(ing['description'])}</p>
                    </section>
                    
                    <section class="info-section">
                        <h3>Mechanism</h3>
                        <p>{escape(ing['mechanism'])}</p>
                    </section>
                    
                    <section class="info-section">
                        <h3>Key Benefits</h3>
                        <div class="benefits-list">
                            {''.join([f'<span class="benefit-tag large">{escape(b)}</span>' for b in ing['keyBenefits']])}
                        </div>
                    </section>
                    
                    <section class="info-section">
                        <h3>Products</h3>
                        <div class="products-list">
                            {''.join([f'<span class="product-tag large">{escape(p)}</span>' for p in ing['products']])}
                        </div>
                    </section>
                    
                    <section class="info-section">
                        <h3>Research Evidence</h3>
                        <div class="evidence-list">
                            {''.join(evidence_html)}
                        </div>
                    </section>
                    
                    <section class="info-section safety-section">
                        <h3>Safety Information</h3>
                        <div class="safety-grid">
                            <div class="safety-item">
                                <span class="safety-label">Side Effects</span>
                                <span class="safety-value">{escape(side_effects)}</span>
                            </div>
                            <div class="safety-item">
                                <span class="safety-label">Contraindications</span>
                                <span class="safety-value">{escape(contraindications)}</span>
                            </div>
                            <div class="safety-item">
                                <span class="safety-label">Max Safe Dosage</span>
                                <span class="safety-value highlight">{escape(safety['maxSafeDosage'])}</span>
                            </div>
                        </div>
                    </section>
                </div>
            </div>
        </div>
        '''
        modals_html.append(modal)
    return '\n'.join(modals_html)

# Generate category filter buttons
def generate_category_filters():
    return ''.join([
        f'<button class="filter-btn" data-category="{escape(cat)}" onclick="filterCategory(\'{escape(cat)}\')">{escape(cat)}</button>'
        for cat in categories
    ])

# Generate product filter buttons
def generate_product_filters():
    return ''.join([
        f'<button class="filter-btn product" data-product="{escape(prod)}" onclick="filterProduct(\'{escape(prod)}\')">{escape(prod)}</button>'
        for prod in products
    ])

# Generate the complete HTML
html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Supplement Ingredients Research Database - AI-Assisted Meta-Analysis</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@300;400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        :root {{
            --bg-primary: #ffffff;
            --bg-secondary: #fafafa;
            --bg-tertiary: #f5f5f5;
            --text-primary: #0a0a0a;
            --text-secondary: #404040;
            --text-tertiary: #737373;
            --border-light: #e5e5e5;
            --border-medium: #d4d4d4;
            --border-dark: #a3a3a3;
            --accent: #171717;
        }}
        
        body {{
            font-family: 'IBM Plex Sans', -apple-system, BlinkMacSystemFont, sans-serif;
            background: var(--bg-secondary);
            min-height: 100vh;
            color: var(--text-primary);
            line-height: 1.6;
            font-weight: 400;
        }}
        
        .container {{
            max-width: 1400px;
            margin: 0 auto;
            padding: 60px 40px;
        }}
        
        header {{
            margin-bottom: 60px;
            padding-bottom: 40px;
            border-bottom: 1px solid var(--border-light);
        }}
        
        header h1 {{
            font-size: 2.5rem;
            font-weight: 300;
            letter-spacing: -0.02em;
            margin-bottom: 12px;
            color: var(--text-primary);
        }}
        
        header p {{
            font-size: 1.1rem;
            color: var(--text-secondary);
            max-width: 700px;
            font-weight: 400;
            line-height: 1.5;
        }}
        
        .meta-info {{
            display: flex;
            gap: 24px;
            margin-top: 24px;
            font-family: 'IBM Plex Mono', monospace;
            font-size: 0.8rem;
            color: var(--text-tertiary);
        }}
        
        .meta-badge {{
            padding: 6px 0;
        }}
        
        .disclaimer {{
            background: var(--bg-primary);
            padding: 24px 28px;
            margin-bottom: 40px;
            font-size: 0.9rem;
            color: var(--text-secondary);
            border: 1px solid var(--border-light);
            border-left: 3px solid var(--text-primary);
        }}
        
        .filters {{
            background: var(--bg-primary);
            padding: 32px;
            margin-bottom: 40px;
            border: 1px solid var(--border-light);
        }}
        
        .filter-section {{
            margin-bottom: 28px;
        }}
        
        .filter-section:last-child {{
            margin-bottom: 0;
        }}
        
        .filter-label {{
            font-family: 'IBM Plex Mono', monospace;
            font-weight: 500;
            color: var(--text-tertiary);
            margin-bottom: 12px;
            display: block;
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 0.1em;
        }}
        
        .search-box {{
            width: 100%;
            padding: 14px 18px;
            border: 1px solid var(--border-medium);
            font-size: 0.95rem;
            font-family: 'IBM Plex Sans', sans-serif;
            transition: all 0.2s ease;
            background: var(--bg-primary);
            color: var(--text-primary);
        }}
        
        .search-box:focus {{
            outline: none;
            border-color: var(--text-primary);
            box-shadow: 0 0 0 1px var(--text-primary);
        }}
        
        .search-box::placeholder {{
            color: var(--text-tertiary);
        }}
        
        .filter-buttons {{
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
        }}
        
        .filter-btn {{
            padding: 8px 16px;
            border: 1px solid var(--border-medium);
            background: var(--bg-primary);
            cursor: pointer;
            font-size: 0.85rem;
            font-family: 'IBM Plex Sans', sans-serif;
            font-weight: 500;
            transition: all 0.15s ease;
            color: var(--text-secondary);
        }}
        
        .filter-btn:hover {{
            border-color: var(--text-primary);
            color: var(--text-primary);
        }}
        
        .filter-btn.active {{
            background: var(--text-primary);
            color: var(--bg-primary);
            border-color: var(--text-primary);
        }}
        
        .filter-btn.product {{
            font-size: 0.8rem;
        }}
        
        .cards-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
            gap: 20px;
        }}
        
        .ingredient-card {{
            background: var(--bg-primary);
            border: 1px solid var(--border-light);
            overflow: hidden;
            cursor: pointer;
            transition: all 0.2s ease;
        }}
        
        .ingredient-card:hover {{
            border-color: var(--border-dark);
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
        }}
        
        .ingredient-card.hidden {{
            display: none;
        }}
        
        .card-header {{
            padding: 24px 24px 16px;
            border-bottom: 1px solid var(--border-light);
        }}
        
        .category-badge {{
            display: inline-block;
            padding: 4px 10px;
            font-size: 0.7rem;
            font-weight: 500;
            font-family: 'IBM Plex Mono', monospace;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 12px;
            border: 1px solid;
        }}
        
        .card-title {{
            font-size: 1.25rem;
            color: var(--text-primary);
            margin-bottom: 4px;
            font-weight: 600;
            letter-spacing: -0.01em;
        }}
        
        .card-dosage {{
            font-size: 0.85rem;
            color: var(--text-tertiary);
            font-weight: 400;
            font-family: 'IBM Plex Mono', monospace;
        }}
        
        .card-body {{
            padding: 20px 24px 24px;
        }}
        
        .card-description {{
            color: var(--text-secondary);
            font-size: 0.9rem;
            margin-bottom: 16px;
            line-height: 1.5;
        }}
        
        .card-rating {{
            display: flex;
            align-items: center;
            gap: 8px;
            margin-bottom: 16px;
        }}
        
        .stars {{
            color: var(--text-primary);
            font-size: 0.95rem;
            letter-spacing: 2px;
        }}
        
        .rating-value {{
            color: var(--text-tertiary);
            font-size: 0.85rem;
            font-weight: 500;
            font-family: 'IBM Plex Mono', monospace;
        }}
        
        .key-benefits, .product-tags {{
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
            margin-top: 12px;
        }}
        
        .benefit-tag {{
            background: var(--bg-tertiary);
            color: var(--text-secondary);
            padding: 4px 10px;
            font-size: 0.75rem;
            font-weight: 500;
            border: 1px solid var(--border-light);
        }}
        
        .benefit-tag.large {{
            padding: 6px 12px;
            font-size: 0.85rem;
        }}
        
        .product-tag {{
            background: var(--bg-secondary);
            color: var(--text-secondary);
            padding: 4px 10px;
            font-size: 0.75rem;
            font-weight: 500;
            border: 1px solid var(--border-light);
        }}
        
        .product-tag.large {{
            padding: 6px 12px;
            font-size: 0.85rem;
        }}
        
        /* Modal Styles */
        .modal {{
            display: none;
            position: fixed;
            z-index: 1000;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.5);
            animation: fadeIn 0.2s ease;
        }}
        
        .modal.active {{
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 40px;
        }}
        
        @keyframes fadeIn {{
            from {{ opacity: 0; }}
            to {{ opacity: 1; }}
        }}
        
        .modal-content {{
            background: var(--bg-primary);
            max-width: 800px;
            width: 100%;
            max-height: 90vh;
            overflow-y: auto;
            animation: slideUp 0.2s ease;
            box-shadow: 0 25px 80px rgba(0, 0, 0, 0.3);
            border: 1px solid var(--border-medium);
        }}
        
        @keyframes slideUp {{
            from {{ 
                opacity: 0;
                transform: translateY(20px);
            }}
            to {{ 
                opacity: 1;
                transform: translateY(0);
            }}
        }}
        
        .modal-header {{
            padding: 32px;
            position: relative;
            border-bottom: 1px solid var(--border-light);
        }}
        
        .close-btn {{
            position: absolute;
            top: 20px;
            right: 20px;
            background: none;
            border: none;
            font-size: 1.25rem;
            cursor: pointer;
            width: 32px;
            height: 32px;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.15s ease;
            color: var(--text-tertiary);
        }}
        
        .close-btn:hover {{
            color: var(--text-primary);
        }}
        
        .modal-header h2 {{
            font-size: 1.6rem;
            color: var(--text-primary);
            margin: 12px 0 4px 0;
            font-weight: 600;
            letter-spacing: -0.01em;
        }}
        
        .molecular-formula {{
            font-family: 'IBM Plex Mono', monospace;
            color: var(--text-tertiary);
            font-size: 0.85rem;
        }}
        
        .modal-dosage {{
            margin-top: 8px;
            color: var(--text-secondary);
            font-weight: 400;
            font-family: 'IBM Plex Mono', monospace;
            font-size: 0.9rem;
        }}
        
        .modal-body {{
            padding: 32px;
        }}
        
        .info-section {{
            margin-bottom: 32px;
        }}
        
        .info-section:last-child {{
            margin-bottom: 0;
        }}
        
        .info-section h3 {{
            font-family: 'IBM Plex Mono', monospace;
            font-size: 0.8rem;
            color: var(--text-tertiary);
            margin-bottom: 16px;
            padding-bottom: 8px;
            border-bottom: 1px solid var(--border-light);
            text-transform: uppercase;
            letter-spacing: 0.05em;
            font-weight: 500;
        }}
        
        .info-section p {{
            color: var(--text-secondary);
            line-height: 1.6;
        }}
        
        .benefits-list, .products-list {{
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
        }}
        
        .evidence-list {{
            display: flex;
            flex-direction: column;
            gap: 16px;
        }}
        
        .evidence-item {{
            background: var(--bg-secondary);
            padding: 20px;
            border: 1px solid var(--border-light);
            border-left: 2px solid var(--text-primary);
        }}
        
        .evidence-header {{
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            flex-wrap: wrap;
            gap: 12px;
            margin-bottom: 12px;
        }}
        
        .evidence-header h4 {{
            font-size: 1rem;
            color: var(--text-primary);
            flex: 1;
            font-weight: 600;
        }}
        
        .evidence-metrics {{
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
        }}
        
        .rating-badge, .impact-badge, .confidence-badge {{
            padding: 4px 10px;
            font-size: 0.75rem;
            font-weight: 500;
            font-family: 'IBM Plex Mono', monospace;
            border: 1px solid var(--border-medium);
            background: var(--bg-primary);
        }}
        
        .rating-badge {{
            color: var(--text-primary);
        }}
        
        .evidence-description {{
            color: var(--text-secondary);
            margin-bottom: 12px;
            line-height: 1.5;
            font-size: 0.9rem;
        }}
        
        .evidence-footer {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 10px;
            font-size: 0.8rem;
            color: var(--text-tertiary);
            padding-top: 12px;
            border-top: 1px solid var(--border-light);
            font-family: 'IBM Plex Mono', monospace;
        }}
        
        .dosage-info strong {{
            color: var(--text-primary);
        }}
        
        .ref-link {{
            color: var(--text-primary);
            text-decoration: underline;
        }}
        
        .ref-link:hover {{
            opacity: 0.7;
        }}
        
        .safety-section {{
            background: var(--bg-secondary);
            padding: 20px;
            border: 1px solid var(--border-light);
        }}
        
        .safety-section h3 {{
            color: var(--text-primary);
            border-bottom-color: var(--border-medium);
        }}
        
        .safety-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 15px;
        }}
        
        .safety-item {{
            display: flex;
            flex-direction: column;
            gap: 4px;
        }}
        
        .safety-label {{
            font-size: 0.75rem;
            color: var(--text-tertiary);
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            font-family: 'IBM Plex Mono', monospace;
        }}
        
        .safety-value {{
            color: var(--text-secondary);
            font-size: 0.95rem;
        }}
        
        .safety-value.highlight {{
            color: var(--text-primary);
            font-weight: 600;
        }}
        
        @media (max-width: 768px) {{
            .container {{
                padding: 30px 20px;
            }}
            
            header h1 {{
                font-size: 1.8rem;
            }}
            
            header p {{
                font-size: 1rem;
            }}
            
            .meta-info {{
                gap: 16px;
            }}
            
            .cards-grid {{
                grid-template-columns: 1fr;
            }}
            
            .modal-content {{
                max-height: 95vh;
                border-radius: 0;
            }}
            
            .modal-header, .modal-body {{
                padding: 24px;
            }}
            
            .modal.active {{
                padding: 0;
            }}
            
            .evidence-header {{
                flex-direction: column;
            }}
            
            .filter-btn {{
                font-size: 0.8rem;
                padding: 6px 12px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Blueprint Ingredients</h1>
            <p>{escape(data['description'])}</p>
            <div class="meta-info">
                <span class="meta-badge">{data['totalIngredients']} Ingredients</span>
                <span class="meta-badge">Data: {data['lastUpdated']}</span>
                <span class="meta-badge">v{data['version']}</span>
            </div>
        </header>
        
        <div class="disclaimer">
            <strong>Disclaimer:</strong> {escape(data['disclaimer'])}
        </div>
        
        <div class="filters">
            <div class="filter-section">
                <label class="filter-label">Search</label>
                <input type="text" class="search-box" id="searchBox" placeholder="Search by name, category, or benefit..." oninput="searchIngredients()">
            </div>
            
            <div class="filter-section">
                <label class="filter-label">Category</label>
                <div class="filter-buttons">
                    <button class="filter-btn active" data-category="all" onclick="filterCategory('all')">All</button>
                    {generate_category_filters()}
                </div>
            </div>
            
            <div class="filter-section">
                <label class="filter-label">Product</label>
                <div class="filter-buttons">
                    <button class="filter-btn active" data-product="all" onclick="filterProduct('all')">All Products</button>
                    {generate_product_filters()}
                </div>
            </div>
        </div>
        
        <div class="cards-grid" id="cardsGrid">
            {generate_cards()}
        </div>
        
        {generate_modals()}
    </div>
    
    <script>
        let currentCategory = 'all';
        let currentProduct = 'all';
        let currentSearch = '';
        
        function filterCategory(category) {{
            currentCategory = category;
            
            // Update button states
            document.querySelectorAll('[data-category]').forEach(btn => {{
                btn.classList.remove('active');
                if (btn.dataset.category === category) {{
                    btn.classList.add('active');
                }}
            }});
            
            applyFilters();
        }}
        
        function filterProduct(product) {{
            currentProduct = product;
            
            // Update button states
            document.querySelectorAll('[data-product]').forEach(btn => {{
                btn.classList.remove('active');
                if (btn.dataset.product === product) {{
                    btn.classList.add('active');
                }}
            }});
            
            applyFilters();
        }}
        
        function searchIngredients() {{
            currentSearch = document.getElementById('searchBox').value.toLowerCase();
            applyFilters();
        }}
        
        function applyFilters() {{
            const cards = document.querySelectorAll('.ingredient-card');
            
            cards.forEach(card => {{
                const category = card.dataset.category;
                const id = card.dataset.id;
                const ingredient = getIngredientById(id);
                
                let matchesCategory = currentCategory === 'all' || category === currentCategory;
                let matchesProduct = currentProduct === 'all' || ingredient.products.includes(currentProduct);
                let matchesSearch = true;
                
                if (currentSearch) {{
                    const searchText = (
                        ingredient.name + ' ' +
                        ingredient.category + ' ' +
                        ingredient.keyBenefits.join(' ') + ' ' +
                        ingredient.description
                    ).toLowerCase();
                    matchesSearch = searchText.includes(currentSearch);
                }}
                
                if (matchesCategory && matchesProduct && matchesSearch) {{
                    card.classList.remove('hidden');
                }} else {{
                    card.classList.add('hidden');
                }}
            }});
        }}
        
        function getIngredientById(id) {{
            const ingredientsData = {json.dumps(ingredients)};
            return ingredientsData.find(i => i.id === id);
        }}
        
        function openModal(id) {{
            const modal = document.getElementById('modal-' + id);
            modal.classList.add('active');
            document.body.style.overflow = 'hidden';
        }}
        
        function closeModal(id) {{
            const modal = document.getElementById('modal-' + id);
            modal.classList.remove('active');
            document.body.style.overflow = '';
        }}
        
        // Close modal when clicking outside
        document.addEventListener('click', function(e) {{
            if (e.target.classList.contains('modal')) {{
                e.target.classList.remove('active');
                document.body.style.overflow = '';
            }}
        }});
        
        // Close modal with Escape key
        document.addEventListener('keydown', function(e) {{
            if (e.key === 'Escape') {{
                document.querySelectorAll('.modal.active').forEach(modal => {{
                    modal.classList.remove('active');
                }});
                document.body.style.overflow = '';
            }}
        }});
    </script>
</body>
</html>
'''

# Write the HTML file
with open('ingredients.html', 'w') as f:
    f.write(html_content)

print("Generated ingredients.html with 40 ingredients")
print("Open ingredients.html in your browser to view the website")
