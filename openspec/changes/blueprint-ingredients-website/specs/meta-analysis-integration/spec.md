## ADDED Requirements

### Requirement: Integrate with PubMed API
The system SHALL integrate with NCBI E-utilities API to search for meta-analyses related to each ingredient.

#### Scenario: System searches PubMed
- **WHEN** the system needs meta-analysis data for an ingredient
- **THEN** it calls the PubMed ESearch API with appropriate search terms
- **AND** retrieves a list of relevant meta-analysis PMIDs

### Requirement: Fetch meta-analysis abstracts
The system SHALL fetch abstracts and metadata for meta-analyses to extract key information including study type, conclusion, and sample size.

#### Scenario: System fetches study details
- **WHEN** the system has a list of PMIDs
- **THEN** it calls the PubMed ESummary API to retrieve study metadata
- **AND** parses the response to extract title, abstract, and publication details

### Requirement: Cache API responses
The system SHALL cache PubMed API responses for 24 hours to prevent hitting rate limits and improve performance.

#### Scenario: Repeated requests
- **WHEN** the system requests data for an ingredient within 24 hours
- **THEN** it returns cached data instead of making a new API call
- **AND** the cache automatically expires after 24 hours

### Requirement: Handle API failures gracefully
The system SHALL handle PubMed API failures gracefully, falling back to static snapshot data when the API is unavailable.

#### Scenario: API is down
- **WHEN** the PubMed API returns an error or times out
- **THEN** the system logs the error
- **AND** displays pre-loaded static data for the ingredient
- **AND** shows a notification that live data is temporarily unavailable

### Requirement: Parse clinical dosages from abstracts
The system SHALL attempt to extract clinically studied dosages from meta-analysis abstracts using pattern matching or NLP.

#### Scenario: Extract dosage information
- **WHEN** the system parses an abstract
- **THEN** it identifies dosage mentions (e.g., "doses of 500-1000 mg")
- **AND** stores the extracted dosage range with the study
