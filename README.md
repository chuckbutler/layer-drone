# DRONE layer

Drone is a self-hosted Continuous Integration server based on docker.

This layer consumes `layer:docker`, and spins up Drone in a docker container.
Currently the layer is not configured to enable peering to scale the build
service across multiple nodes, future moving versions of the layer will support
scale-out operations.

Presently, the charm only integrates with GitHub, and will not start the
Drone service until you have configured the charm with `github_client` and
`github_secret`.
