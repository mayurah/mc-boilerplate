
# Managed Connector Boilerplate

This repository acts as a template/boilerlate for building TruStar Managed Connectors.


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

For access to Intel Workflows/API 2.0

`WORKFLOW_USER_API_KEY`

`WORKFLOW_USER_API_SECRET`

For 1.3 API

`LEGACY_USER_API_KEY`

`LEGACY_USER_API_SECRET`

  
## Installation

Ensure that Docker is installed
Clone the repo

Setup Envionment variables

```bash
  % cd path_to_repo/mc-boilerplate
  % cp .env.example .env
```
Edit the .env file with your API key and secret

Build the docker container

```bash
   % docker network create managed-connector
   % docker-compose up --build --remove-orphans
```

Once built and ran you should see the following:

```
Attaching to mc-boilerplate_mc_boilerplate_1
mc_boilerplate_1  | {"message": "Response TS 1.3: pong", "level": "INFO", "module": "mc_boilerplate.main", "time": "2021-09-17T19:34:17.357344"}
mc_boilerplate_1  | {"message": "Response TS 2.0: {'result': 'pong\\n'}", "level": "INFO", "module": "mc_boilerplate.main", "time": "2021-09-17T19:34:18.655587"}
mc-boilerplate_mc_boilerplate_1 exited with code 0
```