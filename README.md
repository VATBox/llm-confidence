
# llm-confidence

**llm-confidence** is a Python package designed to extract and calculate confidence scores from outputs of large language models (LLMs), specifically focusing on log probabilities. The package helps you work with model responses, particularly when working with structured data such as JSON outputs.

## Features

- Extract token-level log probabilities.
- Aggregate probabilities to calculate confidence scores for key-value pairs.
- Handle nested keys to compute confidence scores for related fields.
- Simple API for processing log probabilities from OpenAI GPT models.

## Installation

You can install the package using `pip`:

```bash
pip install llm-confidence
```

## Usage

Here’s an example of how to use the `llm-confidence` package to calculate confidence scores based on log probabilities from OpenAI GPT models:

```python
from openai import OpenAI
import os
from llm_confidence.logprobs_handler import LogprobsHandler

# Initialize the LogprobsHandler
logprobs_handler = LogprobsHandler()

def get_completion(
        messages: list[dict[str, str]],
        model: str = "gpt-4o",
        max_tokens=500,
        temperature=0,
        stop=None,
        seed=42,
        response_format=None,
        logprobs=None,
        top_logprobs=None,
):
    params = {
        "model": model,
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "stop": stop,
        "seed": seed,
        "logprobs": logprobs,
        "top_logprobs": top_logprobs,
    }
    if response_format:
        params["response_format"] = response_format

    completion = client.chat.completions.create(**params)
    return completion

# Set up your OpenAI client with your API key
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "<your OpenAI API key if not set as env var>"))

# Define a prompt for completion
response_raw = get_completion(
    [{'role': 'user', 'content': 'Tell me the name of a city and a few streets in this city, and return the response in JSON format.'}],
    logprobs=True,
    response_format={'type': 'json_object'}
)

# Print the output
print(response_raw.choices[0].message.content)

# Extract the log probabilities from the response
response_logprobs = response_raw.choices[0].logprobs.content if hasattr(response_raw.choices[0], 'logprobs') else []

# Format the logprobs
logprobs_formatted = logprobs_handler.format_logprobs(response_logprobs)

# Process the log probabilities to get confidence scores
confidence = logprobs_handler.process_logprobs(
    logprobs_formatted, 
    nested_keys_dct={'vat': ['vat_data', 'percent', 'vat_amount', 'exclude_vat_amount']}
)

# Print the confidence scores
print(confidence)
```

### Example Breakdown
1. **Get Completion**: Sends a prompt to the OpenAI GPT model and retrieves the completion, including log probabilities.
2. **Logprobs Formatting**: Formats the raw log probabilities into a structured format that can be processed.
3. **Confidence Calculation**: Aggregates the probabilities and returns confidence scores for key-value pairs in the model's JSON response.

### Customization

You can customize the `nested_keys_dct` parameter to aggregate confidence scores for your specific fields. For example:

```python
nested_keys_dct={'address': ['street', 'city', 'state']}
```

This will compute a combined confidence score for all fields related to addresses.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Contributing

We welcome contributions! Here's how you can help:

1. Fork the project.
2. Create a branch for your feature or bug fix.
3. Open a pull request.

Make sure to include tests for any new features or bug fixes.

---

Feel free to use the package and improve upon it. If you encounter any issues, please open an issue in the repository.
