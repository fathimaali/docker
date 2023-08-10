# docker file syntax

elements in a docker file

* instructions: written in caps
    - FROM - sets the base image for a build, eg.alpine
    - LABEL - adds metadata to an image (eg.description)
    - RUN - runs commands in a new layer (eg. installs or config) --> creates a new layer
    - COPY - copy **new** files/folders from src (client machine) to destination --> creates a new layer 
    - ADD - as above, but can add **existing** files from a remote URL and do extraction etc --> creates a new layer 
    - CMD - default executable of a container. can be overriden via docker run parameters.  use case: general purpose image 
    - ENTRYPOINT - same as CMD, but cannot be overriden. use case: single purpose image
    - EXPOSE - informs docker what port the container app is running on (this is simply metadata, this does not perform network config)

* arguments: values passed to the instructions


