from abc import ABC, abstractmethod

from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Optional
import os
from pathlib import Path

from ai_commit.default_config import default_model, default_template


@dataclass_json
@dataclass
class AppConfig:
    prompt: str
    model: str = "gpt-4o-mini"


config_file_name = ".ai-commit.json"


class ConfigRepository(ABC):
    @abstractmethod
    def save(self, config: AppConfig) -> None:
        pass

    @abstractmethod
    def load(self) -> Optional[AppConfig]:
        pass


def search_config_file(path: Path) -> Optional[Path]:
    if (path / config_file_name).exists():
        return path / config_file_name
    if path == path.parent:
        return None
    return search_config_file(path.parent)


def default_config_file_path() -> Path:
    return search_config_file(Path.cwd()) or Path.home() / config_file_name


class JsonConfigRepository(ConfigRepository):
    def __init__(self, file_path: Path):
        self.file_path = file_path

    def save(self, config: AppConfig) -> None:
        with open(self.file_path, "w") as f:
            f.write(config.to_json())

    def load(self) -> Optional[AppConfig]:
        print("Loading config from", self.file_path)
        if not os.path.exists(self.file_path):
            return None
        with open(self.file_path, "r") as f:
            return AppConfig.from_json(f.read())


class ConfigService:
    def __init__(self, repository: ConfigRepository):
        self.repository = repository

    def save_config(self, config: AppConfig) -> None:
        self.repository.save(config)

    def get_config(self) -> AppConfig:
        try:
            return self.repository.load() or AppConfig(prompt=default_template, model=default_model)
        except Exception:
            print("Error loading config file")
            return AppConfig(prompt=default_template, model=default_model)
