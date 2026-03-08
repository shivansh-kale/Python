"""
CONFIGURATION MANAGEMENT IN PYTHON
----------------------------------

Configuration management separates settings from code.

Common configuration methods:

1. Environment variables
2. .env files
3. JSON / YAML config files
4. Configuration classes

These are widely used in:
- ML pipelines
- web applications
- deployment environments
"""

# =========================================================
# 1. ENVIRONMENT VARIABLES
# =========================================================

"""
Environment variables store configuration outside the code.
"""

import os

# Access environment variable
database_url = os.getenv("DATABASE_URL")

print("Database URL:", database_url)


# Setting environment variable (example)
os.environ["APP_MODE"] = "development"

print("App mode:", os.getenv("APP_MODE"))


# =========================================================
# 2. USING .ENV FILES
# =========================================================

"""
.env files store environment variables in a file.

Example .env file:

DATABASE_URL=postgresql://user:password@localhost/db
API_KEY=secret_key
"""

from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

api_key = os.getenv("API_KEY")

print("API key:", api_key)


# =========================================================
# 3. JSON CONFIGURATION FILE
# =========================================================

"""
Configuration can be stored in JSON files.
"""

import json

config_data = {
    "app_name": "ML App",
    "debug": True,
    "batch_size": 32
}

# Save configuration
with open("config.json", "w") as f:
    json.dump(config_data, f, indent=4)

# Load configuration
with open("config.json", "r") as f:
    config = json.load(f)

print("Config loaded:", config)


# =========================================================
# 4. YAML CONFIGURATION
# =========================================================

"""
YAML is commonly used for configuration files
because it is easier to read than JSON.
"""

import yaml

yaml_config = {
    "learning_rate": 0.001,
    "epochs": 10
}

# Save YAML
with open("config.yaml", "w") as f:
    yaml.dump(yaml_config, f)

# Load YAML
with open("config.yaml", "r") as f:
    config_yaml = yaml.safe_load(f)

print("YAML config:", config_yaml)


# =========================================================
# 5. CONFIGURATION CLASS
# =========================================================

"""
A configuration class organizes settings in a structured way.
"""

class Config:

    DEBUG = True
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite://local.db")
    API_KEY = os.getenv("API_KEY", "default_key")


config = Config()

print("Debug mode:", config.DEBUG)
print("Database:", config.DATABASE_URL)