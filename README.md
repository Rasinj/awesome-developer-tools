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
- [Development Environments](#development-environments)
- [DevOps & Infrastructure](#devops--infrastructure)
- [Monitoring & Logging](#monitoring--logging)
- [Security](#security)
- [Documentation](#documentation)
- [Design & Prototyping](#design--prototyping)
- [Productivity](#productivity)
- [Python Libraries & Tools](#python-libraries--tools)
- [Learning & References](#learning--references)
- [Cloud Platforms](#cloud-platforms)
- [Mobile Development](#mobile-development)
- [Web Frameworks](#web-frameworks)
- [Desktop Application Development](#desktop-application-development)
- [Data Science & Machine Learning](#data-science--machine-learning)
- [Data Engineering](#data-engineering)



## Code Editors & IDEs


Essential text editors and integrated development environments for writing, editing, and managing code across different programming languages.



### Modern Editors
- **[Visual Studio Code](https://code.visualstudio.com/)** - Microsoft's lightweight, extensible code editor with massive ecosystem
- **[Helix](https://helix-editor.com/)** - Post-modern modal text editor written in Rust
- **[Zed](https://zed.dev/)** - High-performance, multiplayer code editor built in Rust
- **[Cursor](https://www.cursor.com/)** - AI-first code editor built for pair programming
- **[Sublime Text](https://www.sublimetext.com/)** - Fast, lightweight text editor for code and prose
- **[VSCodium](https://vscodium.com/)** - Telemetry-free build of VS Code
- **[Kate](https://kate-editor.org/)** - Advanced text editor from the KDE project
- **[Notepad++](https://notepad-plus-plus.org/)** - Free source code editor for Windows


### Full IDEs
- **[IntelliJ IDEA](https://www.jetbrains.com/idea/)** - Powerful Java IDE with excellent refactoring tools
- **[PyCharm](https://www.jetbrains.com/pycharm/)** - Professional Python IDE with advanced debugging
- **[WebStorm](https://www.jetbrains.com/webstorm/)** - JavaScript and TypeScript IDE
- **[JetBrains Fleet](https://www.jetbrains.com/fleet/)** - Lightweight IDE by JetBrains with a modern UI
- **[Android Studio](https://developer.android.com/studio)** - Official Android development environment


### Online Editors
- **[GitHub Codespaces](https://github.com/features/codespaces)** - Cloud development environments
- **[Replit](https://replit.com/)** - Browser-based IDE for collaborative coding
- **[CodeSandbox](https://codesandbox.io/)** - Online code editor for web development


### Vim & Modal Editors
- **[Neovim](https://neovim.io/)** - Modern Vim fork with better defaults, Lua scripting, and built-in LSP
- **[Vim](https://www.vim.org/)** - Highly configurable text editor built to make creating and changing text efficient
- **[SpaceVim](https://spacevim.org/)** - Community-driven Vim distribution with modular configuration
- **[LazyVim](https://lazyvim.org/)** - Neovim configuration for the lazy with sane defaults and easy customization
- **[AstroNvim](https://astronvim.com/)** - Aesthetic and feature-rich neovim config that is extensible and easy to use
- **[LunarVim](https://lunarvim.org/)** - IDE layer for Neovim with sane defaults and plugin management
- **[NvChad](https://nvchad.com/)** - Blazing fast Neovim config providing solid defaults and beautiful UI


### Emacs
- **[GNU Emacs](https://www.gnu.org/software/emacs/)** - Extensible, customizable text editor and computing environment
- **[Doom Emacs](https://doomemacs.org/)** - Emacs framework with Vim emulation and curated package selection
- **[Spacemacs](https://www.spacemacs.org/)** - Community-driven Emacs distribution with excellent defaults


## Version Control


Tools for tracking changes in code, collaborating with teams, and managing different versions of software projects.



### Git Tools
- **[Git](https://git-scm.com/)** - Distributed version control system
- **[GitHub CLI](https://cli.github.com/)** - Command-line tool for GitHub
- **[GitHub Desktop](https://desktop.github.com/)** - Simple Git GUI client for GitHub workflows
- **[Lazygit](https://github.com/jesseduffield/lazygit)** - Simple terminal UI for git commands
- **[Fork](https://git-fork.com/)** - Fast and friendly Git client for macOS and Windows
- **[GitKraken](https://www.gitkraken.com/)** - Cross-platform Git GUI client
- **[Sourcetree](https://www.sourcetreeapp.com/)** - Free Git GUI for Mac and Windows


### Git Utilities
- **[pre-commit](https://pre-commit.com/)** - Framework for managing git pre-commit hooks
- **[Git LFS](https://git-lfs.com/)** - Git extension for versioning large files
- **[commitizen](https://commitizen-tools.github.io/commitizen/)** - Tool for creating committing rules
- **[semantic-release](https://semantic-release.gitbook.io/)** - Automated version management and package publishing


## Terminal & Shell


Command-line interfaces, terminal emulators, shells, and utilities that enhance productivity in the terminal environment.



### Terminal Emulators
- **[Alacritty](https://alacritty.org/)** - Fast, cross-platform terminal emulator
- **[kitty](https://sw.kovidgoyal.net/kitty/)** - Fast, feature-rich GPU-based terminal emulator
- **[WezTerm](https://wezfurlong.org/wezterm/)** - GPU-accelerated terminal emulator and multiplexer
- **[Ghostty](https://ghostty.org/)** - Fast, native terminal emulator focused on performance
- **[Warp](https://www.warp.dev/)** - Modern terminal with a collaborative, AI-assisted workflow
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
- **[visidata](https://visidata.org/)** - Terminal spreadsheet multitool for exploring and arranging data


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
- **[Poetry](https://python-poetry.org/)** - Python dependency management and packaging
- **[PDM](https://pdm.fming.dev/)** - Modern Python package manager with PEP 582 support
- **[Pipenv](https://pipenv.pypa.io/)** - Python development workflow for humans
- **[Cargo](https://doc.rust-lang.org/cargo/)** - Rust package manager
- **[Go Modules](https://golang.org/ref/mod)** - Go dependency management


### System Package Managers
- **[Homebrew](https://brew.sh/)** - Package manager for macOS and Linux
- **[Chocolatey](https://chocolatey.org/)** - Package manager for Windows
- **[Scoop](https://scoop.sh/)** - Command-line installer for Windows


### Version Managers
- **[nvm](https://github.com/nvm-sh/nvm)** - Node.js version manager with easy switching between versions
- **[fnm](https://github.com/Schniz/fnm)** - Fast and simple Node.js version manager built in Rust
- **[rbenv](https://github.com/rbenv/rbenv)** - Ruby version management with project-specific versions
- **[pyenv](https://github.com/pyenv/pyenv)** - Simple Python version management with project-specific versions
- **[SDKMAN!](https://sdkman.io/)** - Tool for managing parallel versions of multiple SDKs (Java, Scala, etc.)
- **[rustup](https://rustup.rs/)** - Official Rust toolchain installer and version manager


## Build Tools & Task Runners


Automation tools for compiling code, running tasks, managing builds, and streamlining development workflows.



### General Build Systems
- **[CMake](https://cmake.org/)** - Cross-platform build system generator
- **[Ninja](https://ninja-build.org/)** - Small build system focused on speed
- **[Meson](https://mesonbuild.com/)** - Fast, user-friendly build system
- **[Bazel](https://bazel.build/)** - Build and test tool for large codebases


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
- **[Ruff](https://docs.astral.sh/ruff/)** - Extremely fast Python linter and formatter
- **[Pylint](https://pylint.org/)** - Python static code analysis
- **[Flake8](https://flake8.pycqa.org/)** - Python linting tool
- **[isort](https://pycqa.github.io/isort/)** - Python import sorting utility
- **[mypy](https://mypy-lang.org/)** - Static type checker for Python
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
- **[Bruno](https://www.usebruno.com/)** - Fast, git-friendly API client
- **[Hoppscotch](https://hoppscotch.io/)** - Open-source API development ecosystem
- **[HTTPie](https://httpie.io/)** - Command-line HTTP client
- **[curl](https://curl.se/)** - Command-line tool for transferring data


### API Documentation
- **[Swagger/OpenAPI](https://swagger.io/)** - API documentation framework
- **[Redoc](https://redoc.ly/)** - OpenAPI documentation generator
- **[OpenAPI Generator](https://openapi-generator.tech/)** - Generate API clients, servers, and docs from OpenAPI specs
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


### Graph & Analytics Databases
- **[Neo4j](https://neo4j.com/)** - Graph database platform for connected data and complex queries
- **[KuzuDB](https://kuzudb.com/)** - Embeddable graph database built for query speed and scalability
- **[ClickHouse](https://clickhouse.com/)** - Real-time analytics DBMS for big data and high performance
- **[Apache Parquet Tools](https://github.com/apache/parquet-mr)** - Command-line tools for reading, writing and manipulating Parquet files


## Development Environments


Tools for creating, managing, and maintaining consistent development environments across different platforms and projects.



### Containerized Environments
- **[Dev Containers](https://containers.dev/)** - Open specification for development containers with VS Code integration
- **[Gitpod](https://gitpod.io/)** - Cloud development environments that start in seconds
- **[Devpod](https://devpod.sh/)** - Client-only tool for creating reproducible developer environments
- **[Coder](https://coder.com/)** - Self-hosted remote development environments on your infrastructure


### Virtual Machines
- **[Vagrant](https://www.vagrantup.com/)** - Tool for building and managing virtual machine environments
- **[Lima](https://github.com/lima-vm/lima)** - Linux virtual machines for macOS with automatic file sharing
- **[Multipass](https://multipass.run/)** - Ubuntu VMs on demand for any workstation
- **[UTM](https://mac.getutm.app/)** - Virtual machines for iOS and macOS using QEMU


### Reproducible Systems
- **[Nix](https://nixos.org/)** - Functional package manager for reproducible and declarative systems
- **[asdf](https://asdf-vm.com/)** - Version manager for multiple runtime versions with plugin ecosystem
- **[mise](https://mise.jdx.dev/)** - Fast polyglot tool version manager and task runner
- **[Guix](https://guix.gnu.org/)** - Functional package manager and distribution for reproducible builds


### Local Development Orchestration
- **[Tilt](https://tilt.dev/)** - Toolkit for microservice development with live updates
- **[DevSpace](https://devspace.sh/)** - Client-only developer tool for deploying & developing Kubernetes apps
- **[Garden](https://garden.io/)** - Automation platform for Kubernetes development and testing workflows
- **[Telepresence](https://telepresence.io/)** - Local development against remote Kubernetes clusters


### Remote Development
- **[VS Code Remote](https://code.visualstudio.com/docs/remote/remote-overview)** - VS Code extensions for remote development via SSH, containers, and WSL
- **[code-server](https://github.com/coder/code-server)** - VS Code in the browser running on a remote server
- **[JetBrains Gateway](https://www.jetbrains.com/remote-development/gateway/)** - Remote development solution for JetBrains IDEs
- **[Theia](https://theia-ide.org/)** - Cloud and desktop IDE platform built with modern web technologies


### Project Scaffolding
- **[Cookiecutter](https://cookiecutter.readthedocs.io/)** - Command-line utility for creating projects from templates
- **[Yeoman](https://yeoman.io/)** - Web application scaffolding tool with generator ecosystem
- **[degit](https://github.com/Rich-Harris/degit)** - Straightforward project scaffolding without git history
- **[Plop](https://plopjs.com/)** - Micro-generator framework for teams to create consistent code


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
- **[SigNoz](https://signoz.io/)** - Open-source observability platform for metrics, logs, and traces


### Tracing & Observability
- **[OpenTelemetry](https://opentelemetry.io/)** - Open-source observability framework for traces, metrics, and logs
- **[Jaeger](https://www.jaegertracing.io/)** - Distributed tracing system
- **[Grafana Tempo](https://grafana.com/oss/tempo/)** - High-scale distributed tracing backend


### Logging
- **[ELK Stack](https://www.elastic.co/elk-stack)** - Elasticsearch, Logstash, and Kibana
- **[Fluentd](https://www.fluentd.org/)** - Open-source data collector
- **[Loki](https://grafana.com/oss/loki/)** - Log aggregation system


## Security


Tools for vulnerability scanning, security testing, secret management, and protecting applications from security threats.



### Security Scanning
- **[Snyk](https://snyk.io/)** - Developer-first security platform
- **[OWASP ZAP](https://owasp.org/www-project-zap/)** - Web application security scanner
- **[Burp Suite](https://portswigger.net/burp)** - Web security testing toolkit
- **[Bandit](https://bandit.readthedocs.io/)** - Security linter for Python
- **[Trivy](https://trivy.dev/)** - Vulnerability scanner for containers and dependencies
- **[Gitleaks](https://gitleaks.io/)** - Detect and prevent secrets in Git repos
- **[Checkov](https://www.checkov.io/)** - Infrastructure as code security scanner
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


## Python Libraries & Tools


Python-specific libraries, frameworks, and utilities for environment management and application development.



### Environment Management
- **[conda](https://docs.conda.io/)** - Package and environment management system for Python and other languages
- **[virtualenv](https://virtualenv.pypa.io/)** - Virtual Python environment builder for dependency isolation
- **[pipx](https://pypa.github.io/pipx/)** - Install and run Python applications in isolated environments


### CLI Development
- **[Click](https://click.palletsprojects.com/)** - Composable command line interface toolkit for Python
- **[Typer](https://typer.tiangolo.com/)** - Modern library for building CLI applications with type hints
- **[Rich](https://rich.readthedocs.io/)** - Library for rich text and beautiful formatting in the terminal
- **[Textual](https://textual.textualize.io/)** - Framework for building interactive terminal user interfaces


### HTTP Clients
- **[requests](https://requests.readthedocs.io/)** - Simple and elegant HTTP library for synchronous requests
- **[httpx](https://www.python-httpx.org/)** - Modern HTTP client with async/sync support and HTTP/2
- **[aiohttp](https://docs.aiohttp.org/)** - Async HTTP client/server framework for high-concurrency applications


### Data Validation
- **[Pydantic](https://docs.pydantic.dev/)** - Data validation using Python type hints with high performance
- **[Marshmallow](https://marshmallow.readthedocs.io/)** - Object serialization and deserialization library with schema-based validation
- **[Cerberus](https://docs.python-cerberus.org/)** - Lightweight and extensible data validation library


### Testing Extensions
- **[pytest-cov](https://pytest-cov.readthedocs.io/)** - Coverage plugin for pytest to measure test coverage
- **[coverage.py](https://coverage.readthedocs.io/)** - Code coverage measurement tool for Python
- **[Hypothesis](https://hypothesis.readthedocs.io/)** - Property-based testing library for writing powerful tests
- **[tox](https://tox.wiki/)** - Automation tool for testing in multiple Python environments


### Web & Data Apps
- **[Streamlit](https://streamlit.io/)** - Framework for building interactive data apps and dashboards rapidly
- **[Gradio](https://www.gradio.app/)** - Build and share machine learning demos and web apps quickly
- **[Reflex](https://reflex.dev/)** - Full-stack Python framework for building web apps without JavaScript


### Async Libraries
- **[asyncio](https://docs.python.org/3/library/asyncio.html)** - Built-in library for writing concurrent code using async/await syntax
- **[Trio](https://trio.readthedocs.io/)** - Friendly Python library for async concurrency with structured concurrency
- **[AnyIO](https://anyio.readthedocs.io/)** - Compatibility layer for asyncio and Trio with unified high-level API


### ORMs & Database Libraries
- **[SQLAlchemy](https://www.sqlalchemy.org/)** - Powerful and flexible SQL toolkit and ORM for Python
- **[Tortoise ORM](https://tortoise.github.io/)** - Async ORM inspired by Django with excellent performance
- **[Peewee](http://docs.peewee-orm.com/)** - Lightweight and expressive ORM for small to medium applications


### Task Queues & Scheduling
- **[Celery](https://docs.celeryq.dev/)** - Distributed task queue for handling asynchronous jobs at scale
- **[RQ](https://python-rq.org/)** - Simple Python library for queueing jobs backed by Redis
- **[Dramatiq](https://dramatiq.io/)** - Fast and reliable alternative to Celery for distributed tasks
- **[APScheduler](https://apscheduler.readthedocs.io/)** - Advanced Python scheduler for running jobs at specific times or intervals


### Logging
- **[loguru](https://loguru.readthedocs.io/)** - Simplified logging library with beautiful colors and easy configuration
- **[structlog](https://www.structlog.org/)** - Structured logging library for producing JSON or Logfmt output


### Configuration Management
- **[Dynaconf](https://www.dynaconf.com/)** - Layered configuration system supporting multiple formats and environments
- **[pydantic-settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)** - Type-safe settings management with Pydantic integration
- **[python-decouple](https://github.com/HBNetwork/python-decouple)** - Strict separation of settings from code for 12-factor apps


### Documentation Generators
- **[Sphinx](https://www.sphinx-doc.org/)** - Popular documentation generator supporting multiple output formats
- **[pdoc](https://pdoc.dev/)** - Lightweight automatic API documentation generator with zero configuration
- **[mkdocstrings](https://mkdocstrings.github.io/)** - Automatic documentation from docstrings for MkDocs


### Serialization
- **[orjson](https://github.com/ijl/orjson)** - Fast, correct JSON library for Python written in Rust
- **[msgpack](https://msgpack.org/)** - Efficient binary serialization format faster and smaller than JSON
- **[msgspec](https://jcristharif.com/msgspec/)** - Fast serialization library supporting JSON, MessagePack, YAML, and TOML


### Profiling & Performance
- **[py-spy](https://github.com/benfred/py-spy)** - Sampling profiler for Python programs with minimal overhead
- **[Scalene](https://github.com/plasma-umass/scalene)** - High-performance CPU, GPU, and memory profiler with AI optimization suggestions
- **[Memray](https://bloomberg.github.io/memray/)** - Memory profiler for Python tracking allocations in native extensions


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


## Web Frameworks


Backend and full-stack frameworks for building web applications, REST APIs, and web services across different programming languages.



### Python
- **[FastAPI](https://fastapi.tiangolo.com/)** - Modern, fast web framework for building APIs with automatic documentation
- **[Django](https://www.djangoproject.com/)** - High-level Python web framework with batteries-included approach
- **[Flask](https://flask.palletsprojects.com/)** - Lightweight WSGI web application framework for simple to complex applications
- **[Starlette](https://www.starlette.io/)** - Lightweight ASGI framework for building high-performance async web services


### JavaScript/TypeScript
- **[Next.js](https://nextjs.org/)** - React framework with server-side rendering and static site generation
- **[Express](https://expressjs.com/)** - Fast, unopinionated, minimalist web framework for Node.js
- **[NestJS](https://nestjs.com/)** - Progressive Node.js framework for building efficient and scalable server-side applications
- **[Nuxt](https://nuxt.com/)** - Vue.js framework for building universal and static web applications
- **[SvelteKit](https://kit.svelte.dev/)** - Full-stack framework for building web apps with Svelte
- **[Remix](https://remix.run/)** - Full-stack web framework built on Web Fetch API
- **[Hono](https://hono.dev/)** - Ultrafast web framework for the Edge runtime


### Other Languages
- **[Ruby on Rails](https://rubyonrails.org/)** - Server-side web application framework written in Ruby
- **[Laravel](https://laravel.com/)** - PHP web application framework with elegant syntax
- **[Spring Boot](https://spring.io/projects/spring-boot)** - Java-based framework for building production-ready applications
- **[ASP.NET Core](https://dotnet.microsoft.com/apps/aspnet)** - Cross-platform framework for building modern web applications with .NET
- **[Gin](https://gin-gonic.com/)** - High-performance HTTP web framework written in Go
- **[Fiber](https://gofiber.io/)** - Express-inspired web framework built on Fasthttp for Go
- **[Actix Web](https://actix.rs/)** - Powerful, pragmatic, and fast web framework for Rust
- **[Axum](https://github.com/tokio-rs/axum)** - Ergonomic and modular web framework built with Tokio for Rust


## Desktop Application Development


Frameworks and tools for building cross-platform and native desktop applications.



### Cross-Platform
- **[Electron](https://www.electronjs.org/)** - Build cross-platform desktop apps with JavaScript, HTML, and CSS
- **[Tauri](https://tauri.app/)** - Lightweight framework for building desktop apps with web technologies and Rust
- **[Flutter Desktop](https://flutter.dev/desktop)** - Build beautiful native desktop applications with Flutter
- **[Qt](https://www.qt.io/)** - Cross-platform framework for C++ desktop application development
- **[Avalonia](https://avaloniaui.net/)** - Cross-platform XAML-based UI framework for .NET
- **[Wails](https://wails.io/)** - Build desktop apps using Go and web technologies


### Native
- **[SwiftUI](https://developer.apple.com/xcode/swiftui/)** - Declarative framework for building macOS applications
- **[WPF](https://docs.microsoft.com/en-us/dotnet/desktop/wpf/)** - Windows Presentation Foundation for building Windows desktop applications
- **[WinUI](https://microsoft.github.io/microsoft-ui-xaml/)** - Modern native UI platform for Windows applications


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
- **[DuckDB](https://duckdb.org/)** - In-process SQL OLAP database for analytics with zero dependencies
- **[Polars](https://pola.rs/)** - Fast DataFrame library implemented in Rust with Python bindings
- **[Apache Arrow](https://arrow.apache.org/)** - Cross-language development platform for in-memory columnar data
- **[Parquet](https://parquet.apache.org/)** - Columnar storage format optimized for analytics workloads


### Time Series
- **[Tsfresh](https://tsfresh.com/)** - A Python package for automatic extraction of a large number of time-series features.
- **[Sktime](https://www.sktime.net/)** - A unified framework for time series analysis in Python, interoperable with scikit-learn.
- **[AutoTS](https://github.com/winedarksea/AutoTS)** - An automated time-series forecasting library for Python.
- **[Prophet](https://facebook.github.io/prophet/)** - A forecasting library for time series data developed by Facebook.


## Data Engineering


Tools and frameworks for building, orchestrating, and managing data pipelines, ETL/ELT processes, and data infrastructure at scale.



### Workflow Orchestration
- **[Apache Airflow](https://airflow.apache.org/)** - Platform to programmatically author, schedule, and monitor workflows as DAGs
- **[Prefect](https://www.prefect.io/)** - Modern workflow orchestration tool with dynamic, Pythonic pipeline definitions
- **[Dagster](https://dagster.io/)** - Data orchestration platform with built-in testing, data quality, and observability
- **[Temporal](https://temporal.io/)** - Durable execution framework for building resilient workflows and distributed systems
- **[Mage](https://www.mage.ai/)** - Modern data pipeline tool with notebook-style development and built-in observability
- **[Argo Workflows](https://argoproj.github.io/workflows/)** - Kubernetes-native workflow engine for orchestrating parallel jobs


### Data Transformation
- **[dbt](https://www.getdbt.com/)** - Data build tool for transforming data in your warehouse using SQL and version control
- **[Apache Spark](https://spark.apache.org/)** - Unified analytics engine for large-scale data processing with batch and streaming
- **[SQLMesh](https://sqlmesh.com/)** - DataOps framework for SQL transformations with built-in testing and CI/CD
- **[dlt](https://dlthub.com/)** - Python library for building data pipelines with automatic schema inference
- **[Malloy](https://github.com/malloydata/malloy)** - Experimental language for describing data relationships and transformations


### Data Integration
- **[Airbyte](https://airbyte.com/)** - Open-source data integration platform with 300+ pre-built connectors
- **[Meltano](https://meltano.com/)** - Open-source ELT platform built on top of Singer with CLI-first approach
- **[Singer](https://www.singer.io/)** - Open-source standard for writing scripts that move data between systems
- **[Fivetran](https://www.fivetran.com/)** - Fully managed ELT service with automated connectors and schema management
- **[Estuary Flow](https://estuary.dev/)** - Real-time data integration platform built on change data capture


### Stream Processing
- **[Apache Kafka](https://kafka.apache.org/)** - Distributed event streaming platform for high-performance data pipelines and streaming apps
- **[Apache Flink](https://flink.apache.org/)** - Stateful stream processing framework for distributed, high-performing applications
- **[Redpanda](https://redpanda.com/)** - Kafka-compatible streaming platform built in C++ for faster performance
- **[Apache Pulsar](https://pulsar.apache.org/)** - Cloud-native distributed messaging and streaming platform with multi-tenancy
- **[Kafka Streams](https://kafka.apache.org/documentation/streams/)** - Client library for building stream processing applications with Apache Kafka
- **[Benthos](https://www.benthos.dev/)** - Stream processor for mundane tasks with a declarative configuration approach


### Data Quality & Validation
- **[Great Expectations](https://greatexpectations.io/)** - Python-based data validation framework with declarative expectations and profiling
- **[Soda](https://www.soda.io/)** - Data quality platform with SQL-based checks and automated monitoring
- **[deequ](https://github.com/awslabs/deequ)** - Data quality library built on Apache Spark for defining unit tests on data
- **[Pandera](https://pandera.readthedocs.io/)** - Statistical data validation library for pandas DataFrames with type hints
- **[ydata-profiling](https://github.com/ydataai/ydata-profiling)** - Python library for generating comprehensive data profiling reports from DataFrames
- **[whylogs](https://whylogs.readthedocs.io/)** - Data logging library for monitoring data quality in production pipelines


### Data Lake Technologies
- **[Apache Iceberg](https://iceberg.apache.org/)** - High-performance table format for huge analytic datasets with ACID transactions
- **[Delta Lake](https://delta.io/)** - Open-source storage framework with ACID transactions for data lakes
- **[Apache Hudi](https://hudi.apache.org/)** - Streaming data lake platform with incremental processing and upsert capabilities
- **[lakeFS](https://lakefs.io/)** - Git-like version control for data lakes with branching and rollback support
- **[Project Nessie](https://projectnessie.org/)** - Git-like version control for data lakes compatible with Iceberg, Delta, and Hudi


### Query Engines
- **[Trino](https://trino.io/)** - Distributed SQL query engine for querying data across multiple sources
- **[Presto](https://prestodb.io/)** - Distributed SQL query engine for running interactive queries against diverse data sources
- **[Apache Drill](https://drill.apache.org/)** - Schema-free SQL query engine for Hadoop, NoSQL, and cloud storage
- **[Dremio](https://www.dremio.com/)** - Data lakehouse platform with SQL query acceleration and self-service analytics


### Data Cataloging & Metadata
- **[DataHub](https://datahubproject.io/)** - Extensible metadata platform for data discovery and governance with lineage tracking
- **[Amundsen](https://www.amundsen.io/)** - Data discovery and metadata platform for improving data productivity
- **[OpenMetadata](https://open-metadata.org/)** - Open standard for metadata with data discovery, lineage, and quality capabilities
- **[Apache Atlas](https://atlas.apache.org/)** - Scalable metadata and governance platform for Hadoop and cloud environments


### Data Version Control
- **[DVC](https://dvc.org/)** - Git-based data version control for machine learning projects with experiment tracking
- **[Pachyderm](https://www.pachyderm.com/)** - Data versioning and pipeline platform with reproducible data science workflows



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