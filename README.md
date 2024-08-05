# ai-commit

Automatic generation of commit messages

## Install

Place ai-commit in a location included in your PATH

Such as `${HOME}/.local/bin` or `/usr/local/bin`

## Usage

Set your OpenAI API key as an environment variable.

Add this to your `.bashrc` or similar:

```bash
export OPENAI_API_KEY=sk-******************************
```

Execute the command in a git repository to create a commit message.

```bash
ai-commit
```

## Roadmap

- [ ] Add support for other AI models
- [ ] Add configuration options
- [ ] Add custom templates
- [ ] Add argument parsing
- [ ] Allow editing generated commit messages in an editor after creation
