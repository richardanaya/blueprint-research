## ADDED Requirements

### Requirement: Full-text search ingredients
The system SHALL provide a full-text search that matches ingredient names, descriptions, benefits, and categories.

#### Scenario: Search by name
- **WHEN** user types "creatine" in the search box
- **THEN** the system displays ingredients matching that name
- **AND** updates results in real-time as user types (debounced 300ms)

#### Scenario: Search by benefit
- **WHEN** user types "sleep" in the search box
- **THEN** the system displays ingredients with sleep-related benefits
- **AND** highlights the matching text in results

### Requirement: Category filtering
The system SHALL allow filtering ingredients by category (e.g., "Vitamins", "Minerals", "Amino Acids", "Adaptogens").

#### Scenario: Filter by category
- **WHEN** user selects "Amino Acids" from category filter
- **THEN** the system displays only ingredients in that category
- **AND** updates the URL with filter parameter

### Requirement: Product filtering
The system SHALL allow filtering by Blueprint product (Longevity Mix, Essential Capsules, etc.).

#### Scenario: Filter by product
- **WHEN** user selects "Essential Capsules" from product filter
- **THEN** the system displays only ingredients found in that product
- **AND** shows a count of matching ingredients

### Requirement: Impact level filtering
The system SHALL allow filtering ingredients by evidence impact level (High, Medium, Low).

#### Scenario: Filter by impact
- **WHEN** user selects "High Impact" filter
- **THEN** the system displays only ingredients with High evidence impact
- **AND** sorts them by rating

### Requirement: URL-based filter state
The system SHALL encode all filter and search states in the URL for shareability and browser history support.

#### Scenario: Share filtered view
- **WHEN** user applies filters and copies the URL
- **THEN** another user opening that URL sees the same filtered results
- **AND** browser back/forward buttons work correctly with filter history

### Requirement: Clear filters
The system SHALL provide a clear/reset button to remove all applied filters and search terms.

#### Scenario: Clear filters
- **WHEN** user clicks "Clear All" button
- **THEN** all filters are removed
- **AND** the ingredient list returns to default (all ingredients)
- **AND** the URL resets to base ingredients path
