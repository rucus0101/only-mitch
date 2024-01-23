ARG FROM_IMAGE
ARG FROM_VARIANT

FROM ${FROM_IMAGE}:${FROM_VARIANT}

ARG USERNAME
USER ${USERNAME}

RUN bash -c "$(curl -sL https://get.containerlab.dev)"; \
    bash -c "$(curl -sL https://raw.githubusercontent.com/hellt/cmdo/master/get.sh)"; \
    sudo mv cmdo /bin/; \
    pip3 install passlib cookiecutter; \
    sudo apt-get update; sudo apt-get -y install xz-utils; \
    echo "zstyle ':completion:*:*:make:*' tag-order 'targets'" >> ~/.zshrc; \
    echo "autoload -U compinit && compinit" >> ~/.zshrc
