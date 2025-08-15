### 🃏Solution design for card game ##

#### Initial To-Do List with Reasoning:

1. **Development Environment Setup**
   - Install Node.js/npm
   - Initialize Git repository
   - Create `.gitignore` file
   - *Why*: Ensures consistent environment for all developers and enables dependency management

2. **Solution Scaffolding**
   - Create project structure:
     ```
     /src
        /core
        /adapters
        /application
        /html
     /tests
        /unit
        /integration
    jest.config.js
    package.json
    README.md
     ```
   - *Why*: Clean architecture separation with test directories
3. **Continuous Delivery Pipeline**
   - GitHub Actions workflow with:
     - Linting stage
     - Unit test stage
     - Build verification
     - Containerization
   - *Why*: Ensures quality before integration

4. **Core Domain Implementation**
   - Card entity
   - Deck aggregate
   - Shuffle domain service
   - *Why*: Foundation for all card games

5. **Test Infrastructure**
   - Configure Jest
   - Setup test coverage
   - Implement first unit test
   - *Why*: Enforces TDD approach

#### How to Run

```bash
# Install dependencies
npm install

# Run tests with coverage
npm test

# Start CLI interface
node src/html/cli.js

# Build Docker image
docker build -t Excercise3 .

#### Architecture Decision Record (ADR)

**Decision Implementation of clean Architecture**

*Why Chosen (Values & Philosophy)*
- **Future-proofing**: The constraint "unsure of UI or game rules" demanded an architecture where core logic remains untouched by delivery mechanisms
- **Cognitive Bias Mitigation**: Avoided *pro-innovation bias* (no over-engineering for hypothetical UIs) and *ambiguity effect* (clear boundaries reduced uncertainty)
- **Team Collaboration**: Explicit contracts between layers enable parallel development by multiple engineers

### Alternatives Considered
1. **Monolithic Class Approach**
   - *Why rejected*: Would couple game rules with UI, violating the "unsure of UI" constraint
   - *Risk*: High refactoring cost when adding web UI later

2. **Traditional Layered Architecture**
   - *Why rejected*: Database-centric layers don't fit card game domain
   - *Risk*: Business logic leakage into infrastructure

3. **Event Sourcing**
   - *Why rejected*: Overkill for initial card operations
   - *Compromise*: Repository interface allows event sourcing later


*Surprises:*
- This exercise reinforces how capable modern, vanilla JavaScript has become. 
- with ES6 modules, classes, and modern tooling (like Jest), we can apply robust software architecture principles directly, creating clean, maintainable, and framework-agnostic code from day one.
- Initial setup complexity balanced by long-term flexibility
- Domain purity required stricter test boundaries

---


