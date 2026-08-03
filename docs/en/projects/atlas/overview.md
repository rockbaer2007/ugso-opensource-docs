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

## Planned Usage

ATLAS is intended to support:

- Home Assistant tools
- dashboard components
- diagnostics applications
- plugin-based desktop or web applications
- the planned **UGSo Thread Monitor**
