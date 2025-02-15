import tiktoken

# Tokenizer
CL100K_ENCODER = tiktoken.get_encoding("cl100k_base")
P50K_ENCODER = tiktoken.get_encoding("p50k_base")


# OpenAI model details


openai_models = {  # Updated from https://platform.openai.com/docs/models/continuous-model-upgrades on 16th April 2024
    "qwen2.5-coder:14b": {
        "description": "qwen2.5-coder:14b",
        "context_window": 32_000,
        "training_data": "",
    },
    "granite3.1-dense:8b": {
        "description": "granite3.1-dense:8b",
        "context_window": 128_000,
        "training_data": "",
    },
    "llama3.1:8b": {
        "description": "llama3.1:8b",
        "context_window": 128_000,
        "training_data": "",
    },
    "llama-3.3-70b": {
        "description": "llama-3.3-70b",
        "context_window": 8_192,
        "training_data": "",
    },
    "gemma2:9b": {
        "description": "gemma2:9b",
        "context_window": 8_192,
        "training_data": "",
    },
    "gpt-4o": {
        "description": "GPT-4o ('o' for 'omni') is our versatile, high-intelligence flagship model.",
        "context_window": 128_000,
        "training_data": "Up to Aug 2024",
    },
    "gpt-4-turbo": {
        "description": "New GPT-4 Turbo with Vision. The latest GPT-4 Turbo model with vision capabilities. Vision requests can now use JSON mode and function calling. Currently points to gpt-4-turbo-2024-04-09.",
        "context_window": 128_000,
        "training_data": "Up to Dec 2023",
    },
    "gpt-4-turbo-2024-04-09": {
        "description": "GPT-4 Turbo with Vision model. Vision requests can now use JSON mode and function calling. gpt-4-turbo currently points to this version.",
        "context_window": 128_000,
        "training_data": "Up to Dec 2023",
    },
    "gpt-4-turbo-preview": {
        "description": "GPT-4 Turbo preview model. Currently points to gpt-4-0125-preview.",
        "context_window": 128_000,
        "training_data": "Up to Dec 2023",
    },
    "gpt-4-0125-preview": {
        "description": "GPT-4 Turbo preview model intended to reduce cases of “laziness” where the model doesn’t complete a task. Returns a maximum of 4,096 output tokens. Learn more.",
        "context_window": 128_000,
        "training_data": "Up to Dec 2023",
    },
    "gpt-4-1106-preview": {
        "description": "GPT-4 Turbo preview model featuring improved instruction following, JSON mode, reproducible outputs, parallel function calling, and more. Returns a maximum of 4,096 output tokens. This is a preview model. Learn more.",
        "context_window": 128_000,
        "training_data": "Up to Apr 2023",
    },
    "gpt-4-vision-preview": {
        "description": "GPT-4 model with the ability to understand images, in addition to all other GPT-4 Turbo capabilities. This is a preview model, we recommend developers to now use gpt-4-turbo which includes vision capabilities. Currently points to gpt-4-1106-vision-preview.",
        "context_window": 128_000,
        "training_data": "Up to Apr 2023",
    },
    "gpt-4-1106-vision-preview": {
        "description": "GPT-4 model with the ability to understand images, in addition to all other GPT-4 Turbo capabilities. This is a preview model, we recommend developers to now use gpt-4-turbo which includes vision capabilities. Returns a maximum of 4,096 output tokens. Learn more.",
        "context_window": 128_000,
        "training_data": "Up to Apr 2023",
    },
    "gpt-4": {
        "description": "Currently points to gpt-4-0613. See continuous model upgrades.",
        "context_window": 8_192,
        "training_data": "Up to Sep 2021",
    },
    "gpt-4-0613": {
        "description": "Snapshot of gpt-4 from June 13th 2023 with improved function calling support.",
        "context_window": 8_192,
        "training_data": "Up to Sep 2021",
    },
    "gpt-4-32k": {
        "description": "Currently points to gpt-4-32k-0613. See continuous model upgrades. This model was never rolled out widely in favor of GPT-4 Turbo.",
        "context_window": 32_768,
        "training_data": "Up to Sep 2021",
    },
    "gpt-4-32k-0613": {
        "description": "Snapshot of gpt-4-32k from June 13th 2023 with improved function calling support. This model was never rolled out widely in favor of GPT-4 Turbo.",
        "context_window": 32_768,
        "training_data": "Up to Sep 2021",
    },
    "gpt-3.5-turbo-0125": {
        "description": "New Updated GPT 3.5 Turbo. The latest GPT-3.5 Turbo model with higher accuracy at responding in requested formats and a fix for a bug which caused a text encoding issue for non-English language function calls. Returns a maximum of 4,096 output tokens. Learn more.",
        "context_window": 16_385,
        "training_data": "Up to Sep 2021",
    },
    "gpt-3.5-turbo": {
        "description": "Currently points to gpt-3.5-turbo-0125.",
        "context_window": 16_385,
        "training_data": "Up to Sep 2021",
    },
    "gpt-3.5-turbo-1106": {
        "description": "GPT-3.5 Turbo model with improved instruction following, JSON mode, reproducible outputs, parallel function calling, and more. Returns a maximum of 4,096 output tokens. Learn more.",
        "context_window": 16_385,
        "training_data": "Up to Sep 2021",
    },
    "gpt-3.5-turbo-instruct": {
        "description": "Similar capabilities as GPT-3 era models. Compatible with legacy Completions endpoint and not Chat Completions.",
        "context_window": 4_096,
        "training_data": "Up to Sep 2021",
    },
    "gpt-3.5-turbo-16k": {
        "description": "Legacy Currently points to gpt-3.5-turbo-16k-0613.",
        "context_window": 16_385,
        "training_data": "Up to Sep 2021",
    },
    "gpt-3.5-turbo-0613": {
        "description": "Legacy Snapshot of gpt-3.5-turbo from June 13th 2023. Will be deprecated on June 13, 2024.",
        "context_window": 4_096,
        "training_data": "Up to Sep 2021",
    },
    "gpt-3.5-turbo-16k-0613": {
        "description": "Legacy Snapshot of gpt-3.5-16k-turbo from June 13th 2023. Will be deprecated on June 13, 2024.",
        "context_window": 16_385,
        "training_data": "Up to Sep 2021",
    },
}

openai_rate_limits_per_tier_per_model = {  # Updated from https://platform.openai.com/docs/guides/rate-limits/usage-tiers?context=tier-free on 16th April 2024
    "free": {
        "gpt-3.5-turbo": {"RPM": 3, "RPD": 200, "TPM": 40000, "Batch Queue Limit": 200000},
        "text-embedding-3-small": {"RPM": 3, "RPD": 200, "TPM": 150000, "Batch Queue Limit": None},
        "whisper-1": {"RPM": 3, "RPD": 200, "TPM": None, "Batch Queue Limit": None},
        "tts-1": {"RPM": 3, "RPD": 200, "TPM": None, "Batch Queue Limit": None},
        "dall-e-2": {"RPM": "5 img/min", "RPD": None, "TPM": None, "Batch Queue Limit": None},
        "dall-e-3": {"RPM": "1 img/min", "RPD": None, "TPM": None, "Batch Queue Limit": None},
    },
    "tier1": {
        "gpt-4-turbo": {"RPM": 500, "RPD": None, "TPM": 300000, "Batch Queue Limit": 900000},
        "gpt-4": {"RPM": 500, "RPD": 10000, "TPM": 10000, "Batch Queue Limit": 100000},
        "gpt-3.5-turbo": {"RPM": 3500, "RPD": 10000, "TPM": 60000, "Batch Queue Limit": 200000},
        "text-embedding-3-large": {"RPM": 500, "RPD": 10000, "TPM": 1000000, "Batch Queue Limit": None},
        "whisper-1": {"RPM": 50, "RPD": None, "TPM": None, "Batch Queue Limit": None},
        "tts-1": {"RPM": 50, "RPD": None, "TPM": None, "Batch Queue Limit": None},
        "tts-1-hd": {"RPM": 3, "RPD": None, "TPM": None, "Batch Queue Limit": None},
        "dall-e-2": {"RPM": "5 img/min", "RPD": None, "TPM": None, "Batch Queue Limit": None},
        "dall-e-3": {"RPM": "5 img/min", "RPD": None, "TPM": None, "Batch Queue Limit": None},
    },
    "tier2": {
        "gpt-4-turbo": {"RPM": 5000, "TPM": 450000, "Batch Queue Limit": 1350000},
        "gpt-4": {"RPM": 5000, "TPM": 40000, "Batch Queue Limit": 200000},
        "gpt-3.5-turbo": {"RPM": 3500, "TPM": 80000, "Batch Queue Limit": 400000},
        "text-embedding-3-large": {"RPM": 500, "TPM": 1000000, "Batch Queue Limit": None},
        "whisper-1": {"RPM": "50", "TPM": None, "Batch Queue Limit": None},
        "tts-1": {"RPM": "50", "TPM": None, "Batch Queue Limit": None},
        "tts-1-hd": {"RPM": "5", "TPM": None, "Batch Queue Limit": None},
        "dall-e-2": {"RPM": "50 img/min", "TPM": None, "Batch Queue Limit": None},
        "dall-e-3": {"RPM": "7 img/min", "TPM": None, "Batch Queue Limit": None},
    },
    "tier3": {
        "gpt-4-turbo": {"RPM": 5000, "TPM": 600000, "Batch Queue Limit": 40000000},
        "gpt-4": {"RPM": 5000, "TPM": 80000, "Batch Queue Limit": 5000000},
        "gpt-3.5-turbo": {"RPM": 3500, "TPM": 160000, "Batch Queue Limit": 10000000},
        "text-embedding-3-large": {"RPM": 5000, "TPM": 5000000, "Batch Queue Limit": None},
        "whisper-1": {"RPM": 100, "TPM": None, "Batch Queue Limit": None},
        "tts-1": {"RPM": 100, "TPM": None, "Batch Queue Limit": None},
        "tts-1-hd": {"RPM": 7, "TPM": None, "Batch Queue Limit": None},
        "dall-e-2": {"RPM": "100 img/min", "TPM": None, "Batch Queue Limit": None},
        "dall-e-3": {"RPM": "7 img/min", "TPM": None, "Batch Queue Limit": None},
    },
    "tier4": {
        "gpt-4-turbo": {"RPM": 10000, "TPM": 800000, "Batch Queue Limit": 80000000},
        "gpt-4": {"RPM": 10000, "TPM": 300000, "Batch Queue Limit": 30000000},
        "gpt-3.5-turbo": {"RPM": 10000, "TPM": 1000000, "Batch Queue Limit": 100000000},
        "text-embedding-3-large": {"RPM": 10000, "TPM": 5000000, "Batch Queue Limit": None},
        "whisper-1": {"RPM": 100, "TPM": None, "Batch Queue Limit": None},
        "tts-1": {"RPM": 100, "TPM": None, "Batch Queue Limit": None},
        "tts-1-hd": {"RPM": 10, "TPM": None, "Batch Queue Limit": None},
        "dall-e-2": {"RPM": "100 img/min", "TPM": None, "Batch Queue Limit": None},
        "dall-e-3": {"RPM": "15 img/min", "TPM": None, "Batch Queue Limit": None},
    },
    "tier5": {
        "gpt-4-turbo": {"RPM": 10000, "TPM": 1500000, "Batch Queue Limit": 250000000},
        "gpt-4": {"RPM": 10000, "TPM": 300000, "Batch Queue Limit": 45000000},
        "gpt-3.5-turbo": {"RPM": 10000, "TPM": 2000000, "Batch Queue Limit": 300000000},
        "text-embedding-3-large": {"RPM": 10000, "TPM": 10000000, "Batch Queue Limit": None},
        "whisper-1": {"RPM": 500, "TPM": None, "Batch Queue Limit": None},
        "tts-1": {"RPM": 500, "TPM": None, "Batch Queue Limit": None},
        "tts-1-hd": {"RPM": 20, "TPM": None, "Batch Queue Limit": None},
        "dall-e-2": {"RPM": "500 img/min", "TPM": None, "Batch Queue Limit": None},
        "dall-e-3": {"RPM": "50 img/min", "TPM": None, "Batch Queue Limit": None},
    },
}


def num_tokens_consumed_by_chat_request(messages, max_tokens=15, n=1, functions="", **kwargs):
    # num_tokens = n * max_tokens
    # for message in messages:
    #     num_tokens += 4 # Every message follows <im_start>{role/name}\n{content}<im_end>\n
    #     for key, value in message.items():
    #         num_tokens += len(CL100K_ENCODER.encode(str(value)))

    #         if key == "name": # If there's a name, the role is omitted
    #             num_tokens -= 1

    # num_tokens += 2 # Every reply is primed with <im_start>assistant
    num_tokens = num_tokens_from_messages(messages)

    if functions:
        function_tokens = num_tokens_from_functions(functions)
        num_tokens += function_tokens

    return num_tokens


def num_tokens_from_messages(messages, model="gpt-4-0613"):
    """Return the number of tokens used by a list of messages."""
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        print("Warning: model not found. Using cl100k_base encoding.")
        encoding = tiktoken.get_encoding("cl100k_base")
    if model in {
        "gpt-3.5-turbo-0613",
        "gpt-3.5-turbo-16k-0613",
        "gpt-4-0314",
        "gpt-4-32k-0314",
        "gpt-4-0613",
        "gpt-4-32k-0613",
    }:
        tokens_per_message = 3
        tokens_per_name = 1
    elif model == "gpt-3.5-turbo-0301":
        tokens_per_message = 4  # every message follows <|start|>{role/name}\n{content}<|end|>\n
        tokens_per_name = -1  # if there's a name, the role is omitted
    elif "gpt-3.5-turbo" in model:
        print("Warning: gpt-3.5-turbo may update over time. Returning num tokens assuming gpt-3.5-turbo-0613.")
        return num_tokens_from_messages(messages, model="gpt-3.5-turbo-0613")
    elif "gpt-4" in model:
        print("Warning: gpt-4 may update over time. Returning num tokens assuming gpt-4-0613.")
        return num_tokens_from_messages(messages, model="gpt-4-0613")
    else:
        raise NotImplementedError(
            f"""num_tokens_from_messages() is not implemented for model {model}. See https://github.com/openai/openai-python/blob/main/chatml.md for information on how messages are converted to tokens."""
        )
    num_tokens = 0
    for message in messages:
        num_tokens += tokens_per_message
        for key, value in message.items():
            try:
                num_tokens += len(encoding.encode(value))
            except TypeError:
                num_tokens += len(encoding.encode(str(value)))
            if key == "name":
                num_tokens += tokens_per_name
    num_tokens += 3  # every reply is primed with <|start|>assistant<|message|>
    return num_tokens


def num_tokens_from_functions(tools, model="gpt-3.5-turbo-0613"):
    """Return the number of tokens used by a list of functions."""
    num_tokens = 0
    for tool in tools:
        function_tokens = len(CL100K_ENCODER.encode(tool["function"]["name"]))
        function_tokens += len(CL100K_ENCODER.encode(tool["function"]["description"]))

        if "parameters" in tool["function"]:
            parameters = tool["function"]["parameters"]
            if "properties" in parameters:
                for propertiesKey in parameters["properties"]:
                    function_tokens += len(CL100K_ENCODER.encode(propertiesKey))
                    v = parameters["properties"][propertiesKey]
                    for field in v:
                        if field == "type":
                            function_tokens += 2
                            function_tokens += len(CL100K_ENCODER.encode(v["type"]))
                        elif field == "description":
                            function_tokens += 2
                            function_tokens += len(CL100K_ENCODER.encode(v["description"]))
                        elif field == "enum":
                            function_tokens -= 3
                            for o in v["enum"]:
                                function_tokens += 3
                                function_tokens += len(CL100K_ENCODER.encode(o))
                        elif field == "items":
                            # function_tokens += 2
                            # function_tokens += 2
                            function_tokens += len(CL100K_ENCODER.encode(v["type"]))
                            if "properties" in v[field]:
                                NestedParameters = v[field]
                                for NestedpropertiesKey in NestedParameters["properties"]:
                                    function_tokens += len(CL100K_ENCODER.encode(NestedpropertiesKey))
                                    Nestedv = NestedParameters["properties"][NestedpropertiesKey]
                                    for Nestedfield in Nestedv:
                                        if Nestedfield == "type":
                                            # function_tokens += 2
                                            function_tokens += len(CL100K_ENCODER.encode(Nestedv["type"]))
                                        elif Nestedfield == "description":
                                            # function_tokens += 2
                                            function_tokens += len(CL100K_ENCODER.encode(Nestedv["description"]))
                                        elif Nestedfield == "enum":
                                            function_tokens -= 3
                                            for Nestedo in Nestedv["enum"]:
                                                # function_tokens += 3
                                                function_tokens += len(CL100K_ENCODER.encode(Nestedo))
                                        elif field == "items":
                                            # function_tokens += 2
                                            # function_tokens += 2
                                            function_tokens += len(CL100K_ENCODER.encode(Nestedv["type"]))

                                print("")
                        else:
                            print(f"Warning: not supported field {field} : {v[field]}")
                function_tokens += 11

        num_tokens += function_tokens

    num_tokens += 12
    return num_tokens
