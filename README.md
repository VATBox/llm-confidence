Explanation:
Get Completion: Sends a prompt to the OpenAI GPT model and retrieves the completion, including the log probabilities.
Logprobs Formatting: Formats the raw log probabilities into a structured format that can be processed.
Confidence Calculation: Aggregates the probabilities and returns confidence scores for key-value pairs in the model’s JSON response.
Customizing Nested Keys for Confidence Aggregation
In the example above, the nested keys dictionary (nested_keys_dct) allows you to define custom fields (like 'vat') and related sub-keys (e.g., 'vat_data', 'percent', etc.) to calculate an aggregated confidence score.

You can modify this to fit your use case by adding more nested keys based on the structure of your LLM outputs.

License
This package is licensed under the Apache License 2.0. See the LICENSE file for more details.

Contributing
Feel free to fork the repository, create new branches, and open PRs to contribute to the project. Ensure that new features or fixes come with adequate tests.

Usage
Here’s an example of how to use the llm-confidence package to calculate confidence scores based on log probabilities from OpenAI GPT models:

from openai import OpenAI
import os
from llm_confidence.logprobs_handler import LogprobsHandler

# Initialize the LogprobsHandler
logprobs_handler = LogprobsHandler()

def get_completion(
        messages: list[dict[str, str]],
        model: str = "gpt-4",
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

Example Breakdown
Get Completion: Sends a prompt to the OpenAI GPT model and retrieves the completion, including log probabilities.
Logprobs Formatting: Formats the raw log probabilities into a structured format that can be processed.
Confidence Calculation: Aggregates the probabilities and returns confidence scores for key-value pairs in the model's JSON response.
Customization
You can customize the nested_keys_dct parameter to aggregate confidence scores for your specific fields. For example:

nested_keys_dct={'address': ['street', 'city', 'state']}

This will compute a combined confidence score for all fields related to addresses.

License
This project is licensed under the Apache License 2.0 - see the LICENSE file for details.

Contributing
We welcome contributions! Here's how you can help:

Fork the project.
Create a branch for your feature or bug fix.
Open a pull request.
Make sure to include tests for any new features or bug fixes.

Feel free to use the package and improve upon it. If you encounter any issues, please open an issue in the repository.


### Key Sections:
- **Title & Description**: Provides a quick overview of what the package does.
- **Installation**: Simple command to install the package via `pip`.
- **Usage**: Includes a working example with code that shows how to use the package.
- **Customization**: A brief section explaining how users can modify the `nested_keys_dct` parameter.
- **License**: License details for the project.
- **Contributing**: A call for contributions with basic steps.

You can save this content as `README.md` in the root of your repository.

Let me know if you'd like any additional modifications!
