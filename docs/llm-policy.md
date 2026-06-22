---
layout: default
title: LLM Usage Policy
table:
  - title: None
    definition: |
      This indicates that LLM tools have not been used in any
      meaningful capacity.
  - title: LLM Assistance
    definition: |
      LLM assisted work is when an LLM has been used in the process of
      development, but the output of the LLM has not been directly incorporated
      into the work.

      Examples of this include analysis of the codebase, code review, assisting
      with debugging, etc.
  - title: LLM Generation
    definition: |
      LLM generated work is when the output of an LLM has been directly
      incorportated into the work, whether that be code, art, music,
      documentation, etc.

      Any app with commits attributed to Claude, Cursor, Copilot, etc will be
      automatically assigned LLM generated. That said, commit attribution is not
      required for work to be LLM generated, if you have directly used the
      output of an LLM you should select this category.
  - title: Undisclosed
    definition: |
      Our LLM usage field was only added in May 2026 so anything submitted to
      the database before that point will default to displaying "undisclosed".
      This does not inherently indicate anything about the author's opinions or
      usage of LLM tools. All apps not updated since before 2023 are assumed to
      have not had access to LLM tools, if you update your app and it changes
      from "none" to "undisclosed" this is why.

      We would prefer all new apps indicate LLM usage, but choosing to leave
      it undisclosed is still valid.
---

# LLM usage policy and definitions

This page details the LLM usage policy for contributions to Universal-DB itself
as well as the definitions we use for an apps "LLM Usage" as displayed on the
app card.

This page uses the word "LLM" (Large Language Model) to describe any large
scale text generation program, sometimes called "AI", ie. ChatGPT, GitHub
Copilot, etc.

When submitting an app please make sure to select the correct option, apps
found to have maliciously indicated the wrong field (ie. None on a "vibecoded"
app) are subject to permanent removal from the database. If LLM usage changes
later, we appreciate if you drop an issue or pull request updating the value.

## Definitions

<table class="table">
    {% for item in page.table %}
        <tr><th>{{ item.title }}</th><td>{{ item.definition | markdownify }}</td></tr>
    {% endfor %}
</table>

## Universal-DB LLM Policy

This is the LLM usage policy for Universal-DB itself:

- Usage of LLM tools in the process of making apps being submitted to Universal-DB is **okay** so long as it is indicated properly
- Usage of LLM tools to generate code or other assets for Universal-DB **itself** is **prohibited**
- Usage of LLM tools to write descriptions for pull requests or issues is **prohibited**
   - Please just take a second to write it yourself, a sentence or two usually suffices
