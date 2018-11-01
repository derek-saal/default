# Purpose

# Build Instructions
1. `docker build -t `**project**`:latest .`
1. `docker run -p 8080:8080 -it `**project**`:latest`
1. Go to `localhost:8080/ui` for usage

# How it works

# Growth

# DevOps
* Implements /health_check
* Does not require other services
    * Does not need to specify consumed ports from other containers
* Does not require any data mount
* Does not use any env vars
* In-Container port is exposed on 8080
