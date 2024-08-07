FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

USER vscode

# Install rye
RUN curl -sSf https://rye.astral.sh/get | RYE_INSTALL_OPTION="--yes" bash && \
    echo "export PATH=\$PATH:$HOME/.rye/bin" >> /home/vscode/.bashrc && \
    echo "source <(rye self completion bash)" >> /home/vscode/.bashrc
