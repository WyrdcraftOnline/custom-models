# Creating a Pull Request for Wyrdcraft — For Dummies

So, you've made a custom model for Wyrdcraft and need to get it into the resource pack.

Don't panic.

You **do not need to be a programmer**, and you don't need to understand all the weird Git terminology. This guide will walk you through the process using **GitHub Desktop**, step by step.

We'll be working with the Wyrdcraft Custom Models repository:
[**WyrdcraftOnline/custom-models**](https://github.com/WyrdcraftOnline/custom-models)

---
# First: What Even Is a Pull Request?

Think of the repository as the **official copy** of the Wyrdcraft resource pack.

Instead of editing that official copy directly, you:
1. Make your own temporary copy of the work called a **branch**.
2. Add your models to that branch.
3. Save your changes with a **commit**.
4. Upload your branch to GitHub with a **push**.
5. Ask Wyrdcraft to add your changes to the official version with a **Pull Request**, usually shortened to **PR**.

In other words:
> [!NOTE]
> **Branch → Make Changes → Commit → Push → Pull Request → Review → Merge**

Once the PR is approved and merged, your changes become part of the main Wyrdcraft resource pack.

---
# Before You Start
You'll need:
* [ ] A GitHub account
* [ ] [GitHub Desktop](https://desktop.github.com/download/) installed
* [ ] Access to the [`WyrdcraftOnline/custom-models`](https://github.com/WyrdcraftOnline/custom-models) repository
* [ ] Your custom model files
* [ ] An assigned CustomModelData number range
* [ ] A model that you've tested in Minecraft

The repository requires contributors to use their assigned number range and asks that models be tested before a Pull Request is opened.

---
# Part 1 — Download the Repository
You only have to do this the **first time** you work with the repository.
## Step 1: Open GitHub Desktop
Open **GitHub Desktop**.

> [!NOTE]
> If this is your first time using it, sign in using your GitHub account.

---
## Step 2: Clone the Wyrdcraft Repository

1. In GitHub Desktop: **File → Clone Repository**
2. Select `WyrdcraftOnline/custom-models`. GitHub Desktop will ask where you want to save the repository on your computer. The default location is usually fine.
3. Click **Clone**. GitHub Desktop will download the entire resource pack onto your computer.
### Congratulations.
You have successfully done a Git Thing™.

---
# Part 2 — Make Sure You Have the Latest Version

Before adding anything, make sure your copy of the resource pack is up to date.

> [!IMPORTANT] 
> Do this every time before starting new work.
> It helps prevent your changes from colliding with someone else's.

1. At the top of GitHub Desktop, make sure your branch says: `main`
2. Then click: **Fetch origin**. If GitHub Desktop changes the button to **Pull origin** click that too.

This downloads any changes that other Wyrdcraft members have made since the last time you updated your copy.

---
# Part 3 — Create Your Branch

> [!IMPORTANT]
> **DO NOT make your changes directly on `main`.**
The Wyrdcraft repository specifically asks contributors to commit their work to a new branch before opening a Pull Request.

1. At the top of GitHub Desktop, click **Current Branch**
2. Then click **New Branch**
3. Give your branch a short name describing what you're adding

> [!NOTE]
Try to use:
> * Lowercase letters
> * Hyphens instead of spaces
> * A short description of what you're changing
> For example:
`sho/new-hat-model`
> 
> or:
> `lewis/magnifying-glass`
> 
> or:
> `dadmann/steampunk-lantern`

4. Then click **Create Branch**

GitHub Desktop should now show your new branch instead of `main`.

---
# Part 4 — Add Your Custom Model
Now you can edit the resource pack like any other folder on your computer.

1. In GitHub Desktop, click: **Repository → Show in Finder**. On Windows: **Repository → Show in Explorer**. This opens the actual resource-pack folder.
2. Add your model files, textures, and JSON files to the appropriate locations.

> [!IMPORTANT] 
> Please follow the existing folder structure whenever possible.
> 
> The current Wyrdcraft pack stores Season One assets under:
> `season_one/assets/`

---
# Part 5 — Follow the File Naming Rules

Model and texture file names should contain:
* Lowercase letters
* Numbers if needed
* Underscores

Avoid:
* Spaces
* Capital letters
* Special characters

> [!NOTE] 
> Good file names:
> `steampunk_lantern.json`
> `copper_mug.png`
> `ancient_staff.json`

> [!NOTE] 
> Bad file names:
> `Steampunk Lantern.json`
> `Copper-Mug.png`
> `Ancient Staff!.json`

Minecraft is particularly picky about resource locations, so boring filenames are good filenames.

The repository specifically requires lowercase, underscore-separated names without spaces or special characters.

---
# Part 6 — Use Your Assigned Number
Every Wyrdcraft member gets their own range of CustomModelData numbers.

For example, the repository currently lists ranges such as:
`SHO310: 001–099`
`LewisGamer327: 101–199`

Your model needs to use a number from **your** range.

> [!IMPORTANT] 
> Do not randomly pick a number.
> If you're not sure which range belongs to you, check the **Assigned Number Ranges** section of the repository's [`README.md`](../README.md).
> 
> If you don't have a range yet, claim the next available range or ask in the Wyrdcraft Discord.

---
# Part 7 — Update the README
Don't forget this part!
1. Open [`README.md`](../README.md)
2. Find the **Contained Models** section
3. Add your new model underneath your name.

The format should look something like:

```markdown
- SHO310: 1-100
  - `1`: Glasses Funny Disguise `(carved_pumpkin)`
  - `2`: Steampunk Goggles `(carved_pumpkin)`
```

The important pieces are:
- `CustomModelData number`
- `Model Name`
- `(base Minecraft item)`

For example:
```markdown
- YourUsername: 200-299
  - `200`: Steampunk Lantern `(stick)`
```

This lets everyone else know which numbers are already being used. 

The repository asks that every submitted model be documented this way.

---
# Part 8 — Test Your Model
Before submitting your PR, test the resource pack in Minecraft.

Make sure:
* [ ] The resource pack loads
* [ ] Your model appears
* [ ] The texture appears correctly
* [ ] The correct CustomModelData number activates it
* [ ] You haven't accidentally replaced someone else's model
* [ ] Minecraft doesn't complain about broken JSON or missing textures

For example, if your model uses CustomModelData `200`, you would test it using the appropriate Wyrdcraft custom-model command, such as:

```mcfunction
/trigger CustomModelData set 200
```

Do **not** submit something you've never tested.

---
# Part 9 — Commit Your Changes
1. Go back to GitHub Desktop.
2. On the left side of the window, you'll see a list of everything you've changed.
3. Take a second to look through it.
4. **Make sure you recognize all of the files.**
	1. If GitHub Desktop says you modified 4 files and you expected to modify 4 files, great. If GitHub Desktop says you modified 327 files, **something has probably gone horribly wrong.**
	2. Ask someone before continuing.
5. At the bottom-left of GitHub Desktop you'll see **Summary (required)**. This is your commit message. Write a short description of what you added. You generally don't need anything in the larger Description box. See **Commit messages** note below.

> [!NOTE] 
> Simple is just as good as complex. For example:
> `Add steampunk lantern model`
> 
> or:
> `Add custom goggles`
> 
> or:
> `Add SHO310 model 27`

6. Then click **Commit to YOUR-BRANCH-NAME**. For example: **Commit to dadmann/steampunk-lantern**

---
# Part 10 — Push Your Branch to GitHub
Your changes are currently only saved on **your computer**. Now we need to send them to GitHub.
1. At the top of GitHub Desktop, click **Publish branch**. Sometimes this may instead say **Push origin**. Click it.

Your branch now exists on GitHub.

> [!IMPORTANT] 
> Another Git Thing™ accomplished.

---
# Part 11 — Create the Pull Request
1. After publishing your branch, GitHub Desktop will usually display a button that says **Create Pull Request**. Click it.
2. GitHub Desktop will open GitHub in your browser. You should see something similar to **base: main ← compare: your-branch-name**

> [!IMPORTANT]
> The **base** should be:
> `main`
> 
> The **compare** branch should be the branch you just created.
> You are asking GitHub:
> 
> "Please take the changes from my branch and add them to `main`."

---
# Part 12 — Give Your PR a Name
Give your Pull Request a short, useful title.

> [!NOTE] 
> Good PR names
> - `Add Steampunk Lantern custom model`
> - `Add SHO310 models 27–30`
> - `Add LewisGamer327 Magnifying Glass update`

> [!NOTE] 
> Not so good PR names
> - `stuff`
> - `changes`
> - `please merge`
> - `idk github told me to type something here`

---
# Part 13 — Describe What You Changed
In the description, give whoever reviews the PR a quick explanation.

For example:
```markdown
## Changes

- Added Steampunk Lantern custom model
- Added lantern texture
- Added CustomModelData 200
- Updated README

## Testing

Tested in-game and confirmed the model and texture display correctly.
```

It doesn't need to be an essay.

The goal is just to make it easy for the reviewer to understand what you've changed.

---

# Part 14 — Create the Pull Request
1. Click **Create Pull Request**
2. And that's it.

> [!IMPORTANT] 
> Seriously.
> You're done.
> You have successfully created a Pull Request.

---
# What Happens Now?
Another Wyrdcraft collaborator will review your changes. They might:
1. **Approve it**. Everything looks good.
2. **Leave a comment**. They have a question.
3. **Request changes**. Something needs to be fixed before the model is added.

Don't panic if someone requests changes.

That's literally what Pull Requests are for.

The Wyrdcraft repository requires changes to be reviewed before they're merged into `main`.

---
# "Someone Asked Me to Change Something. Now What?"
You **do not need to create another Pull Request.**
1. Go back to GitHub Desktop.
2. Make sure you're still on the same branch you used for the PR. For example: `dadmann/steampunk-lantern`
3. Make the requested changes.
4. Check the changed files in GitHub Desktop.
5. Write another commit message.
6. Click **Commit**.
7. Click **Push origin**.

That's it. GitHub automatically adds the new commit to your existing Pull Request.

---
# After Your Pull Request Is Approved
Once everything looks good, the PR can be merged into `main`.

The Wyrdcraft repository automatically handles creation of the updated resource-pack release after approved changes are merged, so contributors do **not** need to manually build a release.

---
# Starting Your Next Model
When you're ready to work on something else:
1. Switch back to `main`. In GitHub Desktop, **Current Branch → main**
2. Update it. Click **Fetch origin** and, if shown, **Pull origin**
3. Create another new branch
4. Start working

Do **not** keep reusing your old branch for unrelated models.

New change = new branch = new Pull Request.

---
# The Entire Process in 30 Seconds
Every time you want to submit something:
* [ ] Switch to `main`
* [ ] Fetch/Pull the latest changes
* [ ] Create a new branch
* [ ] Add your files
* [ ] Use a number from your assigned range
* [ ] Follow the file naming rules
* [ ] Update [`README.md`](../README.md)
* [ ] Test the model in Minecraft
* [ ] Review the files GitHub says you changed
* [ ] Commit your changes
* [ ] Push/Publish your branch
* [ ] Create a Pull Request into `main`
* [ ] Wait for review
* [ ] Make fixes on the same branch if requested
* [ ] Celebrate because you just used Git

---
# Git Vocabulary for Normal Humans
**Repository / Repo**: The project folder GitHub keeps track of.

For us:
`WyrdcraftOnline/custom-models`

---

**main**: The official/current version of the project.

Try not to directly mess with it.

---

**Branch**: Your temporary workspace.

You make changes here without changing the official version.

Example:
`dadmann/steampunk-lantern`

---

**Commit**: A saved checkpoint containing your changes.

Example:
`Add steampunk lantern model`

---

**Push**: Uploads your commits from your computer to GitHub.

---

**Pull**: Downloads newer changes from GitHub to your computer.

---

**Fetch**: Checks GitHub to see whether newer changes exist.

---

**Pull Request / PR**: A request asking:
> "Can we add the changes from my branch to `main`?"

---

**Review**: Another person checks your changes before they become official.

---

**Merge**: The Pull Request was approved and your branch's changes were added to `main`.

---

# Something Looks Wrong?

If any of these happen:
* GitHub says there are conflicts
* Hundreds of unexpected files have changed
* You accidentally worked directly on `main`
* You used the wrong model number
* You're not sure which folder a file belongs in
* Your branch won't push
* Your Pull Request won't merge
* GitHub starts yelling words at you that aren't covered in this document

**Stop and ask in the Wyrdcraft Discord.**

You are significantly less likely to break anything by asking before clicking random buttons.

And even if you do mess something up:

That's one of the reasons we're using Git in the first place.

Usually, it's fixable.
