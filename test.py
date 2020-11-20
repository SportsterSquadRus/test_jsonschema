import os
import jsonschema
import json

events_dir = os.listdir(path="event")
schemas_dir = os.listdir(path="schema")

for schema in schemas_dir:
    with open('schema/{}'.format(schema)) as schema_file:
        current_schema = json.load(schema_file)

    v = jsonschema.Draft3Validator(current_schema)

    for event in events_dir:
        with open('event/{}'.format(event)) as event_file:
            result = json.load(event_file)

        for error in sorted(v.iter_errors(result), key=str):
            with open('readme.md', 'a', encoding='utf8') as readme:
                readme.write('{}\n\n'.format(error.message))
