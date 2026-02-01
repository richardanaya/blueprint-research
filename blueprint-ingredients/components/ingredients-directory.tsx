'use client';

import { useState, useCallback, useEffect } from 'react';
import { IngredientCard } from '@/components/ingredient-card';
import { SearchBar } from '@/components/search-bar';
import { CategoryFilter, ProductFilter } from '@/components/filters';
import { getAllIngredients, filterIngredients } from '@/lib/data';
import { Ingredient } from '@/types';
import { Button } from '@/components/ui/button';

export function IngredientsDirectory() {
  const [ingredients, setIngredients] = useState<Ingredient[]>(getAllIngredients());
  const [search, setSearch] = useState('');
  const [category, setCategory] = useState('');
  const [product, setProduct] = useState('');

  const handleSearch = useCallback((query: string) => {
    setSearch(query);
  }, []);

  const handleClear = () => {
    setSearch('');
    setCategory('');
    setProduct('');
  };

  useEffect(() => {
    const filtered = filterIngredients(
      search,
      category ? [category] : [],
      product ? [product] : [],
      []
    );
    setIngredients(filtered);
  }, [search, category, product]);

  return (
    <div className="space-y-6">
      <div className="flex flex-col sm:flex-row gap-4">
        <div className="flex-1">
          <SearchBar onSearch={handleSearch} initialValue={search} />
        </div>
        <div className="flex gap-2">
          <CategoryFilter value={category} onChange={setCategory} />
          <ProductFilter value={product} onChange={setProduct} />
          {(search || category || product) && (
            <Button variant="outline" onClick={handleClear}>
              Clear
            </Button>
          )}
        </div>
      </div>

      <p className="text-sm text-muted-foreground">
        Showing {ingredients.length} of {getAllIngredients().length} ingredients
      </p>

      {ingredients.length === 0 ? (
        <div className="text-center py-12">
          <p className="text-muted-foreground">No ingredients found matching your criteria.</p>
        </div>
      ) : (
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
          {ingredients.map((ingredient) => (
            <IngredientCard key={ingredient.id} ingredient={ingredient} />
          ))}
        </div>
      )}
    </div>
  );
}
