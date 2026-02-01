'use client';

import Link from 'next/link';
import { Card, CardContent, CardHeader } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Ingredient } from '@/types';

interface IngredientCardProps {
  ingredient: Ingredient;
}

export function IngredientCard({ ingredient }: IngredientCardProps) {
  const getImpactColor = (impact?: string) => {
    switch (impact) {
      case 'High':
        return 'bg-green-100 text-green-800 border-green-200';
      case 'Medium':
        return 'bg-yellow-100 text-yellow-800 border-yellow-200';
      case 'Low':
        return 'bg-gray-100 text-gray-800 border-gray-200';
      default:
        return 'bg-blue-100 text-blue-800 border-blue-200';
    }
  };

  return (
    <Link href={`/ingredients/${ingredient.slug}/`} className="block h-full">
      <Card className="h-full hover:shadow-lg transition-shadow duration-200 cursor-pointer">
        <CardHeader className="pb-2">
          <div className="flex justify-between items-start gap-2">
            <h3 className="text-lg font-semibold leading-tight">
              {ingredient.name}
            </h3>
            <Badge 
              variant="secondary" 
              className={`text-xs whitespace-nowrap ${getImpactColor(ingredient.metaAnalysis?.confidenceLevel)}`}
            >
              {ingredient.category}
            </Badge>
          </div>
        </CardHeader>
        <CardContent className="space-y-3">
          <p className="text-sm text-muted-foreground line-clamp-2">
            {ingredient.description}
          </p>
          
          <div className="flex flex-wrap gap-1">
            {ingredient.keyBenefits.slice(0, 3).map((benefit, index) => (
              <Badge key={index} variant="outline" className="text-xs">
                {benefit}
              </Badge>
            ))}
          </div>
          
          <div className="pt-2 border-t">
            <p className="text-xs text-muted-foreground">
              <span className="font-medium">Blueprint dosage:</span> {ingredient.blueprintDosage}
            </p>
          </div>
        </CardContent>
      </Card>
    </Link>
  );
}
