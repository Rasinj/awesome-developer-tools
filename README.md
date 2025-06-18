# Awesome Developer Tools 🛠️

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of awesome tools, resources, and utilities that make developers' lives easier and more productive.

## Contents

- [Code Editors & IDEs](#code-editors--ides)
- [Version Control](#version-control)
- [Terminal & Shell](#terminal--shell)
- [Package Managers](#package-managers)
- [Build Tools & Task Runners](#build-tools--task-runners)
- [Testing](#testing)
- [Debugging & Profiling](#debugging--profiling)
- [Code Quality & Linting](#code-quality--linting)
- [API Development & Testing](#api-development--testing)
- [Database Tools](#database-tools)
- [DevOps & Infrastructure](#devops--infrastructure)
- [Monitoring & Logging](#monitoring--logging)
- [Security](#security)
- [Documentation](#documentation)
- [Design & Prototyping](#design--prototyping)
- [Productivity](#productivity)
- [Learning & References](#learning--references)
- [Cloud Platforms](#cloud-platforms)
- [Mobile Development](#mobile-development)
- [Data Science & Machine Learning](#data-science--machine-learning)



## Code Editors & IDEs


Essential text editors and integrated development environments for writing, editing, and managing code across different programming languages.



### Modern Editors
- **[Visual Studio Code](https://code.visualstudio.com/)** - Microsoft's lightweight, extensible code editor with massive ecosystem
- **[Neovim](https://neovim.io/)** - Modern Vim fork with better defaults and Lua configuration
- **[Helix](https://helix-editor.com/)** - Post-modern modal text editor written in Rust
- **[Zed](https://zed.dev/)** - High-performance, multiplayer code editor built in Rust


### Full IDEs
- **[IntelliJ IDEA](https://www.jetbrains.com/idea/)** - Powerful Java IDE with excellent refactoring tools
- **[PyCharm](https://www.jetbrains.com/pycharm/)** - Professional Python IDE with advanced debugging
- **[WebStorm](https://www.jetbrains.com/webstorm/)** - JavaScript and TypeScript IDE
- **[Android Studio](https://developer.android.com/studio)** - Official Android development environment


### Online Editors
- **[GitHub Codespaces](https://github.com/features/codespaces)** - Cloud development environments
- **[Replit](https://replit.com/)** - Browser-based IDE for collaborative coding
- **[CodeSandbox](https://codesandbox.io/)** - Online code editor for web development


## Version Control


Tools for tracking changes in code, collaborating with teams, and managing different versions of software projects.



### Git Tools
- **[Git](https://git-scm.com/)** - Distributed version control system
- **[GitHub CLI](https://cli.github.com/)** - Command-line tool for GitHub
- **[Lazygit](https://github.com/jesseduffield/lazygit)** - Simple terminal UI for git commands
- **[GitKraken](https://www.gitkraken.com/)** - Cross-platform Git GUI client
- **[Sourcetree](https://www.sourcetreeapp.com/)** - Free Git GUI for Mac and Windows


### Git Utilities
- **[pre-commit](https://pre-commit.com/)** - Framework for managing git pre-commit hooks
- **[commitizen](https://commitizen-tools.github.io/commitizen/)** - Tool for creating committing rules
- **[semantic-release](https://semantic-release.gitbook.io/)** - Automated version management and package publishing


## Terminal & Shell


Command-line interfaces, terminal emulators, shells, and utilities that enhance productivity in the terminal environment.



### Terminal Emulators
- **[Alacritty](https://alacritty.org/)** - Fast, cross-platform terminal emulator
- **[WezTerm](https://wezfurlong.org/wezterm/)** - GPU-accelerated terminal emulator and multiplexer
- **[iTerm2](https://iterm2.com/)** - macOS terminal replacement with advanced features
- **[Windows Terminal](https://github.com/microsoft/terminal)** - Modern terminal for Windows


### Shell Enhancement
- **[Fish](https://fishshell.com/)** - Smart and user-friendly command line shell
- **[Zsh](https://www.zsh.org/)** - Extended Bourne shell with improvements
- **[Oh My Zsh](https://ohmyz.sh/)** - Framework for managing Zsh configuration
- **[Starship](https://starship.rs/)** - Fast, customizable prompt for any shell


### Session Management
- **[tmux](https://github.com/tmux/tmux)** - Terminal multiplexer for managing multiple terminal sessions in a single window
- **[zellij](https://zellij.dev/)** - Modern terminal workspace with multiplayer collaboration and floating panes


### File Navigation & Search
- **[fzf](https://github.com/junegunn/fzf)** - Command-line fuzzy finder
- **[fd](https://github.com/sharkdp/fd)** - Simple, fast alternative to find
- **[ripgrep](https://github.com/BurntSushi/ripgrep)** - Fast line-oriented search tool
- **[broot](https://github.com/Canop/broot)** - Interactive tree navigation with fuzzy search and directory sizes
- **[ranger](https://github.com/ranger/ranger)** - Console file manager with vi key bindings and three-column layout
- **[nnn](https://github.com/jarun/nnn)** - Extremely fast and lightweight terminal file manager with plugin support
- **[zoxide](https://github.com/ajeetdsouza/zoxide)** - Smarter cd command that learns your habits and jumps to frequently used directories


### Text Processing & Viewing
- **[bat](https://github.com/sharkdp/bat)** - Cat clone with syntax highlighting and Git integration
- **[exa](https://the.exa.website/)** - Modern replacement for ls with colors and Git status
- **[jq](https://github.com/jqlang/jq)** - Lightweight command-line JSON processor for parsing and transforming data
- **[fx](https://github.com/antonmedv/fx)** - Interactive JSON processor and filter with JavaScript expressions
- **[yq](https://github.com/mikefarah/yq)** - Portable command-line YAML, JSON, XML, CSV, TOML processor
- **[delta](https://github.com/dandavison/delta)** - Syntax-highlighting pager for git diff output with side-by-side views


### System Monitoring
- **[htop](https://htop.dev/)** - Interactive process viewer and system monitor
- **[bottom](https://github.com/ClementTsang/bottom)** - Cross-platform graphical process monitor with customizable widgets
- **[procs](https://github.com/dalance/procs)** - Modern replacement for ps with colored output and search capabilities
- **[bandwhich](https://github.com/imsnif/bandwhich)** - CLI utility for displaying network utilization by process and connection
- **[dust](https://github.com/bootandy/dust)** - Intuitive disk usage analyzer with colored tree output
- **[duf](https://github.com/muesli/duf)** - Better df alternative with colorful disk usage information


### Development Tools
- **[tokei](https://github.com/XAMPPRocky/tokei)** - Fast code statistics tool counting lines across 150+ programming languages
- **[hyperfine](https://github.com/sharkdp/hyperfine)** - Command-line benchmarking tool with statistical analysis and warmup runs
- **[watchexec](https://watchexec.github.io/)** - File watcher that runs commands when files change with flexible filtering
- **[lazydocker](https://github.com/jesseduffield/lazydocker)** - Terminal UI for Docker and Docker Compose with container management


### Productivity & Workflow
- **[direnv](https://direnv.net/)** - Loads and unloads environment variables based on current directory
- **[tldr](https://github.com/tldr-pages/tldr)** - Collaborative cheatsheets providing simplified examples for console commands
- **[lnav](https://lnav.org/)** - Advanced log file navigator with automatic format detection and SQL querying


## Package Managers


Tools for installing, updating, and managing software dependencies and libraries across different programming languages and platforms.



### Language-Specific
- **[npm](https://www.npmjs.com/)** - Node.js package manager
- **[Yarn](https://yarnpkg.com/)** - Fast, reliable JavaScript package manager
- **[pnpm](https://pnpm.io/)** - Efficient package manager for Node.js
- **[pip](https://pip.pypa.io/)** - Python package installer
- **[uv](https://docs.astral.sh/uv/)** - Fast Python package installer and resolver
- **[Cargo](https://doc.rust-lang.org/cargo/)** - Rust package manager
- **[Go Modules](https://golang.org/ref/mod)** - Go dependency management


### System Package Managers
- **[Homebrew](https://brew.sh/)** - Package manager for macOS and Linux
- **[Chocolatey](https://chocolatey.org/)** - Package manager for Windows
- **[Scoop](https://scoop.sh/)** - Command-line installer for Windows


## Build Tools & Task Runners


Automation tools for compiling code, running tasks, managing builds, and streamlining development workflows.



### Build Systems
- **[Webpack](https://webpack.js.org/)** - Module bundler for JavaScript applications
- **[Vite](https://vitejs.dev/)** - Fast build tool for modern web projects
- **[Rollup](https://rollupjs.org/)** - Module bundler for JavaScript libraries
- **[esbuild](https://esbuild.github.io/)** - Extremely fast JavaScript bundler
- **[Turbo](https://turbo.build/)** - High-performance build system for JavaScript/TypeScript


### Task Runners
- **[Make](https://www.gnu.org/software/make/)** - Classic build automation tool
- **[just](https://github.com/casey/just)** - Command runner with syntax similar to make
- **[Task](https://taskfile.dev/)** - Task runner written in Go
- **[npm scripts](https://docs.npmjs.com/cli/v7/using-npm/scripts)** - Built-in task runner for Node.js projects


## Testing


Frameworks and tools for writing, running, and managing different types of tests including unit tests, integration tests, and end-to-end testing.



### Testing Frameworks
- **[Jest](https://jestjs.io/)** - JavaScript testing framework with focus on simplicity
- **[Vitest](https://vitest.dev/)** - Fast unit test framework powered by Vite
- **[Playwright](https://playwright.dev/)** - End-to-end testing for modern web apps
- **[Cypress](https://www.cypress.io/)** - JavaScript end-to-end testing framework
- **[pytest](https://pytest.org/)** - Python testing framework
- **[JUnit](https://junit.org/)** - Unit testing framework for Java


### Testing Utilities
- **[Faker.js](https://fakerjs.dev/)** - Generate massive amounts of fake data
- **[Storybook](https://storybook.js.org/)** - Tool for building UI components in isolation
- **[Testing Library](https://testing-library.com/)** - Simple testing utilities for DOM testing


## Debugging & Profiling


Tools for identifying bugs, analyzing code performance, memory usage, and optimizing application behavior during development.



### Debuggers
- **[Chrome DevTools](https://developer.chrome.com/docs/devtools/)** - Web debugging tools
- **[React Developer Tools](https://react.dev/learn/react-developer-tools)** - Browser extension for debugging React
- **[Vue.js DevTools](https://devtools.vuejs.org/)** - Browser extension for debugging Vue.js
- **[pdb](https://docs.python.org/3/library/pdb.html)** - Built-in Python debugger for interactive debugging and code inspection
- **[gdb](https://www.gnu.org/software/gdb/)** - GNU debugger for C/C++


### Performance Profiling
- **[Lighthouse](https://developers.google.com/web/tools/lighthouse)** - Web performance auditing tool
- **[WebPageTest](https://www.webpagetest.org/)** - Website performance testing
- **[Pyflame](https://github.com/uber-archive/pyflame)** - Profiling tool for Python
- **[perf](https://perf.wiki.kernel.org/)** - Linux profiling tool


## Code Quality & Linting


Static analysis tools, linters, and formatters that enforce coding standards, detect potential issues, and maintain consistent code style.



### Linters & Formatters
- **[ESLint](https://eslint.org/)** - JavaScript and TypeScript linter
- **[Prettier](https://prettier.io/)** - Opinionated code formatter
- **[Black](https://black.readthedocs.io/)** - Python code formatter
- **[Pylint](https://pylint.org/)** - Python static code analysis
- **[Flake8](https://flake8.pycqa.org/)** - Python linting tool
- **[Rustfmt](https://github.com/rust-lang/rustfmt)** - Rust code formatter
- **[Clippy](https://github.com/rust-lang/rust-clippy)** - Rust linter that catches common mistakes and suggests idiomatic code improvements


### Code Analysis
- **[SonarQube](https://www.sonarqube.org/)** - Static code analysis platform
- **[CodeClimate](https://codeclimate.com/)** - Automated code review
- **[Semgrep](https://semgrep.dev/)** - Static analysis tool for finding bugs


## API Development & Testing


Tools for designing, building, testing, and documenting APIs including REST, GraphQL, and other web service interfaces.



### API Testing
- **[Postman](https://www.postman.com/)** - API development and testing platform
- **[Insomnia](https://insomnia.rest/)** - HTTP and GraphQL client
- **[HTTPie](https://httpie.io/)** - Command-line HTTP client
- **[curl](https://curl.se/)** - Command-line tool for transferring data


### API Documentation
- **[Swagger/OpenAPI](https://swagger.io/)** - API documentation framework
- **[Redoc](https://redoc.ly/)** - OpenAPI documentation generator
- **[API Blueprint](https://apiblueprint.org/)** - API documentation format


### Mock Servers
- **[json-server](https://github.com/typicode/json-server)** - Create a full fake REST API with zero coding in less than 30 seconds
- **[WireMock](http://wiremock.org/)** - HTTP service virtualization
- **[Mockoon](https://mockoon.com/)** - Desktop API mocking application


## Database Tools


Database management systems, GUI clients, migration tools, and utilities for working with various types of databases.



### Database Clients
- **[DBeaver](https://dbeaver.io/)** - Universal database tool
- **[TablePlus](https://tableplus.com/)** - Modern, native database client
- **[pgAdmin](https://www.pgadmin.org/)** - PostgreSQL administration tool
- **[MongoDB Compass](https://www.mongodb.com/products/compass)** - GUI for MongoDB


### Database Development
- **[Prisma](https://www.prisma.io/)** - Next-generation ORM for Node.js and TypeScript
- **[Drizzle](https://orm.drizzle.team/)** - TypeScript ORM with SQL-like syntax
- **[Flyway](https://flywaydb.org/)** - Database migration tool
- **[Liquibase](https://www.liquibase.org/)** - Database schema change management


## DevOps & Infrastructure


Deployment, containerization, orchestration, and infrastructure management tools for modern software development and operations.



### Containerization
- **[Docker](https://www.docker.com/)** - Platform for developing and running applications in containers
- **[Podman](https://podman.io/)** - Daemonless container engine
- **[Docker Compose](https://docs.docker.com/compose/)** - Tool for defining multi-container Docker applications


### Orchestration
- **[Kubernetes](https://kubernetes.io/)** - Container orchestration platform
- **[k9s](https://k9scli.io/)** - Terminal UI for Kubernetes
- **[Helm](https://helm.sh/)** - Package manager for Kubernetes
- **[Skaffold](https://skaffold.dev/)** - Workflow tool for Kubernetes applications


### Infrastructure as Code
- **[Terraform](https://www.terraform.io/)** - Infrastructure as code tool
- **[Ansible](https://www.ansible.com/)** - IT automation platform
- **[Pulumi](https://www.pulumi.com/)** - Modern infrastructure as code
- **[AWS CDK](https://aws.amazon.com/cdk/)** - Cloud Development Kit for AWS


### CI/CD
- **[GitHub Actions](https://github.com/features/actions)** - CI/CD platform integrated with GitHub
- **[GitLab CI](https://docs.gitlab.com/ee/ci/)** - Continuous integration service
- **[Jenkins](https://www.jenkins.io/)** - Open-source automation server
- **[Circle CI](https://circleci.com/)** - Continuous integration and delivery platform


## Monitoring & Logging


Application performance monitoring, log aggregation, error tracking, and observability tools for production systems.



### Application Monitoring
- **[Datadog](https://www.datadoghq.com/)** - Monitoring and analytics platform
- **[New Relic](https://newrelic.com/)** - Application performance monitoring
- **[Sentry](https://sentry.io/)** - Error tracking and performance monitoring
- **[Grafana](https://grafana.com/)** - Open-source analytics and monitoring


### Logging
- **[ELK Stack](https://www.elastic.co/elk-stack)** - Elasticsearch, Logstash, and Kibana
- **[Fluentd](https://www.fluentd.org/)** - Open-source data collector
- **[Loki](https://grafana.com/oss/loki/)** - Log aggregation system


## Security


Tools for vulnerability scanning, security testing, secret management, and protecting applications from security threats.



### Security Scanning
- **[Snyk](https://snyk.io/)** - Developer-first security platform
- **[OWASP ZAP](https://owasp.org/www-project-zap/)** - Web application security scanner
- **[Bandit](https://bandit.readthedocs.io/)** - Security linter for Python
- **[npm audit](https://docs.npmjs.com/cli/v7/commands/npm-audit)** - Security vulnerability scanner for npm


### Secret Management
- **[HashiCorp Vault](https://www.vaultproject.io/)** - Secrets management platform
- **[1Password CLI](https://developer.1password.com/docs/cli/)** - Command-line interface for 1Password
- **[AWS Secrets Manager](https://aws.amazon.com/secrets-manager/)** - Secrets management service


## Documentation


Static site generators, documentation platforms, and tools for creating and maintaining technical documentation and knowledge bases.



### Documentation Generators
- **[GitBook](https://www.gitbook.com/)** - Modern documentation platform
- **[MkDocs](https://www.mkdocs.org/)** - Static site generator for documentation
- **[Docusaurus](https://docusaurus.io/)** - Documentation website generator
- **[VitePress](https://vitepress.dev/)** - Static site generator powered by Vite


### API Documentation
- **[Stoplight](https://stoplight.io/)** - API design and documentation platform
- **[Readme.io](https://readme.com/)** - Developer hub for API documentation


## Design & Prototyping


UI/UX design tools, wireframing software, and prototyping platforms for creating user interfaces and design systems.



### Design Tools
- **[Figma](https://www.figma.com/)** - Collaborative design and prototyping tool
- **[Sketch](https://www.sketch.com/)** - Digital design toolkit (macOS)
- **[Adobe XD](https://www.adobe.com/products/xd.html)** - UI/UX design and collaboration tool


### Asset Management
- **[ImageOptim](https://imageoptim.com/)** - Image optimization tool
- **[TinyPNG](https://tinypng.com/)** - Online image compression
- **[SVGO](https://github.com/svg/svgo)** - SVG optimizer


## Productivity


Note-taking apps, task management tools, time tracking software, and utilities that enhance developer productivity and organization.



### Project Management
- **[Linear](https://linear.app/)** - Issue tracking for modern software teams
- **[Notion](https://www.notion.so/)** - All-in-one workspace
- **[Jira](https://www.atlassian.com/software/jira)** - Issue and project tracking


### Time Management
- **[RescueTime](https://www.rescuetime.com/)** - Time tracking and productivity insights
- **[Toggl](https://toggl.com/)** - Time tracking tool
- **[Focus](https://heyfocus.com/)** - Website and application blocker


### Note Taking
- **[Obsidian](https://obsidian.md/)** - Knowledge management with bidirectional links
- **[Roam Research](https://roamresearch.com/)** - Note-taking tool for networked thought
- **[Logseq](https://logseq.com/)** - Open-source knowledge management


## Learning & References


Educational platforms, coding challenges, documentation sites, and reference materials for learning programming and staying updated with technology.



### Documentation
- **[DevDocs](https://devdocs.io/)** - API documentation browser
- **[MDN Web Docs](https://developer.mozilla.org/)** - Web technology documentation
- **[Stack Overflow](https://stackoverflow.com/)** - Q&A platform for developers


### Learning Platforms
- **[freeCodeCamp](https://www.freecodecamp.org/)** - Free coding education
- **[Codecademy](https://www.codecademy.com/)** - Interactive coding lessons
- **[Pluralsight](https://www.pluralsight.com/)** - Technology skills platform
- **[Udemy](https://www.udemy.com/)** - Online learning marketplace


### Practice & Challenges
- **[LeetCode](https://leetcode.com/)** - Coding interview preparation
- **[HackerRank](https://www.hackerrank.com/)** - Programming challenges
- **[Codewars](https://www.codewars.com/)** - Coding challenges and kata
- **[Exercism](https://exercism.io/)** - Code practice and mentorship


## Cloud Platforms


Command-line tools and SDKs for interacting with major cloud service providers and managing cloud infrastructure.



### AWS Tools
- **[AWS CLI](https://aws.amazon.com/cli/)** - Official command-line interface for Amazon Web Services


### Google Cloud
- **[Google Cloud CLI](https://cloud.google.com/sdk/gcloud)** - Command-line interface for Google Cloud Platform services


### Microsoft Azure
- **[Azure CLI](https://docs.microsoft.com/en-us/cli/azure/)** - Cross-platform command-line interface for Microsoft Azure


### Multi-Cloud
- **[Crossplane](https://crossplane.io/)** - Multi-cloud control plane for managing infrastructure across cloud providers


## Mobile Development


Frameworks, tools, and platforms for developing mobile applications across iOS, Android, and cross-platform solutions.



### Cross-Platform
- **[Flutter](https://flutter.dev/)** - Google's UI toolkit for building natively compiled mobile, web, and desktop apps
- **[React Native](https://reactnative.dev/)** - Framework for building mobile apps using React and JavaScript
- **[Expo](https://expo.dev/)** - Platform for universal React applications with tools and services


### Native Development
- **[Xcode](https://developer.apple.com/xcode/)** - Apple's integrated development environment for iOS and macOS applications


## Data Science & Machine Learning


Tools, frameworks, and platforms for data analysis, machine learning, artificial intelligence, and scientific computing.



### Notebooks & Analysis
- **[Jupyter Notebook](https://jupyter.org/)** - Interactive computing environment for creating and sharing documents with code and visualizations
- **[JupyterLab](https://jupyterlab.readthedocs.io/)** - Web-based interactive development environment for Jupyter notebooks and data science


### Machine Learning Libraries
- **[TensorFlow](https://www.tensorflow.org/)** - Open-source machine learning framework for building and deploying ML models
- **[PyTorch](https://pytorch.org/)** - Deep learning framework with dynamic computational graphs and Python-first approach
- **[scikit-learn](https://scikit-learn.org/)** - Machine learning library for Python with simple and efficient tools for data analysis


### Data Processing
- **[pandas](https://pandas.pydata.org/)** - Powerful data manipulation and analysis library for Python
- **[NumPy](https://numpy.org/)** - Fundamental package for scientific computing with Python



## Contributing

Contributions are welcome! Please read the [contribution guidelines](CONTRIBUTING.md) first.

1. Fork the repository
2. Create a new branch for your addition
3. Add your tool with a brief description and link
4. Ensure it fits the category and maintains quality standards
5. Submit a pull request

## Criteria for Inclusion

To maintain quality, tools included in this list should be:

- **Actively maintained** - Regular updates and community support
- **Widely adopted** - Used by a significant portion of the developer community
- **High quality** - Well-designed, reliable, and performant
- **Developer-focused** - Specifically designed to improve developer productivity
- **Accessible** - Available to developers regardless of budget (free or reasonable pricing)

## License

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

This work is licensed under a [Creative Commons Zero v1.0 Universal](LICENSE) license.