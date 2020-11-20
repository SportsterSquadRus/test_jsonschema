import os
import jsonschema
import json

events_dir = os.listdir(path="event")
schemas_dir = os.listdir(path="schema")

with open('readme.md', 'w', encoding='utf8') as readme:
    readme.write(
        'test.py is the main script file. It will work fine after jsonschema module installation.\n\nResults:\n\n')

for schema in schemas_dir:
    with open('schema/{}'.format(schema)) as schema_file:
        current_schema = json.load(schema_file)

    v = jsonschema.Draft3Validator(current_schema)

    for event in events_dir:
        with open('event/{}'.format(event)) as event_file:
            result = json.load(event_file)

        for error in sorted(v.iter_errors(result), key=str):
            with open('readme.md', 'a', encoding='utf8') as readme:
                readme.write('Schema: {}\nEvent: {}\nError: {}\n\n'.format(
                    schema, event, error.message))
