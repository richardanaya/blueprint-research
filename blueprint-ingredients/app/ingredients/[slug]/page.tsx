import { notFound } from 'next/navigation';
import { getIngredientBySlug, getAllSlugs } from '@/lib/data';
import { Badge } from '@/components/ui/badge';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { getStaticMetaAnalysis } from '@/lib/pubmed';
import { BenefitsTable } from '@/components/benefits-table';

interface IngredientPageProps {
  params: Promise<{
    slug: string;
  }>;
}

export async function generateStaticParams() {
  const slugs = getAllSlugs();
  return slugs.map((slug) => ({ slug }));
}

export default async function IngredientPage({ params }: IngredientPageProps) {
  const { slug } = await params;
  const ingredient = getIngredientBySlug(slug);

  if (!ingredient) {
    notFound();
  }

  // Use static meta-analysis data (no API calls during build)
  const metaAnalysis = getStaticMetaAnalysis(ingredient.name);

  return (
    <div className="container mx-auto px-4 py-8 max-w-5xl">
      <div className="mb-6">
        <div className="flex items-center gap-2 text-sm text-muted-foreground mb-2">
          <a href="/ingredients/" className="hover:underline">Ingredients</a>
          <span>/</span>
          <span>{ingredient.name}</span>
        </div>
        <h1 className="text-3xl font-bold">{ingredient.name}</h1>
        <div className="flex flex-wrap gap-2 mt-2">
          <Badge variant="secondary">{ingredient.category}</Badge>
          {ingredient.products.map((product) => (
            <Badge key={product} variant="outline">{product}</Badge>
          ))}
        </div>
      </div>

      <div className="grid gap-6">
        <Card>
          <CardHeader>
            <CardTitle>Description</CardTitle>
          </CardHeader>
          <CardContent className="space-y-4">
            <p>{ingredient.description}</p>
            {ingredient.molecularFormula && (
              <p className="text-sm text-muted-foreground">
                <strong>Molecular Formula:</strong> {ingredient.molecularFormula}
              </p>
            )}
            {ingredient.mechanism && (
              <div>
                <h4 className="font-semibold mb-1">Mechanism of Action</h4>
                <p className="text-sm">{ingredient.mechanism}</p>
              </div>
            )}
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Blueprint Dosage</CardTitle>
          </CardHeader>
          <CardContent>
            <p className="text-lg font-medium text-primary">{ingredient.blueprintDosage}</p>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Key Benefits</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="flex flex-wrap gap-2">
              {ingredient.keyBenefits.map((benefit, index) => (
                <Badge key={index} variant="secondary">{benefit}</Badge>
              ))}
            </div>
          </CardContent>
        </Card>

        {metaAnalysis && metaAnalysis.benefits.length > 0 ? (
          <Card>
            <CardHeader>
              <CardTitle>Research Evidence ({metaAnalysis.totalStudies} studies)</CardTitle>
            </CardHeader>
            <CardContent>
              <BenefitsTable benefits={metaAnalysis.benefits} />
            </CardContent>
          </Card>
        ) : (
          <Card>
            <CardHeader>
              <CardTitle>Research Evidence</CardTitle>
            </CardHeader>
            <CardContent>
              <p className="text-muted-foreground">Loading research data...</p>
            </CardContent>
          </Card>
        )}

        {ingredient.safetyInfo && (
          <Card>
            <CardHeader>
              <CardTitle>Safety Information</CardTitle>
            </CardHeader>
            <CardContent className="space-y-4">
              {ingredient.safetyInfo.sideEffects.length > 0 && (
                <div>
                  <h4 className="font-semibold mb-2">Potential Side Effects</h4>
                  <ul className="list-disc list-inside text-sm space-y-1">
                    {ingredient.safetyInfo.sideEffects.map((effect, index) => (
                      <li key={index}>{effect}</li>
                    ))}
                  </ul>
                </div>
              )}
              
              {ingredient.safetyInfo.contraindications.length > 0 && (
                <div>
                  <h4 className="font-semibold mb-2">Contraindications</h4>
                  <ul className="list-disc list-inside text-sm space-y-1">
                    {ingredient.safetyInfo.contraindications.map((contra, index) => (
                      <li key={index}>{contra}</li>
                    ))}
                  </ul>
                </div>
              )}
              
              {ingredient.safetyInfo.maxSafeDosage && (
                <p className="text-sm">
                  <strong>Maximum Safe Dosage:</strong> {ingredient.safetyInfo.maxSafeDosage}
                </p>
              )}
            </CardContent>
          </Card>
        )}
      </div>
    </div>
  );
}
