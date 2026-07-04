# Wyrdcraft Custom Models

This repository contains the custom model resource pack for the Wyrdcraft SMP.

The pack allows approved custom models to be assigned to specific items or blocks using Minecraft’s `CustomModelData` system. On the server, players can apply a model by using the `/trigger` command with the correct custom model number.

```mcfunction
/trigger CustomModelData set 1
```

In this example, `1` is the `CustomModelData` value assigned to a specific custom model.

---

## How This Repo Works

Each custom model is assigned a unique number. To avoid conflicts, every contributor should claim a dedicated number range before adding models to the pack.

Please do not use numbers outside of your assigned range unless you have cleared it with the rest of the group.

---

## Adding Custom Models

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
- **username:** 000–099
- **username:** 100–199
```

Current assigned ranges:

* **(username):** (number range)

---

## Contained Models

The following custom models are currently included in the resource pack.

> [!IMPORTANT]
> Only add or use models that have been approved for use by their creators and for which Wyrdcraft has permission.

```markdown
- **username:** number range
  - `number`: Model Name `(base item)`
```

Current models:

* **(username):** (number range)

  * `(number)`: (model name) `(base item)`

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
