"""Simple codex generator / enhancer script.

Usage:
  1. Maintain a YAML/JSON input file describing rings or other items.
  2. Run this script to render the full codex JSON (printed or saved).
  3. Optionally you can pipe the output through an LLM prompt to expand/validate.

The script is deliberately minimal so you can adapt it or replace it with
an LLM-based generator later.
"""

import argparse
import json
import yaml
import sys


def load_input(path):
    with open(path, 'r') as f:
        if path.lower().endswith(('.yaml', '.yml')):
            return yaml.safe_load(f)
        else:
            return json.load(f)


def main():
    parser = argparse.ArgumentParser(description="Generate or enhance a codex file")
    parser.add_argument('input', help="YAML/JSON file with codex fragments")
    parser.add_argument('-o', '--output', help="where to write the generated codex (json)")
    args = parser.parse_args()

    data = load_input(args.input)

    # if the input already has a "codex" root, just print it
    codex = data.get('codex', data)

    # ensure output is pretty-printed JSON
    json_str = json.dumps(codex, indent=2, ensure_ascii=False)
    if args.output:
        with open(args.output, 'w') as f:
            f.write(json_str)
        print(f"Written generated codex to {args.output}")
    else:
        sys.stdout.write(json_str)

# ------------------------------------------------------------------
# Optional: feed the current codex to an LLM to "enhance" it.
#
# This is not part of the basic generator, but you can use the
# produced JSON string as the input to a free model such as GPT-3.5
# or GPT-J.  For example, using the OpenAI python client (requires
# an API key but the free tier should suffice for light usage):
#
#   import openai
#   prompt = (
#       "Here is my existing codex data:\n" + json_str +
#       "\nPlease add a fourth ring called 'Echo of Chaos' with three
#       components and an unexpected twist.  Output in JSON."
#   )
#   resp = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[
#       {"role": "user", "content": prompt}
#   ])
#   print(resp.choices[0].message.content)
#
# You can similarly use local transformers models with
# "transformers" or "llama_cpp" libraries; just load the model and
# call `model.generate()` with the appropriate prompt.
#
# The idea is to use the generator as a pre/post-processing step: you
# maintain a clean YAML, generate JSON, ask the LLM to expand it, then
# merge the result back into your source.
# ------------------------------------------------------------------


if __name__ == '__main__':
    main()
