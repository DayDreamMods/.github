This repository contains (most) of the reusable workflows under the `feature/reusable-workflows` branch and utility mergeable branches under `feature/mergeable/*`.

First add a new remote named `something`:

`git remote add something https://github.com/RedEyeMods/.github.git`

and fetching it:

`git fetch something`

Mergeable branches can be force merged initially into repos by adding a remote and then merging of `something/feature/mergeable/xyz` with `--allow-unrelated-histories`. Further merges need no extra tag since the history is now related.

`git merge something/feature/mergeable/xyz [--allow-unrelated-histories]`

The below workflow mergeables are working and in use frequently:

- `feature/mergeable/policy` - Organization workflow based policy
- `feature/mergeable/auto-label-pr` - Automatically label PRs based on branch name
- `feature/mergeable/issue-templates` - Uniform issue templates
