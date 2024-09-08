import uuid
import os


def import_used_uuids():
    with open("../../static/processed/v2/uuids.txt", "r") as uuid_file:
        line = uuid_file.read()
        uuids = line.split()

    return uuids


def write_used_uuid(generated_uuid):
    with open("../../static/processed/v2/uuids.txt", "a") as uuid_file:
        uuid_file.write(f"{generated_uuid},")


def generate_unique_id():
    uuid_path = "../../static/processed/v2/uuids.txt"
    if not os.path.exists(uuid_path):
        with open(uuid_path, "w") as uuid_file:
            pass

    generated_uuid = uuid.uuid4()
    uuids = import_used_uuids()

    while generated_uuid in uuids:
        generated_uuid = uuid.uuid4()

    write_used_uuid(generated_uuid)
    return generated_uuid
