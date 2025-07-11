# GitHub Personal Access Token Permissions Guide

This guide details the specific permissions needed for GitHub Personal Access Tokens (PATs) when creating and managing repositories.

## Overview

GitHub Personal Access Tokens use a fine-grained permission system. When creating a PAT for repository management, you need to carefully select the appropriate scopes based on your intended operations.

## Core Repository Permissions

### 1. **repo** (Full control of private repositories)
This is the most comprehensive permission for repository management.

**What it allows:**
- Create new repositories (public and private)
- Delete repositories
- Manage repository settings
- Access commit statuses
- Manage deployment keys and services
- Invite collaborators
- Full read/write access to code, issues, pull requests, wikis, settings, webhooks, and deploy keys

**Sub-scopes included:**
- `repo:status` - Access commit status
- `repo_deployment` - Access deployment status
- `public_repo` - Access public repositories
- `repo:invite` - Access repository invitations
- `security_events` - Read and write security events

### 2. **public_repo** (Access public repositories)
A subset of the `repo` scope for public repositories only.

**What it allows:**
- Create public repositories only
- Read/write access to code in public repositories
- Access public repository issues and pull requests
- Cannot create private repositories

## Administrative Permissions

### 3. **delete_repo** (Delete repositories)
**What it allows:**
- Delete repositories you have admin access to
- This is a sensitive permission and should be granted carefully

### 4. **admin:org** (Full control of organizations)
Required if creating repositories within an organization.

**Sub-scopes:**
- `write:org` - Read and write organization data
- `read:org` - Read organization data
- `manage_runners:org` - Manage organization runners
- `workflow` - Update GitHub Action workflow files

## Workflow and Actions Permissions

### 5. **workflow** (Update GitHub Action workflows)
**What it allows:**
- Add or update GitHub Actions workflow files
- Required if your repository management includes CI/CD setup

## User and Collaboration Permissions

### 6. **user** (Update user data)
**Sub-scopes:**
- `read:user` - Read user profile data
- `user:email` - Access user email addresses
- `user:follow` - Follow and unfollow users

### 7. **admin:repo_hook** (Manage repository webhooks)
**What it allows:**
- Create, update, and delete webhooks
- Read webhook configurations
- Test webhook deliveries

### 8. **write:discussion** (Manage repository discussions)
**What it allows:**
- Create and manage discussions
- Moderate discussion comments

## Recommended Permission Sets

### For Basic Repository Creation and Management
```
✓ repo (includes all sub-scopes)
✓ workflow (if using GitHub Actions)
✓ read:user
```

### For Organization Repository Management
```
✓ repo
✓ admin:org
✓ workflow
✓ read:user
```

### For Minimal Public Repository Creation
```
✓ public_repo
✓ read:user
```

### For Full Repository Lifecycle Management
```
✓ repo
✓ delete_repo
✓ admin:repo_hook
✓ workflow
✓ read:user
✓ write:discussion
```

## Creating a Personal Access Token

1. Go to GitHub Settings → Developer settings → Personal access tokens
2. Choose between:
   - **Classic tokens**: Use the scopes listed above
   - **Fine-grained tokens**: More specific repository-level permissions

### Classic Token Creation Steps:
1. Click "Generate new token (classic)"
2. Add a descriptive note
3. Set expiration (recommended: 90 days or less)
4. Select required scopes from the list above
5. Click "Generate token"
6. Copy and securely store the token immediately

### Fine-grained Token Creation Steps:
1. Click "Generate new token (Beta)"
2. Set token name and expiration
3. Select repository access:
   - **All repositories** or
   - **Selected repositories**
4. Set repository permissions:
   - **Actions**: Read/Write (for workflow management)
   - **Administration**: Read/Write (for repo settings)
   - **Contents**: Read/Write (for code access)
   - **Issues**: Read/Write (if managing issues)
   - **Metadata**: Read (always required)
   - **Pull requests**: Read/Write (if managing PRs)
   - **Webhooks**: Read/Write (if managing webhooks)

## Security Best Practices

1. **Principle of Least Privilege**: Only grant permissions you actually need
2. **Token Expiration**: Set short expiration periods (30-90 days)
3. **Token Storage**: Never commit tokens to repositories
4. **Token Rotation**: Regularly rotate tokens
5. **Scope Review**: Periodically review and remove unused permissions
6. **Separate Tokens**: Use different tokens for different applications/purposes

## Common Use Cases and Required Permissions

### Use Case 1: Automated Repository Creation Script
**Required Permissions:**
- `repo` (for private repos) OR `public_repo` (for public only)
- `read:user`

### Use Case 2: CI/CD Pipeline Management
**Required Permissions:**
- `repo`
- `workflow`
- `admin:repo_hook`

### Use Case 3: Organization Repository Management
**Required Permissions:**
- `repo`
- `admin:org`
- `read:user`

### Use Case 4: Repository Backup Tool
**Required Permissions:**
- `repo` (full access to clone all data)
- `read:user`

### Use Case 5: Issue and PR Automation
**Required Permissions:**
- `repo` (or just specific issue/PR scopes in fine-grained tokens)
- `read:user`

## Troubleshooting Permission Issues

### Common Error Messages and Solutions:

1. **"Resource not accessible by integration"**
   - Add `repo` scope for private repositories
   - Add `public_repo` for public repositories

2. **"Must have admin rights to Repository"**
   - Ensure you have the full `repo` scope
   - Check repository ownership/admin status

3. **"Insufficient permissions to create repository"**
   - Add `repo` scope for general creation
   - Add `admin:org` for organization repositories

4. **"Cannot update workflow files"**
   - Add `workflow` scope

## Testing Your Token Permissions

You can test your token permissions using the GitHub API:

```bash
# Test basic authentication
curl -H "Authorization: token YOUR_TOKEN" https://api.github.com/user

# Test repository creation permission
curl -H "Authorization: token YOUR_TOKEN" \
     -X POST https://api.github.com/user/repos \
     -d '{"name":"test-repo","private":true}'

# List token scopes
curl -I -H "Authorization: token YOUR_TOKEN" https://api.github.com/users/octocat
# Check the 'X-OAuth-Scopes' header in the response
```

## Migration from Classic to Fine-grained Tokens

GitHub is moving towards fine-grained personal access tokens. Here's how permissions map:

| Classic Scope | Fine-grained Permission |
|--------------|------------------------|
| `repo` | Contents: Write, Issues: Write, Pull requests: Write, Actions: Write |
| `public_repo` | Same as above but for public repos only |
| `delete_repo` | Administration: Write (with delete enabled) |
| `workflow` | Actions: Write |
| `admin:repo_hook` | Webhooks: Write |
| `admin:org` | Organization permissions (various) |

## Conclusion

Selecting the right permissions for your GitHub Personal Access Token is crucial for both functionality and security. Start with minimal permissions and add more as needed. Always follow security best practices and regularly audit your token usage.

Remember: The `repo` scope is often sufficient for most repository creation and management tasks, but always aim to use the least privileged access that meets your requirements.