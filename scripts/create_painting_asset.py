#!/usr/bin/env python3
import json
import re
import shutil
import sys
from pathlib import Path


NAMESPACE = "wyrd_painting"
VALID_ID = re.compile(r"^[a-z0-9_]+$")
SUPPORTED_TEXTURE_EXTENSIONS = {".png"}


def prompt(label, validator=None, default=None):
    while True:
        suffix = f" [{default}]" if default else ""
        value = input(f"{label}{suffix}: ").strip()
        if not value and default is not None:
            value = default
        if not value:
            print("Value is required.")
            continue
        if validator:
            error = validator(value)
            if error:
                print(error)
                continue
        return value


def resolve_input_path(value):
    path = Path(value).expanduser()
    if not path.is_absolute():
        path = Path.cwd() / path
    return path


def validate_id(value):
    if ":" in value:
        return "Enter only the ID, without the namespace. Example: dadmannwalking01"
    if not VALID_ID.match(value):
        return "Use only lowercase letters, numbers, and underscores."
    return None


def validate_image(value):
    path = resolve_input_path(value)
    if not path.exists():
        return "Image file does not exist."
    if not path.is_file():
        return "Image path must point to a file."
    if path.suffix.lower() not in SUPPORTED_TEXTURE_EXTENSIONS:
        return "Minecraft resource-pack textures should be PNG files."
    return None


def choose_item_icon(item_texture_dir):
    icons = sorted(path for path in item_texture_dir.glob("*.png") if path.is_file())
    if not icons:
        print(f"No item icons found in {item_texture_dir}", file=sys.stderr)
        return None

    print("\nChoose an existing item icon:")
    for index, icon in enumerate(icons, start=1):
        print(f"{index}. {icon.stem}")

    while True:
        value = input("Item icon number or ID: ").strip()
        if not value:
            print("Value is required.")
            continue

        if value.isdigit():
            index = int(value)
            if 1 <= index <= len(icons):
                return icons[index - 1]
            print(f"Enter a number from 1 to {len(icons)}.")
            continue

        if validate_id(value):
            print(validate_id(value))
            continue

        for icon in icons:
            if icon.stem == value:
                return icon

        print("No matching item icon exists.")


def confirm_overwrite(paths):
    existing = [path for path in paths if path.exists()]
    if not existing:
        return True

    print("\nThe following files already exist:")
    for path in existing:
        print(f"- {path}")

    try:
        answer = input("Overwrite them? [y/N]: ").strip().lower()
    except EOFError:
        return False
    return answer in {"y", "yes"}


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def update_painting_item_mapping(path, namespaced_asset_id, namespaced_model_id):
    data = load_json(path)
    cases = data["model"]["cases"]

    new_case = {
        "when": namespaced_asset_id,
        "model": {
            "type": "model",
            "model": namespaced_model_id,
        },
    }

    for index, case in enumerate(cases):
        if case.get("when") == namespaced_asset_id:
            cases[index] = new_case
            write_json(path, data)
            return "updated"

    cases.append(new_case)
    write_json(path, data)
    return "added"


def main():
    repo_root = Path(__file__).resolve().parents[1]
    season_file = repo_root / "season.txt"

    if not season_file.exists():
        print("season.txt does not exist.", file=sys.stderr)
        return 1

    season = season_file.read_text(encoding="utf-8").strip()
    if not season:
        print("season.txt is empty.", file=sys.stderr)
        return 1

    season_dir = repo_root / season
    if not season_dir.exists():
        print(f"Season directory does not exist: {season_dir}", file=sys.stderr)
        return 1

    item_texture_dir = season_dir / "assets" / NAMESPACE / "textures" / "item"

    print("Create a Wyrdcraft custom painting resource-pack entry\n")
    painting_image = resolve_input_path(prompt("Painting image path", validate_image))
    asset_id = prompt("Datapack asset ID", validate_id)
    print("This ID must exactly match the custom painting datapack asset ID.")
    item_icon = choose_item_icon(item_texture_dir)
    if item_icon is None:
        return 1
    item_id = item_icon.stem

    namespaced_asset_id = f"{NAMESPACE}:{asset_id}"
    namespaced_model_id = f"{NAMESPACE}:item/{item_id}"

    painting_texture_path = (
        season_dir / "assets" / NAMESPACE / "textures" / "painting" / f"{asset_id}.png"
    )
    item_model_path = season_dir / "assets" / NAMESPACE / "models" / "item" / f"{item_id}.json"
    painting_item_path = season_dir / "assets" / "minecraft" / "items" / "painting.json"

    write_paths = [painting_texture_path]
    if not confirm_overwrite(write_paths):
        print("No files were changed.")
        return 1

    painting_texture_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(painting_image, painting_texture_path)

    item_model_created = False
    if not item_model_path.exists():
        item_model = {
            "parent": "minecraft:item/generated",
            "textures": {
                "layer0": f"{NAMESPACE}:item/{item_id}",
            },
        }
        write_json(item_model_path, item_model)
        item_model_created = True

    mapping_result = update_painting_item_mapping(
        painting_item_path,
        namespaced_asset_id,
        namespaced_model_id,
    )

    print("\nCreated resource-pack files:")
    print(f"- {painting_texture_path.relative_to(repo_root)}")
    print(f"- selected item icon: {item_icon.relative_to(repo_root)}")
    model_status = "created" if item_model_created else "reused"
    print(f"- {item_model_path.relative_to(repo_root)} ({model_status})")
    print(f"- {painting_item_path.relative_to(repo_root)} ({mapping_result} mapping)")

    print("\nDatapack follow-up:")
    print(f"- Confirm the datapack has a painting variant for {namespaced_asset_id}.")
    print("- See https://github.com/WyrdcraftOnline/wyrd-paintings")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
