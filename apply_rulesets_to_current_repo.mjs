// Import the necessary libraries
import { Octokit } from '@octokit/core';
import fetch from 'node-fetch';

// Initialize Octokit with the GitHub token and fetch implementation
const octokit = new Octokit({
  auth: process.env.GITHUB_TOKEN,
  request: {
    fetch: fetch
  }
});

// Function to get repository rulesets
async function getRepoRulesets(owner, repo) {
  const response = await octokit.request('GET /repos/{owner}/{repo}/rulesets', {
    owner: owner,
    repo: repo,
    headers: {
      'X-GitHub-Api-Version': '2022-11-28'
    }
  });
  console.log(`Fetched rulesets from ${owner}/${repo}:`, JSON.stringify(response.data, null, 2));
  return response.data;
}

// Function to get full details of a specific ruleset
async function getFullRuleset(url, token) {
  const response = await fetch(url, {
    headers: {
      'Authorization': `token ${token}`,
      'Accept': 'application/vnd.github+json',
      'X-GitHub-Api-Version': '2022-11-28'
    }
  });
  const data = await response.json();
  console.log(`Fetched full ruleset details:`, JSON.stringify(data, null, 2));
  return data;
}

// Function to apply rulesets to the current repository
async function applyRulesets(rulesets, owner, repo, token) {
  for (const ruleset of rulesets) {
    const fullRuleset = await getFullRuleset(ruleset._links.self.href, token);
    const data = {
      name: "[WF] " + fullRuleset.name,
      rules: fullRuleset.rules,
      enforcement: fullRuleset.enforcement == 'active' ? 'disabled' : 'active', // Set enforcement to opposite for special enforcement scenarios.
      conditions: fullRuleset.conditions, // Copy the conditions/targets
      bypass_actors: fullRuleset.bypass_actors // Copy bypass actors if any
    };
    const response = await octokit.request('POST /repos/{owner}/{repo}/rulesets', {
      owner: owner,
      repo: repo,
      headers: {
        'X-GitHub-Api-Version': '2022-11-28'
      },
      name: data.name,
      rules: data.rules,
      enforcement: data.enforcement,
      conditions: data.conditions,
      bypass_actors: data.bypass_actors
    });
    console.log(`Applied ruleset to ${owner}/${repo}:`, JSON.stringify(response.data, null, 2));
  }
}

async function main() {
  const token = process.env.GITHUB_TOKEN;
  const [owner, currentRepo] = process.env.GITHUB_REPOSITORY.split('/');
  const [targetOwner, targetRepo] = process.env.TARGET_REPO.split('/');

  // Fetch rulesets from the target repository
  const rulesets = await getRepoRulesets(targetOwner, targetRepo);

  // Apply rulesets to the current repository
  await applyRulesets(rulesets, owner, currentRepo, token);
}

main().catch(error => {
  console.error(error);
  process.exit(1);
});
