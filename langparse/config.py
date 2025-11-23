import os
from pathlib import Path
from typing import Any, Dict, Optional
import json

class Config:
    """
    Global configuration manager for LangParse.
    Priorities:
    1. Runtime kwargs (passed to functions)
    2. Environment variables (LANGPARSE_*)
    3. Config file (~/.langparse/config.json)
    4. Defaults
    """
    
    DEFAULT_CONFIG = {
        "default_pdf_engine": "simple",
        "engines": {
            "mineru": {
                "model_dir": None,  # Auto-download or user specified
                "device": "cpu"
            },
            "vision_llm": {
                "provider": "openai",
                "model": "gpt-4o",
                "api_key": None
            }
        }
    }
    
    def __init__(self):
        self._config = self.DEFAULT_CONFIG.copy()
        self._load_from_file()
        self._load_from_env()
        
    def _load_from_file(self):
        config_path = Path.home() / ".langparse" / "config.json"
        if config_path.exists():
            try:
                with open(config_path, 'r') as f:
                    user_config = json.load(f)
                    self._merge_dict(self._config, user_config)
            except Exception as e:
                print(f"Warning: Failed to load config file: {e}")

    def _load_from_env(self):
        # Example: LANGPARSE_VISION_LLM_API_KEY -> engines.vision_llm.api_key
        pass # TODO: Implement full env var mapping if needed

    def _merge_dict(self, base: Dict, update: Dict):
        for k, v in update.items():
            if k in base and isinstance(base[k], dict) and isinstance(v, dict):
                self._merge_dict(base[k], v)
            else:
                base[k] = v

    def get(self, key: str, default: Any = None) -> Any:
        """Get a config value using dot notation, e.g. 'engines.mineru.model_dir'"""
        keys = key.split('.')
        val = self._config
        for k in keys:
            if isinstance(val, dict) and k in val:
                val = val[k]
            else:
                return default
        return val

# Singleton instance
settings = Config()
