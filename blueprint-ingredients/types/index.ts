export interface Ingredient {
  id: string;
  slug: string;
  name: string;
  description: string;
  category: Category;
  products: Product[];
  blueprintDosage: string;
  molecularFormula?: string;
  mechanism?: string;
  keyBenefits: string[];
  safetyInfo?: SafetyInfo;
  metaAnalysis?: MetaAnalysis;
}

export type Category = 
  | 'Vitamins'
  | 'Minerals'
  | 'Amino Acids'
  | 'Antioxidants'
  | 'Adaptogens'
  | 'Probiotics'
  | 'Nucleotides'
  | 'Polyphenols'
  | 'Carotenoids'
  | 'Other';

export type Product = 
  | 'Longevity Mix'
  | 'Essential Capsules'
  | 'Advanced Antioxidants'
  | 'NAC + Ginger + Curcumin'
  | 'Omega-3'
  | 'Creatine'
  | 'Collagen'
  | 'Ashwagandha + Rhodiola';

export interface SafetyInfo {
  sideEffects: string[];
  contraindications: string[];
  maxSafeDosage?: string;
  warnings?: string[];
}

export interface MetaAnalysis {
  benefits: Benefit[];
  lastUpdated: string;
  totalStudies: number;
  confidenceLevel: 'High' | 'Medium' | 'Low';
}

export interface Benefit {
  name: string;
  description: string;
  clinicalDosage: string;
  blueprintComparison: 'within' | 'above' | 'below';
  rating: number; // 1-10
  impact: 'High' | 'Medium' | 'Low';
  confidence: 'High' | 'Medium' | 'Low';
  studies: Study[];
}

export interface Study {
  pmid: string;
  title: string;
  authors: string;
  journal: string;
  year: number;
  studyType: 'Meta-Analysis' | 'Systematic Review' | 'RCT' | 'Observational' | 'Other';
  sampleSize?: number;
  conclusion: string;
  quality: 'Cochrane' | 'Large RCT' | 'Other';
}

export interface FilterState {
  search: string;
  categories: Category[];
  products: Product[];
  impact: ('High' | 'Medium' | 'Low')[];
}
