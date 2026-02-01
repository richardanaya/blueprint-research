import { Ingredient } from '@/types';
import ingredientsData from '@/data/ingredients.json';

export function getAllIngredients(): Ingredient[] {
  return ingredientsData.ingredients as Ingredient[];
}

export function getIngredientBySlug(slug: string): Ingredient | undefined {
  return ingredientsData.ingredients.find(ingredient => ingredient.slug === slug) as Ingredient | undefined;
}

export function getAllSlugs(): string[] {
  return ingredientsData.ingredients.map(ingredient => ingredient.slug);
}

export function getIngredientsByCategory(category: string): Ingredient[] {
  return ingredientsData.ingredients.filter(ingredient => ingredient.category === category) as Ingredient[];
}

export function getIngredientsByProduct(product: string): Ingredient[] {
  return ingredientsData.ingredients.filter(ingredient => 
    ingredient.products.includes(product as any)
  ) as Ingredient[];
}

export function getAllCategories(): string[] {
  const categories = new Set(ingredientsData.ingredients.map(i => i.category));
  return Array.from(categories).sort();
}

export function getAllProducts(): string[] {
  return ingredientsData.metadata.products;
}

export function searchIngredients(query: string): Ingredient[] {
  const lowerQuery = query.toLowerCase();
  return ingredientsData.ingredients.filter(ingredient => 
    ingredient.name.toLowerCase().includes(lowerQuery) ||
    ingredient.description.toLowerCase().includes(lowerQuery) ||
    ingredient.keyBenefits.some(benefit => benefit.toLowerCase().includes(lowerQuery))
  ) as Ingredient[];
}

export function filterIngredients(
  search: string,
  categories: string[],
  products: string[],
  impact: string[]
): Ingredient[] {
  let results = getAllIngredients();

  if (search) {
    results = searchIngredients(search);
  }

  if (categories.length > 0) {
    results = results.filter(i => categories.includes(i.category));
  }

  if (products.length > 0) {
    results = results.filter(i => 
      i.products.some(p => products.includes(p))
    );
  }

  return results;
}
