This repository contains of the reusable workflows under the `feature/reusable-workflows` branch and utility mergeable branches under `mergeable/*`.

These 'mergeable' features are available through an automatic install (and update) workflow via this repository (or any repo with the manuals as they can run on remote and local) `mergeable/manual-workflows` under the actions tab.

![image](https://github.com/RedEyeMods/.github/assets/13383838/4e45389e-58cf-4c89-8a5f-84fe24495542)

![image](https://github.com/RedEyeMods/.github/assets/13383838/0e25c3e0-69a0-460d-975e-1b20fbf14048)

And clicking the `Run Workflow` button and entering your repo information to install remotely (the default ~ installs to the repo the workflow is running on).

![image](https://github.com/RedEyeMods/.github/assets/13383838/dd0fd645-b3e4-4acf-b593-4aff995fa1f2)

### Alternative Local Solution

First add a new remote named `remote`:

`git remote add remote https://github.com/RedEyeMods/.github.git`

and fetching it:

`git fetch remote`

Mergeable branches can be force merged initially into repos by adding a remote and then merging of `something/mergeable/xyz` with `--allow-unrelated-histories`. Further merges need no extra tag since the history is now related.

`git merge remote/mergeable/xyz [--allow-unrelated-histories]`

The below workflow mergeables are working and in use frequently:

- `mergeable/auto-label-pr` - Automatically label pull requests for changelog generation.
- `mergeable/code-owners` - Organization Code Ownership for pull requestion approvals/
- `mergeable/issue-templates` - Organization wide template forms.
- `mergeable/policy` - Organization wide policies.
- `mergeable/gitignore` - Global GITIGNORE.
- `mergeable/license` - Global LICENSE. (LGPL 2.1)
- `mergeable/manual-workflows` - Manual workflows for advannced project setup.
- `mergeable/init` - Initialization script for rulesets.
- `mergeable/auto-desc` - OpenAI diff summarization for pull request descriptions.
  - 🚧 Reserved for select users 🚧
- `mergeable/code-of-conduct` - Contains community ruleset, automatically inherited in the RedEyeMods organization
