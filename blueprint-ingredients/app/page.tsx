import { getAllIngredients } from '@/lib/data';
import { IngredientCard } from '@/components/ingredient-card';
import { Alert, AlertTitle, AlertDescription } from '@/components/ui/alert';
import { AlertTriangle } from 'lucide-react';

export default function HomePage() {
  const ingredients = getAllIngredients();

  return (
    <div className="min-h-screen">
      {/* Warning Banner */}
      <div className="bg-yellow-50 border-b border-yellow-200">
        <div className="container mx-auto px-4 py-4">
          <Alert variant="default" className="border-yellow-400 bg-yellow-100">
            <AlertTriangle className="h-5 w-5 text-yellow-700" />
            <AlertTitle className="text-yellow-800 font-semibold">Not Medical Advice</AlertTitle>
            <AlertDescription className="text-yellow-700">
              This website provides links to PubMed meta-analyses and AI-generated summaries for informational purposes only. 
              It is not medical advice, nor a substitute for professional healthcare. Always consult a qualified healthcare 
              provider before making any health decisions or starting supplement regimens.
            </AlertDescription>
          </Alert>
        </div>
      </div>

      {/* Main Content */}
      <div className="container mx-auto px-4 py-8 max-w-full xl:px-8">
        <div className="mb-8">
          <h1 className="text-3xl font-bold mb-2">Blueprint Ingredients</h1>
          <p className="text-muted-foreground">
            {ingredients.length} research-backed ingredients from Blueprint supplements with meta-analysis data from PubMed
          </p>
        </div>
        
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 2xl:grid-cols-5 gap-4">
          {ingredients.map((ingredient) => (
            <IngredientCard key={ingredient.id} ingredient={ingredient} />
          ))}
        </div>
      </div>
    </div>
  );
}
