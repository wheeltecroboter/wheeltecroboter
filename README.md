<!--- START OF DELETION --->
# readmefetch

**readmefetch** This GitHub Workflow script, written in Python, automatically generates a neofetch-like README based on your GitHub account stats :D

## 🚀 Setup

### 1. Repository Setup
1. **Fork this repository**.
2. **Rename the fork** to match your GitHub username (e.g., `username/username`).

### 2. Create a GitHub Token
1. Go to [GitHub Settings → Developer Settings → Personal Access Tokens → Tokens (classic)](https://github.com/settings/tokens).
2. Click **"Generate new token (classic)"**.
3. **Name**: `whatever you want (e.g Readmefetch Token)`.
4. **Expiration**: Choose as needed. Never recommended, otherwise it won't automatically update
5. **Select scopes**: `workflow`.
6. Click **"Generate"** and **copy the token**! You will never see it again!

### 3. Configure the Repository
1. Go to your fork's **"Settings" → "Secrets and variables" → "Actions"**.
2. Create a new repository secret:
   - **Name**: `GH_TOKEN`
   - **Value**: Your copied token

### 4. Enable Actions
1. Go to the **"Actions"** tab.
2. Click **"Enable workflow"**.
3. Click **"Run workflow"**.

⚠️ **Note**: It might take a couple of seconds until your new README appears! 😊

## ⚙️ Configuration

Customize your profile by editing `config.json`:
Remove keys to exclude them from your README.

```json
{
  "display_stats": [
    "username",
    "bio",
    "location",
    "company",
    "email",
    "hireable",
    "followers",
    "following",
    "public_repos",
    "public_gists",
    "total_stars",
    "lines_of_code",
    "created_at",
    "updated_at",
    "languages",
    "total_commits",
    "total_issues",
    "total_prs"
  ],
  "additional_info": "", // some additional information you can provide :)
  "preferred_color": "lightblue", // color it will be printed out in
  "max_languages": 5, // number of max. biggest languages displayed in the fetch
  "append_autmatic": true // appends the embedded image automatically if not found in README 
}
```
### Editing the README

After the initial deployment, you can edit the `README.md` file however you want!

## Disclaimer

Use this script at your own risk. The software is provided "as is", without warranty of any kind, express or implied, as stated in the MIT License.

## Example Output

<!--- END OF DELETION --->

<div align='center'>
  <img src='out/fetch.png' alt='Github Fetch'>
</div>
