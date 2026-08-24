# Wyrdcraft Custom Models

This repository contains the custom assets resource pack for the Wyrdcraft SMP.

Want to contribute but don't know how? Check out the [docs overview](docs/overview.md), the [Creating a Model for Dummies Guide](docs/custom_models_for_dummies.md), and the [Pull Requests for Dummies Guide](docs/pull_request_for_dummies.md).

## Custom Models
The pack allows approved custom models to be assigned to specific items or blocks using Minecraft’s `CustomModelData` system. On the server, players can apply a model by using the `/trigger` command with the correct custom model number.

```mcfunction
/trigger CustomModelData set 1
```

In this example, `1` is the `CustomModelData` value assigned to a specific custom model.

---

## Custom Paintings
This resource pack also contains the client-side assets for Wyrdcraft custom paintings, including painting textures, item icons, item models, and language entries.

Custom paintings require both this resource pack and the matching custom paintings datapack. The datapack defines the painting variants, recipes, and server-side behavior that make the paintings available in game.

For resource-pack asset instructions, see [Custom Painting Assets](docs/custom_paintings.md).

Datapack repo: [Wyrdcraft Custom Paintings](https://github.com/WyrdcraftOnline/wyrd-paintings)

---

## Skins on Armor Stands
This resource pack also contains the client-side assets for displaying custom Minecraft skins on armor stands, including the armor stand CEM model, skin textures, and name-based texture rules.

Armor stand skins are handled directly in this resource pack. For asset instructions, see [Armor Stand Skin Assets](docs/armor_stands.md).

---

## How This Repo Works

Each custom model is assigned a unique number. To avoid conflicts, every contributor should claim a dedicated number range before adding models to the pack.

Please do not use numbers outside of your assigned range unless you have cleared it with the rest of the group.

---

## Adding Custom Models

For a beginner-friendly walkthrough of model JSON, textures, file structure, file names, and `CustomModelData` mappings, see [Creating a Custom Model for Wyrdcraft - For Dummies](docs/custom_models_for_dummies.md).

Before submitting a model, please make sure it has been tested locally and follows the existing pack structure.

### 1. Claim a Number Range

If you do not already have an assigned range, add your name to the **Assigned Number Ranges** section using the next available 100-number range.

Example:

```markdown
- **dadmannwalking:** 100–199
```

Use only numbers from your assigned range for your models.

If you run out of numbers, you may claim another available range.

---

### 2. Add Your Model Files

Add your custom model, textures, and any required JSON files to the appropriate folders in the resource pack.

Make sure your file paths match Minecraft’s expected structure and that your model works in-game before opening a pull request.

---

### 3. Follow Naming Rules

Model and texture file names should use:

* Lowercase letters
* Underscores
* No spaces
* No special characters

Good examples:

```text
ancient_staff
copper_mug
wyrdcraft_banner
```

Avoid names like:

```text
Ancient Staff
copper-mug
WyrdcraftBanner!
```

Minecraft can be picky about file names, so keeping everything lowercase and simple helps prevent resource pack issues.

---

### 4. Document Your Model

After adding your model, update the **Contained Models** section with your new entry.

Please include:

* The model number
* The model name
* The base item or block being used

Example:

```markdown
- **dadmannwalking:** 100–199
  - `100`: Ancient Staff `(carrot_on_a_stick)`
  - `101`: Copper Mug `(stick)`
```

---

### 5. Submit a Pull Request

When your model is ready:

1. Commit your changes to a new branch.
2. Open a pull request into the main branch.
3. Wait for another collaborator to review your changes.
4. Once approved, your pull request can be merged.

All changes should be reviewed before being merged into the main branch.

---

## Assigned Number Ranges

Each contributor should claim a unique 100-number range for their custom models.

If your name is not listed, add yourself using the next available range.

```markdown
- **username:** 001–099
- **username:** 100–199
```

Current assigned ranges:

* **SHO310:** 001–099
* **Lewisgamer327:** 101–199
* **ThatOneGuyJames:** 200–299
---

## Contained Assets

The following custom models are currently included in the resource pack.

> [!IMPORTANT]
> Only add or use models that have been approved for use by their creators and for which Wyrdcraft has permission.

```markdown
- **username:** number range
  - `number`: Model Name `(base item)`
```

### Custom Item Models:

* **SHO310:** 1-100
  *  `1`: Glasses Funny Disguise `(carved_pumpkin)`
  *  `2`: Elytra 1 `(Elytra)`

* **LewisGamer327:** 101-200
  *  `101`: Magnifying Glass `(spyglass)`

* **LewisGamer327:** 200-299
  *  `200`: Sun Glasses `(carved pumpkin)`
  *  `201`: Sun Glasses Two Bits `(carved pumpkin)`
  *  `202`: Sun Glasses Dadmann `(carved pumpkin)`
  *  `203`: Brown Cowboy Hat `(carved pumpkin)`
  *  `204`: Bright Brown Cowboy Hat `(carved pumpkin)`
  *  `205`: Black Cowboy Hat `(carved pumpkin)`
  *  `206`: Edible Fire `(Golden Carrot)`
  *  `207`: Edible Redstone `(Golden Carrot)`

### Custom Paintings

The following custom paintings are currently included in the resource pack.

* `wyrd_painting:dadmannwalking01`: "A Fresh Start" by dadmannwalking

### Custom Armor Stand Skins

The following armor stand skins are currently included in the resource pack.

* `Thatoneguyjames`: ThatOneGuyJames
* `Dadmann`: dadmannwalking 
* `alex`: official Minecraft skin
* `ari`: official Minecraft skin
* `efe`: official Minecraft skin
* `kai`: official Minecraft skin
* `makena`: official Minecraft skin
* `noor`: official Minecraft skin
* `zuri`: official Minecraft skin
* `sunny`: official Minecraft skin

---

## Creating a Release

Releases are handled automatically through continuous integration.

Once a pull request is approved and merged into the main branch, the release workflow will automatically create an updated version of the resource pack on the `release` branch.

No manual release build is required.

---

## Updating the Server

After your pull request has been merged, the server still needs to be updated so it knows which key to use to decrypt the latest pack.

Please contact an admin and ask them to run the following command from the server console:

```mcfunction
/fetchHash
```

Once this has been completed, the updated resource pack should be available to players the next time they log into the server.

---

## Quick Checklist

Before opening a pull request, make sure you have:

* Claimed a number range
* Used a number from your assigned range
* Added your model files in the correct location
* Followed the naming rules
* Tested the model in-game
* Updated the **Contained Models** section
* Opened a pull request for review

---

## Questions or Issues

If you are unsure where something should go, which number to use, or whether a model is ready to submit, ask in the Wyrdcraft Discord before opening a pull request.
