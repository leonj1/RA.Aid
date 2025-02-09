"""
List of model parameters
"""
from typing import Final
from enum import Enum
from typing import List, Set

DEFAULT_TOKEN_LIMIT = 100000

class Capability(str, Enum):
    LOGICAL = "logical"
    MATHEMATICAL = "mathematical"
    CODE_ANALYSIS = "code_analysis"
    CODE_GENERATION = "code_generation"
    PROBLEM_DECOMPOSITION = "problem_decomposition"
    CHAIN_OF_THOUGHT = "chain_of_thought"

    @classmethod
    def list(cls) -> List[str]:
        """Return all capabilities as a list of strings."""
        return [cap.value for cap in cls]
    
    @classmethod
    def set(cls) -> Set[str]:
        """Return all capabilities as a set of strings."""
        return {cap.value for cap in cls}

# Define reasoning tiers as constants to ensure consistency
class ReasoningTier:
    NONE: Final[int] = 0        # No specific reasoning capabilities
    BASIC: Final[int] = 1       # Basic logical reasoning
    ADVANCED: Final[int] = 2    # Advanced reasoning with multiple capabilities
    EXPERT: Final[int] = 3      # Expert-level reasoning with all capabilities

# TODO: make the provider the top-level key
reasoning_tiers = {
    "o1-preview": {
        "tier": ReasoningTier.EXPERT,
        "provider": "openai",
        "capabilities": [Capability.LOGICAL, Capability.MATHEMATICAL, Capability.CODE_ANALYSIS, Capability.CHAIN_OF_THOUGHT, Capability.CODE_GENERATION, Capability.PROBLEM_DECOMPOSITION],
    },
    "o1": {
        "tier": ReasoningTier.EXPERT,
        "provider": "openai",
        "capabilities": [Capability.LOGICAL, Capability.MATHEMATICAL, Capability.CODE_ANALYSIS, Capability.CHAIN_OF_THOUGHT, Capability.CODE_GENERATION, Capability.PROBLEM_DECOMPOSITION],
    },
    "o1-mini": {
        "tier": ReasoningTier.ADVANCED,
        "provider": "openai",
        "capabilities": [Capability.LOGICAL, Capability.MATHEMATICAL, Capability.CODE_ANALYSIS, Capability.CHAIN_OF_THOUGHT, Capability.CODE_GENERATION, Capability.PROBLEM_DECOMPOSITION],
    },
    "deepseek-reasoner": {
        "tier": ReasoningTier.EXPERT,
        "provider": "deepseek",
        "capabilities": [Capability.LOGICAL, Capability.MATHEMATICAL, Capability.CODE_ANALYSIS, Capability.CHAIN_OF_THOUGHT, Capability.CODE_GENERATION, Capability.PROBLEM_DECOMPOSITION],
    },
    "claude-3-sonnet-20240229": {
        "tier": ReasoningTier.EXPERT,
        "provider": "anthropic",
        "capabilities": [Capability.LOGICAL, Capability.MATHEMATICAL, Capability.CODE_ANALYSIS, Capability.CHAIN_OF_THOUGHT, Capability.CODE_GENERATION, Capability.PROBLEM_DECOMPOSITION],
    },
}

models_params = {
    "openai": {
        "gpt-3.5-turbo-0125": {"token_limit": 16385, "supports_temperature": True},
        "gpt-3.5": {"token_limit": 4096, "supports_temperature": True},
        "gpt-3.5-turbo": {"token_limit": 16385, "supports_temperature": True},
        "gpt-3.5-turbo-1106": {"token_limit": 16385, "supports_temperature": True},
        "gpt-3.5-turbo-instruct": {"token_limit": 4096, "supports_temperature": True},
        "gpt-4-0125-preview": {"token_limit": 128000, "supports_temperature": True},
        "gpt-4-turbo-preview": {"token_limit": 128000, "supports_temperature": True},
        "gpt-4-turbo": {"token_limit": 128000, "supports_temperature": True},
        "gpt-4-turbo-2024-04-09": {"token_limit": 128000, "supports_temperature": True},
        "gpt-4-1106-preview": {"token_limit": 128000, "supports_temperature": True},
        "gpt-4-vision-preview": {"token_limit": 128000, "supports_temperature": True},
        "gpt-4": {"token_limit": 8192, "supports_temperature": True},
        "gpt-4-0613": {"token_limit": 8192, "supports_temperature": True},
        "gpt-4-32k": {"token_limit": 32768, "supports_temperature": True},
        "gpt-4-32k-0613": {"token_limit": 32768, "supports_temperature": True},
        "gpt-4o": {"token_limit": 128000, "supports_temperature": True},
        "gpt-4o-2024-08-06": {"token_limit": 128000, "supports_temperature": True},
        "gpt-4o-2024-05-13": {"token_limit": 128000, "supports_temperature": True},
        "gpt-4o-mini": {"token_limit": 128000, "supports_temperature": True},
        "o1-preview": {"token_limit": 128000, "supports_temperature": False},
        "o1-mini": {"token_limit": 128000, "supports_temperature": False},
        "o1-preview": {"token_limit": 128000, "supports_temperature": False},
        "o1": {"token_limit": 200000, "supports_temperature": False},
        "o3-mini": {"token_limit": 200000, "supports_temperature": False},
    },
    "azure_openai": {
        "gpt-3.5-turbo-0125": {"token_limit": 16385, "supports_temperature": True},
        "gpt-3.5": {"token_limit": 4096, "supports_temperature": True},
        "gpt-3.5-turbo": {"token_limit": 16385, "supports_temperature": True},
        "gpt-3.5-turbo-1106": {"token_limit": 16385, "supports_temperature": True},
        "gpt-3.5-turbo-instruct": {"token_limit": 4096, "supports_temperature": True},
        "gpt-4-0125-preview": {"token_limit": 128000, "supports_temperature": True},
        "gpt-4-turbo-preview": {"token_limit": 128000, "supports_temperature": True},
        "gpt-4-turbo": {"token_limit": 128000, "supports_temperature": True},
        "gpt-4-turbo-2024-04-09": {"token_limit": 128000, "supports_temperature": True},
        "gpt-4-1106-preview": {"token_limit": 128000, "supports_temperature": True},
        "gpt-4-vision-preview": {"token_limit": 128000, "supports_temperature": True},
        "gpt-4": {"token_limit": 8192, "supports_temperature": True},
        "gpt-4-0613": {"token_limit": 8192, "supports_temperature": True},
        "gpt-4-32k": {"token_limit": 32768, "supports_temperature": True},
        "gpt-4-32k-0613": {"token_limit": 32768, "supports_temperature": True},
        "gpt-4o": {"token_limit": 128000, "supports_temperature": True},
        "gpt-4o-mini": {"token_limit": 128000, "supports_temperature": True},
        "chatgpt-4o-latest": {"token_limit": 128000, "supports_temperature": True},
        "o1-preview": {"token_limit": 128000, "supports_temperature": False},
        "o1-mini": {"token_limit": 128000, "supports_temperature": False},
    },
    "google_genai": {
        "gemini-pro": {"token_limit": 128000, "supports_temperature": True},
        "gemini-1.5-flash-latest": {
            "token_limit": 128000,
            "supports_temperature": True,
        },
        "gemini-1.5-pro-latest": {"token_limit": 128000, "supports_temperature": True},
        "models/embedding-001": {"token_limit": 2048, "supports_temperature": True},
    },
    "google_vertexai": {
        "gemini-1.5-flash": {"token_limit": 128000, "supports_temperature": True},
        "gemini-1.5-pro": {"token_limit": 128000, "supports_temperature": True},
        "gemini-1.0-pro": {"token_limit": 128000, "supports_temperature": True},
    },
    "ollama": {
        "command-r": {"token_limit": 12800, "supports_temperature": True},
        "codellama": {"token_limit": 16000, "supports_temperature": True},
        "dbrx": {"token_limit": 32768, "supports_temperature": True},
        "deepseek-coder:33b": {"token_limit": 16000, "supports_temperature": True},
        "falcon": {"token_limit": 2048, "supports_temperature": True},
        "llama2": {"token_limit": 4096, "supports_temperature": True},
        "llama2:7b": {"token_limit": 4096, "supports_temperature": True},
        "llama2:13b": {"token_limit": 4096, "supports_temperature": True},
        "llama2:70b": {"token_limit": 4096, "supports_temperature": True},
        "llama3": {"token_limit": 8192, "supports_temperature": True},
        "llama3:8b": {"token_limit": 8192, "supports_temperature": True},
        "llama3:70b": {"token_limit": 8192, "supports_temperature": True},
        "llama3.1": {"token_limit": 128000, "supports_temperature": True},
        "llama3.1:8b": {"token_limit": 128000, "supports_temperature": True},
        "llama3.1:70b": {"token_limit": 128000, "supports_temperature": True},
        "lama3.1:405b": {"token_limit": 128000, "supports_temperature": True},
        "llama3.2": {"token_limit": 128000, "supports_temperature": True},
        "llama3.2:1b": {"token_limit": 128000, "supports_temperature": True},
        "llama3.2:3b": {"token_limit": 128000, "supports_temperature": True},
        "llama3.3:70b": {"token_limit": 128000, "supports_temperature": True},
        "scrapegraph": {"token_limit": 8192, "supports_temperature": True},
        "mistral-small": {"token_limit": 128000, "supports_temperature": True},
        "mistral-openorca": {"token_limit": 32000, "supports_temperature": True},
        "mistral-large": {"token_limit": 128000, "supports_temperature": True},
        "grok-1": {"token_limit": 8192, "supports_temperature": True},
        "llava": {"token_limit": 4096, "supports_temperature": True},
        "mixtral:8x22b-instruct": {"token_limit": 65536, "supports_temperature": True},
        "nomic-embed-text": {"token_limit": 8192, "supports_temperature": True},
        "nous-hermes2:34b": {"token_limit": 4096, "supports_temperature": True},
        "orca-mini": {"token_limit": 2048, "supports_temperature": True},
        "phi3:3.8b": {"token_limit": 12800, "supports_temperature": True},
        "phi3:14b": {"token_limit": 128000, "supports_temperature": True},
        "qwen:0.5b": {"token_limit": 32000, "supports_temperature": True},
        "qwen:1.8b": {"token_limit": 32000, "supports_temperature": True},
        "qwen:4b": {"token_limit": 32000, "supports_temperature": True},
        "qwen:14b": {"token_limit": 32000, "supports_temperature": True},
        "qwen:32b": {"token_limit": 32000, "supports_temperature": True},
        "qwen:72b": {"token_limit": 32000, "supports_temperature": True},
        "qwen:110b": {"token_limit": 32000, "supports_temperature": True},
        "stablelm-zephyr": {"token_limit": 8192, "supports_temperature": True},
        "wizardlm2:8x22b": {"token_limit": 65536, "supports_temperature": True},
        "mistral": {"token_limit": 128000, "supports_temperature": True},
        "gemma2": {"token_limit": 128000, "supports_temperature": True},
        "gemma2:9b": {"token_limit": 128000, "supports_temperature": True},
        "gemma2:27b": {"token_limit": 128000, "supports_temperature": True},
        # embedding models
        "shaw/dmeta-embedding-zh-small-q4": {
            "token_limit": 8192,
            "supports_temperature": True,
        },
        "shaw/dmeta-embedding-zh-q4": {
            "token_limit": 8192,
            "supports_temperature": True,
        },
        "chevalblanc/acge_text_embedding": {
            "token_limit": 8192,
            "supports_temperature": True,
        },
        "martcreation/dmeta-embedding-zh": {
            "token_limit": 8192,
            "supports_temperature": True,
        },
        "snowflake-arctic-embed": {"token_limit": 8192, "supports_temperature": True},
        "mxbai-embed-large": {"token_limit": 512, "supports_temperature": True},
    },
    "oneapi": {"qwen-turbo": {"token_limit": 6000, "supports_temperature": True}},
    "nvidia": {
        "meta/llama3-70b-instruct": {"token_limit": 419, "supports_temperature": True},
        "meta/llama3-8b-instruct": {"token_limit": 419, "supports_temperature": True},
        "nemotron-4-340b-instruct": {"token_limit": 1024, "supports_temperature": True},
        "databricks/dbrx-instruct": {"token_limit": 4096, "supports_temperature": True},
        "google/codegemma-7b": {"token_limit": 8192, "supports_temperature": True},
        "google/gemma-2b": {"token_limit": 2048, "supports_temperature": True},
        "google/gemma-7b": {"token_limit": 8192, "supports_temperature": True},
        "google/recurrentgemma-2b": {"token_limit": 2048, "supports_temperature": True},
        "meta/codellama-70b": {"token_limit": 16384, "supports_temperature": True},
        "meta/llama2-70b": {"token_limit": 4096, "supports_temperature": True},
        "microsoft/phi-3-mini-128k-instruct": {
            "token_limit": 122880,
            "supports_temperature": True,
        },
        "mistralai/mistral-7b-instruct-v0.2": {
            "token_limit": 4096,
            "supports_temperature": True,
        },
        "mistralai/mistral-large": {"token_limit": 8192, "supports_temperature": True},
        "mistralai/mixtral-8x22b-instruct-v0.1": {
            "token_limit": 32768,
            "supports_temperature": True,
        },
        "mistralai/mixtral-8x7b-instruct-v0.1": {
            "token_limit": 8192,
            "supports_temperature": True,
        },
        "snowflake/arctic": {"token_limit": 16384, "supports_temperature": True},
    },
    "groq": {
        "llama3-8b-8192": {"token_limit": 8192, "supports_temperature": True},
        "llama3-70b-8192": {"token_limit": 8192, "supports_temperature": True},
        "mixtral-8x7b-32768": {"token_limit": 32768, "supports_temperature": True},
        "gemma-7b-it": {"token_limit": 8192, "supports_temperature": True},
        "claude-3-haiku-20240307'": {"token_limit": 8192, "supports_temperature": True},
    },
    "toghetherai": {
        "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo": {
            "token_limit": 128000,
            "supports_temperature": True,
        },
        "meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo": {
            "token_limit": 128000,
            "supports_temperature": True,
        },
        "mistralai/Mixtral-8x22B-Instruct-v0.1": {
            "token_limit": 128000,
            "supports_temperature": True,
        },
        "stabilityai/stable-diffusion-xl-base-1.0": {
            "token_limit": 2048,
            "supports_temperature": True,
        },
        "meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo": {
            "token_limit": 128000,
            "supports_temperature": True,
        },
        "NousResearch/Hermes-3-Llama-3.1-405B-Turbo": {
            "token_limit": 128000,
            "supports_temperature": True,
        },
        "Gryphe/MythoMax-L2-13b-Lite": {
            "token_limit": 8192,
            "supports_temperature": True,
        },
        "Salesforce/Llama-Rank-V1": {"token_limit": 8192, "supports_temperature": True},
        "meta-llama/Meta-Llama-Guard-3-8B": {
            "token_limit": 128000,
            "supports_temperature": True,
        },
        "meta-llama/Meta-Llama-3-70B-Instruct-Turbo": {
            "token_limit": 128000,
            "supports_temperature": True,
        },
        "meta-llama/Llama-3-8b-chat-hf": {
            "token_limit": 8192,
            "supports_temperature": True,
        },
        "meta-llama/Llama-3-70b-chat-hf": {
            "token_limit": 8192,
            "supports_temperature": True,
        },
        "Qwen/Qwen2-72B-Instruct": {
            "token_limit": 128000,
            "supports_temperature": True,
        },
        "google/gemma-2-27b-it": {"token_limit": 8192, "supports_temperature": True},
    },
    "anthropic": {
        "claude_instant": {"token_limit": 100000, "supports_temperature": True},
        "claude2": {"token_limit": 9000, "supports_temperature": True},
        "claude2.1": {"token_limit": 200000, "supports_temperature": True},
        "claude3": {"token_limit": 200000, "supports_temperature": True},
        "claude3.5": {"token_limit": 200000, "supports_temperature": True},
        "claude-3-opus-20240229": {"token_limit": 200000, "supports_temperature": True},
        "claude-3-sonnet-20240229": {
            "token_limit": 200000,
            "supports_temperature": True,
        },
        "claude-3-haiku-20240307": {
            "token_limit": 200000,
            "supports_temperature": True,
        },
        "claude-3-5-sonnet-20240620": {
            "token_limit": 200000,
            "supports_temperature": True,
        },
        "claude-3-5-sonnet-20241022": {
            "token_limit": 200000,
            "supports_temperature": True,
        },
        "claude-3-5-haiku-latest": {
            "token_limit": 200000,
            "supports_temperature": True,
        },
    },
    "bedrock": {
        "anthropic.claude-3-haiku-20240307-v1:0": {
            "token_limit": 200000,
            "supports_temperature": True,
        },
        "anthropic.claude-3-sonnet-20240229-v1:0": {
            "token_limit": 200000,
            "supports_temperature": True,
        },
        "anthropic.claude-3-opus-20240229-v1:0": {
            "token_limit": 200000,
            "supports_temperature": True,
        },
        "anthropic.claude-3-5-sonnet-20240620-v1:0": {
            "token_limit": 200000,
            "supports_temperature": True,
        },
        "claude-3-5-haiku-latest": {
            "token_limit": 200000,
            "supports_temperature": True,
        },
        "anthropic.claude-v2:1": {"token_limit": 200000, "supports_temperature": True},
        "anthropic.claude-v2": {"token_limit": 100000, "supports_temperature": True},
        "anthropic.claude-instant-v1": {
            "token_limit": 100000,
            "supports_temperature": True,
        },
        "meta.llama3-8b-instruct-v1:0": {
            "token_limit": 8192,
            "supports_temperature": True,
        },
        "meta.llama3-70b-instruct-v1:0": {
            "token_limit": 8192,
            "supports_temperature": True,
        },
        "meta.llama2-13b-chat-v1": {"token_limit": 4096, "supports_temperature": True},
        "meta.llama2-70b-chat-v1": {"token_limit": 4096, "supports_temperature": True},
        "mistral.mistral-7b-instruct-v0:2": {
            "token_limit": 32768,
            "supports_temperature": True,
        },
        "mistral.mixtral-8x7b-instruct-v0:1": {
            "token_limit": 32768,
            "supports_temperature": True,
        },
        "mistral.mistral-large-2402-v1:0": {
            "token_limit": 32768,
            "supports_temperature": True,
        },
        "mistral.mistral-small-2402-v1:0": {
            "token_limit": 32768,
            "supports_temperature": True,
        },
        "amazon.titan-embed-text-v1": {
            "token_limit": 8000,
            "supports_temperature": True,
        },
        "amazon.titan-embed-text-v2:0": {
            "token_limit": 8000,
            "supports_temperature": True,
        },
        "cohere.embed-english-v3": {"token_limit": 512, "supports_temperature": True},
        "cohere.embed-multilingual-v3": {
            "token_limit": 512,
            "supports_temperature": True,
        },
    },
    "mistralai": {
        "mistral-large-latest": {"token_limit": 128000, "supports_temperature": True},
        "open-mistral-nemo": {"token_limit": 128000, "supports_temperature": True},
        "codestral-latest": {"token_limit": 32000, "supports_temperature": True},
    },
    "togetherai": {
        "Meta-Llama-3.1-70B-Instruct-Turbo": {
            "token_limit": 128000,
            "supports_temperature": True,
        }
    },
}
