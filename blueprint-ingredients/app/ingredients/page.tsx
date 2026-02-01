import type { Metadata } from 'next';
import { getAllIngredients } from '@/lib/data';
import { IngredientCard } from '@/components/ingredient-card';

export default function IngredientsPage() {
  const ingredients = getAllIngredients();

  return (
    <div className="container mx-auto px-4 py-8 max-w-7xl">
      <div className="mb-8">
        <h1 className="text-3xl font-bold mb-2">Blueprint Ingredients</h1>
        <p className="text-muted-foreground">
          {ingredients.length} research-backed ingredients from Blueprint supplements
        </p>
      </div>
      
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
        {ingredients.map((ingredient) => (
          <IngredientCard key={ingredient.id} ingredient={ingredient} />
        ))}
      </div>
    </div>
  );
}
