import { Benefit } from '@/types';
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from '@/components/ui/table';
import { Badge } from '@/components/ui/badge';
import { Tooltip, TooltipContent, TooltipProvider, TooltipTrigger } from '@/components/ui/tooltip';

interface BenefitsTableProps {
  benefits: Benefit[];
}

export function BenefitsTable({ benefits }: BenefitsTableProps) {
  const getRatingColor = (rating: number) => {
    if (rating >= 8) return 'bg-green-100 text-green-800';
    if (rating >= 5) return 'bg-yellow-100 text-yellow-800';
    return 'bg-gray-100 text-gray-800';
  };

  const getImpactColor = (impact: string) => {
    switch (impact) {
      case 'High':
        return 'bg-green-500 text-white';
      case 'Medium':
        return 'bg-yellow-500 text-black';
      case 'Low':
        return 'bg-gray-400 text-white';
      default:
        return 'bg-gray-200 text-gray-800';
    }
  };

  const getConfidenceColor = (confidence: string) => {
    switch (confidence) {
      case 'High':
        return 'text-green-600';
      case 'Medium':
        return 'text-yellow-600';
      case 'Low':
        return 'text-gray-500';
      default:
        return 'text-gray-500';
    }
  };

  return (
    <TooltipProvider>
      <div className="space-y-6">
        {benefits.map((benefit, index) => (
          <div key={index} className="border rounded-lg p-4 space-y-3">
            {/* Header row with benefit name and key metrics */}
            <div className="flex flex-wrap items-center gap-3 pb-3 border-b">
              <h4 className="text-lg font-semibold flex-1 min-w-[200px]">{benefit.name}</h4>
              
              <div className="flex items-center gap-2">
                <Tooltip>
                  <TooltipTrigger>
                    <Badge className={`${getRatingColor(benefit.rating)} font-bold`}>
                      {benefit.rating}/10
                    </Badge>
                  </TooltipTrigger>
                  <TooltipContent>
                    <p className="text-xs max-w-xs">
                      Evidence rating based on {benefit.studies.length} studies
                    </p>
                  </TooltipContent>
                </Tooltip>
                
                <Badge className={getImpactColor(benefit.impact)}>
                  {benefit.impact} Impact
                </Badge>
                
                <span className={`text-sm ${getConfidenceColor(benefit.confidence)}`}>
                  {benefit.confidence} Confidence
                </span>
              </div>
            </div>
            
            {/* Detailed description */}
            <div className="text-sm text-muted-foreground leading-relaxed">
              {benefit.description}
            </div>
            
            {/* Dosage info */}
            <div className="flex flex-wrap gap-4 text-sm">
              <div>
                <span className="font-medium">Clinical Dosage:</span>{' '}
                <span className="text-muted-foreground">{benefit.clinicalDosage}</span>
              </div>
              <div>
                <span className="font-medium">Blueprint Match:</span>{' '}
                <span className={
                  benefit.blueprintComparison === 'within' ? 'text-green-600' :
                  benefit.blueprintComparison === 'above' ? 'text-yellow-600' :
                  'text-blue-600'
                }>
                  {benefit.blueprintComparison === 'within' ? '✓ Within range' :
                   benefit.blueprintComparison === 'above' ? '↑ Above typical' :
                   '↓ Below typical'}
                </span>
              </div>
            </div>
            
            {/* Source studies */}
            <div className="pt-2">
              <p className="text-xs font-medium text-muted-foreground mb-2">Research Sources:</p>
              <div className="flex flex-wrap gap-2">
                {benefit.studies.map((study) => (
                  <a
                    key={study.pmid}
                    href={`https://pubmed.ncbi.nlm.nih.gov/${study.pmid}/`}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-xs bg-slate-100 hover:bg-slate-200 px-2 py-1 rounded transition-colors"
                    title={`${study.title} (${study.year})`}
                  >
                    PMID: {study.pmid}
                  </a>
                ))}
              </div>
            </div>
          </div>
        ))}
      </div>
    </TooltipProvider>
  );
}
