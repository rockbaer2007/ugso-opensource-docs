# Architecture

ATLAS is developed as a modular TypeScript monorepo.

## Packages

| Package | Responsibility |
|---|---|
| `core` | Central contracts and foundational types |
| `foundation` | Shared infrastructure and general building blocks |
| `runtime` | Runtime environment, services and service container |
| `renderer` | Presentation layer and renderer abstractions |
| `homeassistant` | Integration package for Home Assistant workflows |
| `theme` | Shared theme and design foundations |
| `devtools` | Diagnostics and development tools |
| `kernel` | Module contracts, service container and infrastructure |
| `workspace` | Workspace readiness contracts |
| `file-studio` | Internal File Studio contracts and Runtime adapter; the installable web plugin remains external |
| `notifyarchive` | Internal notification archive contracts |

## Architecture Principles

ATLAS follows a few fixed principles:

- clear separation between contracts and implementations
- small, replaceable modules
- testable components
- dependencies through defined interfaces
- reference implementations for central services
- long-term plugin extensibility

## Events

The event layer includes:

- `Event`
- `EventBus`
- `Handler`
- `Subscription`
- `Filter`
- `Publisher`
- `Subscriber`

`DefaultEventBus` is the reference implementation.

## Services and Dependency Injection

The Runtime Foundation contains the groundwork for:

- service descriptors
- service registration
- dependency injection
- service containers
- controlled dependency resolution

## Current use and outlook {#planned-usage}

Administration and the Home Assistant Card Editor reference plugin are already available. Further tools and diagnostics are integrated through plugins. ATLAS provides a foundation for:

- Home Assistant tools
- dashboard components
- diagnostics applications
- plugin-based desktop or web applications
- the planned **Lovelace UV Card**

The contracts are still in development; this architecture does not promise a
stable plugin API. See [Development Status](/en/projects/atlas/development-status).
