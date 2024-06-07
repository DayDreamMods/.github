This repository contains (most) of the reusable workflows under the `feature/reusable-workflows` branch and utility mergeable branches under `feature/mergeable/*`.

These 'mergeable' features are available through an automatic install (and update) workflow via this repository (or any repo with the manuals as they can run on remote and local) `feature/mergeable/manual-workflows` under the actions tab.

![image](https://github.com/RedEyeMods/.github/assets/13383838/4e45389e-58cf-4c89-8a5f-84fe24495542)

![image](https://github.com/RedEyeMods/.github/assets/13383838/0e25c3e0-69a0-460d-975e-1b20fbf14048)

And clicking the `Run Workflow` button and entering your repo information to install remotely (the default ~ installs to the repo the workflow is running on).

![image](https://github.com/RedEyeMods/.github/assets/13383838/dd0fd645-b3e4-4acf-b593-4aff995fa1f2)

### Alternative Local Solution

First add a new remote named `something`:

`git remote add something https://github.com/RedEyeMods/.github.git`

and fetching it:

`git fetch something`

Mergeable branches can be force merged initially into repos by adding a remote and then merging of `something/feature/mergeable/xyz` with `--allow-unrelated-histories`. Further merges need no extra tag since the history is now related.

`git merge something/feature/mergeable/xyz [--allow-unrelated-histories]`

The below workflow mergeables are working and in use frequently:

- `feature/mergeable/auto-label-pr` - Automatically label pull requests for changelog generation.
- `feature/mergeable/code-owners` - Organization Code Ownership for pull requestion approvals/
- `feature/mergeable/issue-templates` - Organization wide template forms.
- `feature/mergeable/policy` - Organization wide policies.
- `feature/mergeable/gitignore` - Global GITIGNORE.
- `feature/mergeable/license` - Global LICENSE. (LGPL 2.1)
- `feature/mergeable/manual-workflows` - Manual workflows for advannced project setup.
- `feature/mergeable/init` - Initialization script for rulesets.
- `feature/mergeable/auto-desc` - OpenAI diff summarization for pull request descriptions.
  - 🚧 Reserved for select users 🚧
- `feature/mergeable/code-of-conduct` - Contains community ruleset, automatically inherited in the RedEyeMods organization
