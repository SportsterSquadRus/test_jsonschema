import os
import jsonschema
import json

events_dir = os.listdir(path="event")
schemas_dir = os.listdir(path="schema")

for schema in schemas_dir:
    with open('schema/{}'.format(schema)) as schema_file:
        current_schema = json.load(schema_file)

    for event in events_dir:
        with open('event/{}'.format(event)) as event_file:
            result = json.load(event_file)
            try:
                jsonschema.validate(result, current_schema)
                with open('readme.md', 'a', encoding='utf8') as readme:
                    readme.write(
                        'File {} matches the schema {}\n\n'.format(event, schema))
            except jsonschema.exceptions.ValidationError as ve:
                with open('readme.md', 'a', encoding='utf8') as readme:
                    readme.write('File {} does not match the schema {}. Error: {}\n\n'.format(
                        event, schemas_dir[0], str(ve)[:str(ve).find(':')]))
