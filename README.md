# Time tracker
IOET Time tracker system

## Architecture
The application follows a DDD approach with a hexagonal clean architecture. BIG WORDS!, what does it mean? it means the following:
- We have a directory for each domain entitiy (i.e. time entries, technologies, activities, etc)
- Inside each entity directory we have other 3 directories (application, domain and infrastructure)
- I'll leave this drawing to understand how these three folders work and what logic should be included in these directories:
![DDD design](/ddd.png)
Taken from [Microsoft Docs](https://docs.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/ddd-oriented-microservice)

## How to contribute
- Clone the repository, create a new branch, implement the logic taken the architecture into account and create a PR
- Wait for the pipeline to run a be on green
- Please ask for peer review in the #timetracker-collaboration slack channel
