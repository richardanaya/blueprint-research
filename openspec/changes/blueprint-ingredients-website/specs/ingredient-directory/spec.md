## ADDED Requirements

### Requirement: Display comprehensive ingredient listing
The system SHALL display a grid or list view of all 40+ Blueprint supplement ingredients with basic information including name, category, and primary benefits.

#### Scenario: User views ingredient directory
- **WHEN** user navigates to the ingredients page
- **THEN** the system displays all ingredients in a visually organized grid layout
- **AND** each ingredient card shows the name, category tag, and 2-3 key benefits

### Requirement: Categorize ingredients by supplement product
The system SHALL group or tag ingredients by their source Blueprint product (Longevity Mix, Essential Capsules, etc.).

#### Scenario: User filters by product
- **WHEN** user clicks on a product filter (e.g., "Essential Capsules")
- **THEN** the system displays only ingredients from that product
- **AND** the filter state is reflected in the URL

### Requirement: Quick overview on ingredient cards
The system SHALL provide at-a-glance information on ingredient cards including dosage from Blueprint products and a visual impact indicator.

#### Scenario: User scans ingredient cards
- **WHEN** user views the ingredient directory
- **THEN** each card displays the Blueprint dosage amount
- **AND** shows a color-coded impact badge (High/Medium/Low) based on evidence quality

### Requirement: Navigate to ingredient detail pages
The system SHALL make each ingredient card clickable to navigate to the detailed ingredient profile page.

#### Scenario: User clicks ingredient card
- **WHEN** user clicks on an ingredient card
- **THEN** the system navigates to /ingredients/[slug] for that ingredient
- **AND** the page loads with pre-rendered data for fast initial paint
