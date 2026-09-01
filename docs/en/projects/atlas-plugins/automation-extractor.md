# Automation Extractor

Automation Extractor is noted as another independent ATLAS plugin. The idea comes from the existing Windows tool for splitting `automations.yaml`, but should move directly into the ATLAS plugin architecture.

## Goal

The plugin should first analyze Home Assistant automations safely and later export or restructure them in a controlled way.

- read `automations.yaml`
- detect automations from packages and includes
- show id, alias, description, triggers, conditions and actions
- surface related entities, scripts, scenes, helpers and notification targets
- export individual automations as YAML files
- run later refactoring steps only with backup, validation, diff preview and a recovery path

## Safety Line

The first step should stay read-only. Writing changes to Home Assistant files belongs to a later stage once backup, YAML validation, diff preview and restore paths are in place.

## Positioning

Automation Extractor complements File Studio: File Studio is the safe file surface, while Automation Extractor becomes the domain-specific analysis and export surface for automations.
