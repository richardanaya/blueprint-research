## ADDED Requirements

### Requirement: Calculate benefit ratings
The system SHALL calculate a rating (1-10) for each benefit based on the quality and quantity of meta-analysis evidence.

#### Scenario: Rate a benefit
- **WHEN** the system processes meta-analysis data for a benefit
- **THEN** it calculates a rating based on: number of supporting studies, study quality, sample sizes, and consistency of results
- **AND** displays the rating as a number with visual indicator (color/stars)

### Requirement: Define rating methodology
The system SHALL use a transparent methodology for ratings: 1-3 (Limited evidence), 4-6 (Moderate evidence), 7-8 (Strong evidence), 9-10 (Very strong evidence with large sample sizes).

#### Scenario: Display rating methodology
- **WHEN** user hovers over or clicks a rating
- **THEN** the system shows a tooltip explaining the rating scale
- **AND** indicates how many studies support that rating

### Requirement: Categorize impact levels
The system SHALL categorize each benefit's impact as High, Medium, or Low based on effect sizes reported in meta-analyses.

#### Scenario: Display impact level
- **WHEN** the system calculates impact for a benefit
- **THEN** it assigns High (large effect size), Medium (moderate effect), or Low (small but significant effect)
- **AND** displays the impact with a colored badge

### Requirement: Show confidence indicators
The system SHALL display confidence indicators for ratings based on heterogeneity (I²) and publication bias risk from meta-analyses.

#### Scenario: Display confidence
- **WHEN** the system shows a benefit rating
- **THEN** it displays a confidence level: High (low heterogeneity), Medium, or Low (high heterogeneity or bias risk)
- **AND** explains the confidence metric on hover

### Requirement: Weight ratings by study quality
The system SHALL weight ratings more heavily from high-quality meta-analyses (Cochrane reviews, large RCTs) than from lower-quality studies.

#### Scenario: Calculate weighted rating
- **WHEN** multiple meta-analyses exist for a benefit
- **THEN** the system applies quality weights (Cochrane: 1.5x, Large RCT: 1.2x, Other: 1.0x)
- **AND** produces a weighted average rating
