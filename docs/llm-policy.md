---
layout: default
title: LLM Usage Policy
---

# LLM usage policy and definitions

This page details the LLM usage policy for contributions to Universal-DB itself
as well as the definitions we use for an apps "LLM Usage" as displayed on the app card.

This page uses the word "LLM" (Large Language Model) to describe any large scale text
generation program, sometimes called "AI", ie. ChatGPT, GitHub Copilot, etc.

When submitting an app please make sure to select the correct option, apps found
to have maliciously indicated the wrong field (ie. None on a "vibecoded" app) are
subject to permanent removal from the database. If LLM usage changes later, we appreciate
if you drop an issue or pull request updating the value. If in doubt it is better to choose
"undisclosed" than to falsely indicate LLM usage.

## Definitions

### None (or minimal)

This indicates that LLM tools have not been used in any meaningful capacity.
As it can be difficult to strictly disallow *all* LLM usage, we find the
[Azahar3DS AI policy][azahar] a good example of what this category describes.

[azahar]: https://github.com/azahar-emu/azahar/blob/master/AI-POLICY.md

### Minor

Apps in this tier indicate that they have used LLMs to write meaningful portions of their
code, documentation, release notes, etc. but the overall project is still being largely
human-managed.

When submitting, select this if:
- You have used an LLM to write some functions, READMEs, release notes, etc
- You belive that you (or a human working on the code) has checked all LLM output to do as expected
- You have **NOT** used an LLM to do large-scale "vibecoding" tasks

### Major

This indicates that large portions of code have been written by an LLM, often called
"vibecoding". The author may not be fully aware of how every portion of the code works,
some may have never been reviewed at all.

When submitting, select this if:
- You have used an LLM to write or re-write large portions of code (ie. whole files)
- You consider yourself to be "vibecoding"
- You have used an LLM to generate code without carefully reviewing that code to ensure it should work as expected

### Undisclosed

Our LLM usage field was only added in May 2026 so anything submitted to the database before that point
will default to displaying "undisclosed". This does not inherently indicate anything about the author's
opinions or usage of LLM tools. All apps not updated since before 2023 are assumed to have not had access
to LLM tools, if you update your app and it changes from "none" to "undisclosed" this is why.

When submitting, please consider the other options first, but this can be valid if:
- You do not know if any significant contributors to your project have used LLMs
- You have not yet used LLMs, but see yourself potentially using them in the future

## Universal-DB LLM Policy

This is the LLM usage policy for Universal-DB itself:

- Usage of LLM tools to write apps being submitted to Universal-DB is **okay** so long as it is indicated properly
- Usage of LLM tools to write code for Universal-DB **itself** is **prohibited**
   - Particularly small portions of code that you have reviewed (ie ["none"](#none-or-minimal) above) may be acceptable, we would prefer you let us know than try sneak it past us
- Usage of LLM tools to write descriptions for pull requests or issues is **prohibited**
   - Please just take a second to write it yourself, a sentence or two usually suffices
