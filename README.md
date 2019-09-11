# IncidentResponse

Protolabs Incident Response Platform V2 is built using Monzo's open source [Response](https://github.com/monzo/response) framework developed in Python and deployed using Docker.

## Getting started with local development

// TODO

### Adding new actions

The Response framework can be extended and custom actions added using the building block methods provided by the framework. These are documented in Monzo's [development documentation](https://github.com/monzo/response/blob/master/docs/development.md#building-blocks).

Custom actions should be added within the `demo/actions/*.py` files that already exist for each action type at the time of documentation creation. For example, `demo/actions/incident_commands.py` contains custom incidents commands.

### Adding new UI views

// TODO

## Deployment

// TODO