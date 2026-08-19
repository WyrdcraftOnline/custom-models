# Creating a Custom Model for Wyrdcraft - For Dummies

This guide explains how to add a normal custom item model to the Wyrdcraft resource pack.

You do not need to be a programmer, but you do need to put files in the right folders and make the JSON point at the right paths.

The current season folder is:
```text
season_one
```

Treat that folder as the root of the actual resource pack assets.

> [!INFO]
> If `season.txt` changes in the future, use the folder named in `season.txt` instead of assuming `season_one`.

## What You Are Adding
Most custom models need three things:
```text
1. A model file
2. One or more texture files
3. A mapping from a CustomModelData number to your model
```

In this repository, those usually live here:
```text
season_one/assets/wyrd_model/models/item/
season_one/assets/wyrd_model/textures/item/
season_one/assets/minecraft/items/
```

The `wyrd_model` folder is Wyrdcraft's custom namespace. The `minecraft` folder is where Minecraft looks for vanilla item definitions, such as `carved_pumpkin`, `stick`, `spyglass`, or `elytra`.

> [!WARNING]
> Do not put custom Wyrdcraft item models directly under `season_one/assets/minecraft/models/item/` unless you are intentionally replacing or extending a vanilla Minecraft model. Normal custom models belong under `season_one/assets/wyrd_model/models/item/`.

## File Naming Rules
Minecraft resource packs are picky. Use boring names.

Use:
* Lowercase letters
* Numbers if needed
* Underscores

Do not use:
* Spaces
* Capital letters
* Hyphens
* Apostrophes
* Exclamation marks
* Parentheses
* Other special characters

> [!INFO]
> Good file names:
> ```text
> ancient_staff.json
> copper_mug.png
> steampunk_lantern.json
> magnifying_glass.json
> ```

> [!WARNING]
> Bad file names:
> ```text
> Ancient Staff.json
> copper-mug.png
> steampunk lantern!.json
> dadmann's Model.png
> ```

Use the same simple name everywhere. If your model is called `ancient_staff`, then your JSON and texture paths should also say `ancient_staff`.

> [!DANGER]
> File names and JSON paths must match exactly. `ancient_staff`, `Ancient_Staff`, and `ancient-staff` are three different names to Minecraft.

## Recommended Folder Pattern
Put your files under your username or creator name so they do not collide with someone else's files.

Example for a model named `ancient_staff` made by `exampleuser`:
```text
season_one/assets/wyrd_model/models/item/exampleuser/ancient_staff/ancient_staff.json
season_one/assets/wyrd_model/textures/item/exampleuser/ancient_staff/texture.png
```

If your model has multiple textures, keep them in the same texture folder:
```text
season_one/assets/wyrd_model/textures/item/exampleuser/ancient_staff/wood.png
season_one/assets/wyrd_model/textures/item/exampleuser/ancient_staff/gem.png
season_one/assets/wyrd_model/textures/item/exampleuser/ancient_staff/metal.png
```
## The Important Path Rule
JSON paths do not include `.json` or `.png`.

> [!WARNING]
> Including `.json` or `.png` inside a model or texture reference is one of the easiest ways to break a resource pack path.

This real file:
```text
season_one/assets/wyrd_model/textures/item/exampleuser/ancient_staff/texture.png
```

Is written in JSON like this:
```json
"wyrd_model:item/exampleuser/ancient_staff/texture"
```

This real file:
```text
season_one/assets/wyrd_model/models/item/exampleuser/ancient_staff/ancient_staff.json
```

Is written in JSON like this:
```json
"wyrd_model:item/exampleuser/ancient_staff/ancient_staff"
```

Why? The format is:
```text
namespace:path_inside_models_or_textures_without_file_extension
```

For this repo, the namespace for custom models is:
```text
wyrd_model
```

> [!INFO]
> `wyrd_model:item/exampleuser/ancient_staff/ancient_staff` points to a model file under `assets/wyrd_model/models/item/...`. `wyrd_model:item/exampleuser/ancient_staff/texture` points to a texture file under `assets/wyrd_model/textures/item/...`.

## Texture Files
Textures should be PNG files.

Put normal item model textures here:
```text
season_one/assets/wyrd_model/textures/item/
```

Example:
```text
season_one/assets/wyrd_model/textures/item/exampleuser/ancient_staff/texture.png
```

If you made the model in Blockbench, export the texture from Blockbench and keep the file names lowercase.

> [!WARNING]
> If Blockbench exports texture paths using a different namespace, an absolute computer path, or a file extension, update those paths before submitting.

The texture path in your model JSON must match the real texture file exactly, except:
* Remove `season_one/assets/`
* Remove `textures/`
* Remove `.png`
* Add the namespace before the colon

Example:
```json
"textures": {
  "0": "wyrd_model:item/exampleuser/ancient_staff/texture",
  "particle": "wyrd_model:item/exampleuser/ancient_staff/texture"
}
```

The `particle` texture is what Minecraft uses for small particles when the item is broken or displayed in some contexts. Usually, point it at your main texture.

> [!INFO]
> If your model uses multiple textures, each texture key, such as `"0"`, `"1"`, or `"particle"`, must point to an existing PNG file.

## Model JSON
Put normal item model JSON files here:
```text
season_one/assets/wyrd_model/models/item/
```

Example:
```text
season_one/assets/wyrd_model/models/item/exampleuser/ancient_staff/ancient_staff.json
```

A Blockbench model usually looks something like this:
```json
{
  "format_version": "1.21.11",
  "credit": "Made with Blockbench",
  "texture_size": [32, 32],
  "textures": {
    "0": "wyrd_model:item/exampleuser/ancient_staff/texture",
    "particle": "wyrd_model:item/exampleuser/ancient_staff/texture"
  },
  "elements": [
    {
      "from": [7, 0, 7],
      "to": [9, 16, 9],
      "faces": {
        "north": { "uv": [0, 0, 2, 16], "texture": "#0" },
        "east": { "uv": [0, 0, 2, 16], "texture": "#0" },
        "south": { "uv": [0, 0, 2, 16], "texture": "#0" },
        "west": { "uv": [0, 0, 2, 16], "texture": "#0" },
        "up": { "uv": [0, 0, 2, 2], "texture": "#0" },
        "down": { "uv": [0, 0, 2, 2], "texture": "#0" }
      }
    }
  ],
  "display": {
    "thirdperson_righthand": {
      "rotation": [0, 0, 0],
      "translation": [0, 2, 1],
      "scale": [1, 1, 1]
    },
    "firstperson_righthand": {
      "rotation": [0, 0, 0],
      "translation": [0, 2, 0],
      "scale": [1, 1, 1]
    },
    "gui": {
      "rotation": [30, 225, 0],
      "translation": [0, 0, 0],
      "scale": [1, 1, 1]
    }
  }
}
```

You normally do not need to write all of this by hand. Blockbench can export it. The main things to check are:
* The file is valid JSON.
* Every texture path starts with `wyrd_model:`.
* Every texture path points to a real PNG file.
* The model file is inside `season_one/assets/wyrd_model/models/item/`.
* The file name is lowercase and uses underscores.

> [!WARNING]
> If the model JSON is invalid, Minecraft may ignore the model or the whole item definition. Check commas, brackets, braces, and quote marks before opening a pull request.

## Simple Flat Item Model
If your custom item is just a flat 2D icon, the model JSON can be much shorter:
```json
{
  "parent": "minecraft:item/generated",
  "textures": {
    "layer0": "wyrd_model:item/exampleuser/ancient_coin/texture"
  }
}
```

Use this for simple item icons. Use a Blockbench-style model for 3D shapes.
## CustomModelData Number
Every custom model needs a unique `CustomModelData` number. Check the [`README`](../README.md) for your assigned number range. Only use numbers from your range.

Examples from this repo:
```text
SHO310: 001-099
LewisGamer327: 101-199
```

If your assigned range is `200-299`, your first model might use:
```text
200
```

> [!WARNING]
> Do not reuse someone else's number. Do not guess.

> [!DANGER]
> Reusing a `CustomModelData` number can make two models fight for the same item. One model may disappear, or someone else's existing model may be replaced.

## Base Item
Your model needs a normal Minecraft item to attach to. This is called the base item.

Examples:
```text
carved_pumpkin
stick
spyglass
elytra
```

The base item decides which Minecraft item the player holds or wears. The custom model only changes how that item looks when the right `CustomModelData` number is applied.

> [!INFO]
> Pick the base item based on how the item should behave in game. For example, use `carved_pumpkin` for head cosmetics, `spyglass` for spyglass behavior, and `elytra` for wearable wings.

## Mapping Your Number to Your Model
The mapping file goes in:
```text
season_one/assets/minecraft/items/
```

The file name must match the base item.

Examples:
```text
season_one/assets/minecraft/items/carved_pumpkin.json
season_one/assets/minecraft/items/spyglass.json
season_one/assets/minecraft/items/stick.json
```

If the base item file does not exist yet, create it.

> [!DANGER]
> If the base item file already exists, do not delete its existing entries. Those entries are probably other players' models.

### Simple Base Item Mapping
This is the basic structure for a normal item:
```json
{
  "model": {
    "type": "minecraft:range_dispatch",
    "property": "minecraft:custom_model_data",
    "fallback": {
      "type": "minecraft:model",
      "model": "minecraft:item/stick"
    },
    "entries": [
      {
        "threshold": 200,
        "model": {
          "type": "minecraft:model",
          "model": "wyrd_model:item/exampleuser/ancient_staff/ancient_staff"
        }
      }
    ]
  }
}
```

In that example:
* `stick.json` is the base item file.
* `minecraft:item/stick` is the normal fallback model.
* `200` is the custom model number.
* `wyrd_model:item/exampleuser/ancient_staff/ancient_staff` points to your model JSON.

> [!WARNING]
> Make sure the fallback model matches the base item file. A `stick.json` mapping should normally fall back to `minecraft:item/stick`, not a different item.

### Adding to an Existing Base Item
> [!WARNING]
> If the base item file already exists, do not replace the whole file unless you understand everything in it.

Instead, add a new entry inside the existing `entries` list:
```json
{
  "threshold": 201,
  "model": {
    "type": "minecraft:model",
    "model": "wyrd_model:item/exampleuser/copper_mug/copper_mug"
  }
}
```

Make sure entries are separated with commas:
```json
"entries": [
  {
    "threshold": 200,
    "model": {
      "type": "minecraft:model",
      "model": "wyrd_model:item/exampleuser/ancient_staff/ancient_staff"
    }
  },
  {
    "threshold": 201,
    "model": {
      "type": "minecraft:model",
      "model": "wyrd_model:item/exampleuser/copper_mug/copper_mug"
    }
  }
]
```

JSON does not allow a trailing comma after the last item.

> [!INFO]
> This is valid:
> ```json
> [
>   { "threshold": 200 },
>   { "threshold": 201 }
> ]
> ```

> [!WARNING]
> This is broken:
> ```json
> [
>   { "threshold": 200 },
>   { "threshold": 201 },
> ]
> ```

## Important Special Cases
Some items need extra structure.

> [!INFO]
> If your item is a normal handheld object, the simple base item mapping is usually enough. If it has special vanilla behavior, check whether it needs one of the patterns below.

### Spyglass
The spyglass can have one model when held normally and another model while the player is using it.

This repo's `spyglass.json` uses:
```text
on_false = normal held item
on_true = in-use spyglass view/animation model
```

If your model uses `spyglass`, check both parts of:
```text
season_one/assets/minecraft/items/spyglass.json
```

You may need two model files:
```text
season_one/assets/wyrd_model/models/item/exampleuser/my_spyglass/my_spyglass.json
season_one/assets/wyrd_model/models/item/exampleuser/my_spyglass_in_hand/my_spyglass_in_hand.json
```

> [!WARNING]
> If you only update one side of `spyglass.json`, the item may look correct in inventory but switch back to the vanilla spyglass while being used, or the other way around.

### Elytra
Elytra consist of 4 states:
```text
An item model
A broken item model
An equipment texture for wings
An equipment JSON file
```

Existing examples:
```text
season_one/assets/wyrd_model/models/item/sho/elytra/sho_elytra_1.json
season_one/assets/wyrd_model/models/item/sho/elytra/sho_elytra_1_broken.json
season_one/assets/wyrd_model/textures/entity/equipment/wings/sho_elytra_1.png
season_one/assets/wyrd_model/equipment/sho_elytra_1.json
season_one/assets/wyrd_model/items/sho_elytra_1.json
```

If you are adding elytra, copy the pattern of the existing elytra files and test it in game.

> [!DANGER]
> Elytra are more than a single item texture. Missing the equipment texture or equipment JSON can make the inventory item look correct while the worn wings are broken or invisible.

### Wearable Head Items
Models worn on the head often use `carved_pumpkin` as the base item.

Existing example:
```text
season_one/assets/minecraft/items/carved_pumpkin.json
season_one/assets/wyrd_model/models/item/sho/glasses/glasses_funny_disguise.json
```

This works well for hats, glasses, masks, and other cosmetic head items.

> [!WARNING]
> Head cosmetics should be tested while worn, not only in the inventory. A model can look fine in the GUI but be positioned badly on the player's head.

## Extra Item Definition Files
This repo also has files here:
```text
season_one/assets/wyrd_model/items/
```

These are item model definition files in the `wyrd_model` namespace. Existing examples include:
```text
season_one/assets/wyrd_model/items/glasses_funny_disguise.json
season_one/assets/wyrd_model/items/sho_elytra_1.json
season_one/assets/wyrd_model/items/invisible.json
```

For a basic CustomModelData model, the most important mapping is still the base item file under:
```text
season_one/assets/minecraft/items/
```

If you are copying an existing model that already has a matching file under `wyrd_model/items/`, keep that pattern. If you are adding a simple model and are unsure whether you need one, ask a pack maintainer before inventing a new structure.

> [!INFO]
> When in doubt, copy the closest existing model's structure and change only the names, paths, textures, and `CustomModelData` number needed for your model.

## Full Example
Here is a complete example for a new custom model:
```text
Creator: exampleuser
Model name: Ancient Staff
Safe file name: ancient_staff
Base item: stick
CustomModelData: 200
```

Files to add:
```text
season_one/assets/wyrd_model/models/item/exampleuser/ancient_staff/ancient_staff.json
season_one/assets/wyrd_model/textures/item/exampleuser/ancient_staff/texture.png
season_one/assets/minecraft/items/stick.json
```

Texture reference inside `ancient_staff.json`:
```json
"textures": {
  "0": "wyrd_model:item/exampleuser/ancient_staff/texture",
  "particle": "wyrd_model:item/exampleuser/ancient_staff/texture"
}
```

Model mapping inside `stick.json`:
```json
{
  "model": {
    "type": "minecraft:range_dispatch",
    "property": "minecraft:custom_model_data",
    "fallback": {
      "type": "minecraft:model",
      "model": "minecraft:item/stick"
    },
    "entries": [
      {
        "threshold": 200,
        "model": {
          "type": "minecraft:model",
          "model": "wyrd_model:item/exampleuser/ancient_staff/ancient_staff"
        }
      }
    ]
  }
}
```

README entry:
```markdown
* **exampleuser:** 200-299
  * `200`: Ancient Staff `(stick)`
```

In-game test command:
```mcfunction
/trigger CustomModelData set 200
```

> [!WARNING]
> The test command only changes the item you are holding if the server command/setup supports that base item. Make sure you are holding the same base item that you mapped in JSON.

## Common Mistakes
If the model shows as a missing black-and-purple texture, check:
* Is the texture file actually a `.png`?
* Does the model JSON texture path exactly match the texture file?
* Did you accidentally include `.png` in the JSON path?
* Did you use the wrong namespace?
* Did you use capital letters in a file name?

If the model does not appear at all, check:
* Did you use the correct `CustomModelData` number?
* Did you update the correct base item file?
* Is the base item in game the same item you mapped?
* Does your entry have the right `threshold`?
* Is the JSON valid?

If Minecraft ignores the file, check:
* Did you put it under `season_one/assets/`?
* Is the folder name `models`, `textures`, or `items` spelled correctly?
* Did you leave a trailing comma in JSON?
* Did you save the file with the correct extension?
## Testing
> [!INFO]
> Before opening a pull request, test the pack in Minecraft.

> [!DANGER]
> Do not submit an untested model if you can test it. Broken JSON or missing textures can affect more than just your item.

At minimum, confirm:
* The resource pack loads.
* Your base item still looks normal without CustomModelData.
* Your model appears with your CustomModelData number.
* Your texture appears correctly.
* The model looks right in first person, third person, inventory, and item frames if those views matter.
* You did not change or break someone else's model.

You can also run the release build locally:
```sh
make
```

That creates a release zip and can catch some obvious packaging problems. It does not replace testing in Minecraft.

> [!INFO]
> `make` is useful for checking that the pack can be packaged, but Minecraft is the real test for model position, texture paths, and item behavior.

## Pull Request Checklist
Before opening your pull request, make sure you have:
* [ ] Claimed or confirmed your assigned number range.
* [ ] Used a unique CustomModelData number from your range.
* [ ] Added your model JSON under `season_one/assets/wyrd_model/models/item/`.
* [ ] Added your PNG textures under `season_one/assets/wyrd_model/textures/item/`.
* [ ] Updated the correct base item JSON under `season_one/assets/minecraft/items/`.
* [ ] Used lowercase underscore file names.
* [ ] Checked that JSON paths do not include `.json` or `.png`.
* [ ] Tested the model in game if possible.
* [ ] Updated the **Custom Item Models** list in [`README.md`](../README.md).
* [ ] Opened your pull request using the pull request guide.

For pull request help, see the [Pull Request doc](pull_request_for_dummies.md).
