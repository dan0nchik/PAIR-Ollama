from enum import Enum

VICUNA_PATH = "/home/pzhao/vicuna-13b-v1.5"
LLAMA_PATH = "/home/pzhao/Llama-2-7b-chat-hf"

ATTACK_TEMP = 1
TARGET_TEMP = 0
ATTACK_TOP_P = 0.9
TARGET_TOP_P = 1


## MODEL PARAMETERS ##
class Model(Enum):
    vicuna = "vicuna-13b-v1.5"
    gpt_3_5 = "gpt-3.5-turbo-1106"
    gpt_4 = "gpt-4o-mini"
    claude_1 = "claude-instant-1.2"
    claude_2 = "claude-2.1"
    gemini = "gemini-pro"
    mixtral = "mixtral"
    llama_2 = "llama2"
    llama_2_uncensored = "llama2-uncensored"
    mixtral_ollama = "mixtral:8x7b"
    llama3 = "llama3.1:8b"
    tinyllama = "tinyllama"
    gemma_2b = "gemma:2b"
    gemma_7b = "gemma:7b"


MODEL_NAMES = [model.value for model in Model]


HF_MODEL_NAMES: dict[Model, str] = {
    Model.llama_2: "meta-llama/Llama-2-7b-chat-hf",
    Model.vicuna: "lmsys/vicuna-13b-v1.5",
    Model.mixtral: "mistralai/Mixtral-8x7B-Instruct-v0.1",
}

OLLAMA_MODEL_NAMES: dict[Model, str] = {
    Model.llama_2: "ollama/llama2",
    Model.llama_2_uncensored: "ollama/llama2-uncensored",
    Model.tinyllama: "ollama/tinyllama",
    Model.gemma_2b: "ollama/gemma:2b",
    Model.gemma_7b: "ollama/gemma:7b",
    Model.mixtral_ollama: "ollama/mixtral:8x7b",
    Model.llama3: "ollama/llama3.1:8b",
}

TOGETHER_MODEL_NAMES: dict[Model, str] = {
    # Model.llama_2: "together_ai/togethercomputer/llama-2-7b-chat",
    Model.vicuna: "together_ai/lmsys/vicuna-13b-v1.5",
    Model.mixtral: "together_ai/mistralai/Mixtral-8x7B-Instruct-v0.1",
}

FASTCHAT_TEMPLATE_NAMES: dict[Model, str] = {
    Model.gpt_3_5: "gpt-3.5-turbo",
    Model.gpt_4: "gpt-4o-mini",
    Model.claude_1: "claude-instant-1.2",
    Model.claude_2: "claude-2.1",
    Model.gemini: "gemini-pro",
    Model.vicuna: "vicuna_v1.1",
    Model.llama_2: "llama-2-7b-chat-hf",
    Model.mixtral: "mixtral",
    Model.llama_2_uncensored: "ollama/llama2-uncensored",
    Model.tinyllama: "ollama/tinyllama",
    Model.mixtral_ollama: "ollama/mixtral:8x7b",
    Model.llama3: "ollama/llama3.1:8b",
}

API_KEY_NAMES: dict[Model, str] = {
    Model.gpt_3_5: "OPENAI_API_KEY",
    Model.gpt_4: "OPENAI_API_KEY",
    Model.claude_1: "ANTHROPIC_API_KEY",
    Model.claude_2: "ANTHROPIC_API_KEY",
    Model.gemini: "GEMINI_API_KEY",
    Model.vicuna: "TOGETHER_API_KEY",
    Model.llama_2: "TOGETHER_API_KEY",
    Model.mixtral: "TOGETHER_API_KEY",
}

LITELLM_TEMPLATES: dict[Model, dict] = {
    Model.vicuna: {
        "roles": {
            "system": {"pre_message": "", "post_message": " "},
            "user": {"pre_message": "USER: ", "post_message": " ASSISTANT:"},
            "assistant": {
                "pre_message": "",
                "post_message": "",
            },
        },
        "post_message": "</s>",
        "initial_prompt_value": "",
        "eos_tokens": ["</s>"],
    },
    Model.llama_2: {
        "roles": {
            "system": {
                "pre_message": "[INST] <<SYS>>\n",
                "post_message": "\n<</SYS>>\n\n",
            },
            "user": {"pre_message": "", "post_message": " [/INST]"},
            "assistant": {"pre_message": "", "post_message": ""},
        },
        "post_message": " </s><s>",
        "initial_prompt_value": "",
        "eos_tokens": ["</s>", "[/INST]"],
    },
    Model.llama_2_uncensored: {
        "roles": {
            "system": {
                "pre_message": "[INST] <<SYS>>\n",
                "post_message": "\n<</SYS>>\n\n",
            },
            "user": {"pre_message": "", "post_message": " [/INST]"},
            "assistant": {"pre_message": "", "post_message": ""},
        },
        "post_message": " </s><s>",
        "initial_prompt_value": "",
        "eos_tokens": ["</s>", "[/INST]"],
    },
    Model.mixtral_ollama: {
        "roles": {
            "system": {"pre_message": "[INST] ", "post_message": " [/INST]"},
            "user": {"pre_message": "[INST] ", "post_message": " [/INST]"},
            "assistant": {
                "pre_message": " ",
                "post_message": "",
            },
        },
        "post_message": "</s>",
        "initial_prompt_value": "<s>",
        "eos_tokens": ["</s>", "[/INST]"],
    },
    Model.llama3: {
        "roles": {
            "system": {
                "pre_message": "[INST] <<SYS>>\n",
                "post_message": "\n<</SYS>>\n\n",
            },
            "user": {"pre_message": "", "post_message": " [/INST]"},
            "assistant": {"pre_message": "", "post_message": ""},
        },
        "post_message": " </s><s>",
        "initial_prompt_value": "",
        "eos_tokens": ["</s>", "[/INST]"],
    },
    Model.tinyllama: {
        "roles": {
            "system": {
                "pre_message": "[INST] <<SYS>>\n",
                "post_message": "\n<</SYS>>\n\n",
            },
            "user": {"pre_message": "", "post_message": " [/INST]"},
            "assistant": {"pre_message": "", "post_message": ""},
        },
        "post_message": " </s><s>",
        "initial_prompt_value": "",
        "eos_tokens": ["</s>", "[/INST]"],
    },
    Model.gemma_2b: {
        "roles": {
            "system": {
                "pre_message": "[INST] <<SYS>>\n",
                "post_message": "\n<</SYS>>\n\n",
            },
            "user": {"pre_message": "", "post_message": " [/INST]"},
            "assistant": {"pre_message": "", "post_message": ""},
        },
        "post_message": " </s><s>",
        "initial_prompt_value": "",
        "eos_tokens": ["</s>", "[/INST]"],
    },
    Model.gemma_7b: {
        "roles": {
            "system": {
                "pre_message": "[INST] <<SYS>>\n",
                "post_message": "\n<</SYS>>\n\n",
            },
            "user": {"pre_message": "", "post_message": " [/INST]"},
            "assistant": {"pre_message": "", "post_message": ""},
        },
        "post_message": " </s><s>",
        "initial_prompt_value": "",
        "eos_tokens": ["</s>", "[/INST]"],
    },
    Model.mixtral: {
        "roles": {
            "system": {"pre_message": "[INST] ", "post_message": " [/INST]"},
            "user": {"pre_message": "[INST] ", "post_message": " [/INST]"},
            "assistant": {
                "pre_message": " ",
                "post_message": "",
            },
        },
        "post_message": "</s>",
        "initial_prompt_value": "<s>",
        "eos_tokens": ["</s>", "[/INST]"],
    },
}
