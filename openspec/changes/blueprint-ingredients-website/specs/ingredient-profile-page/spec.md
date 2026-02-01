## ADDED Requirements

### Requirement: Display detailed ingredient information
The system SHALL display comprehensive information about each ingredient on its dedicated page including: full description, chemical structure/form, Blueprint dosage, category classification, and molecular mechanism.

#### Scenario: User views ingredient profile
- **WHEN** user navigates to an ingredient detail page
- **THEN** the system displays the ingredient name, description, and all metadata
- **AND** shows the dosage as provided in Blueprint supplements

### Requirement: Show meta-analysis research results
The system SHALL display a table of meta-analysis results for the ingredient, including top benefits with clinical dosages, ratings, impact levels, and PubMed citations.

#### Scenario: User views research data
- **WHEN** user scrolls to the research section
- **THEN** the system displays a table with benefit rows
- **AND** each row contains: benefit name, clinical dosage, rating (1-10), impact level, and source link

### Requirement: Provide dosage comparison
The system SHALL visually compare Blueprint dosage against clinically studied dosages to show alignment or gaps.

#### Scenario: User compares dosages
- **WHEN** user views the dosage section
- **THEN** the system displays Blueprint dosage alongside typical clinical study ranges
- **AND** indicates with color if Blueprint dosage is within, above, or below typical ranges

### Requirement: Link to source studies
The system SHALL provide direct links to PubMed abstracts for all meta-analyses cited in the benefits table.

#### Scenario: User clicks source link
- **WHEN** user clicks a "View Study" link in the benefits table
- **THEN** the system opens the PubMed abstract in a new tab
- **AND** the link uses the PubMed ID (PMID) for reliability

### Requirement: Display safety information
The system SHALL display safety information including common side effects, contraindications, and maximum safe dosages from research.

#### Scenario: User checks safety
- **WHEN** user scrolls to the safety section
- **THEN** the system displays known side effects and safety warnings
- **AND** cites the sources for safety data
