# Wyrdcraft Armor Stand Skin Assets

This document covers the resource-pack side of Wyrdcraft custom armor stand skins.

Armor stand skins require:

* This resource pack for the armor stand CEM model, skin textures, and name-based texture rules.
* A custom-named armor stand in game that matches one of the names configured in the resource pack.

## Creating Your Skin

Custom armor stand skins use a `64x256` texture layout that is mapped by the armor stand CEM model.

For instructions on creating the texture asset, use this video guide starting at the armor stand skin section:

[Armor stand skin asset video](https://youtu.be/1ZviOqhaI7A?t=90&si=1YPOBoQOlTcHr_Gz)

Use lowercase file names and keep the numbered armor stand texture naming pattern already used by the pack.

Please treat the current season folder as the root folder when creating your assets. 

For reference, the current season folder is `season_one`.

## Required Resource-Pack Files

At minimum, check these files and folders:

```text
season_one/assets/minecraft/optifine/cem/armor_stand.jem
season_one/assets/minecraft/optifine/random/entity/armorstand/
```

## Skin Texture

Add the finished `64x256` skin texture to:

```text
season_one/assets/minecraft/optifine/random/entity/armorstand/
```

Use the next available numbered texture name.

Example:

```text
season_one/assets/minecraft/optifine/random/entity/armorstand/armorstand4.png
```

Do not replace `armorstand.png` unless you are intentionally changing the default armor stand texture used by this setup.

## Skin Name Mapping

Update:

```text
season_one/assets/minecraft/optifine/random/entity/armorstand/armorstand.properties
```

Each custom skin needs a matching `skins.N` and `name.N` entry, where `N` matches the number in the texture file name.

Example:

```properties
skins.4=4
name.4=ExampleName
```

With this example, an armor stand named `ExampleName` will use `armorstand4.png`.

## Using the Skin In Game

Place an armor stand and name it exactly as configured in `armorstand.properties`.

Example:

```text
ExampleName
```

The name is case-sensitive, so use the same capitalization in game and in the properties file.

## Checklist

Before opening a resource-pack pull request for an armor stand skin, make sure you have:

* Created a `64x256` skin texture using the armor stand skin layout
* Added the texture to `season_one/assets/minecraft/optifine/random/entity/armorstand/`
* Used the next available `armorstandN.png` file name
* Added the matching `skins.N` and `name.N` entries to `armorstand.properties`
* Tested the named armor stand in game if possible
* Updated the **Custom Armor Stand Skins** list in `README.md`
