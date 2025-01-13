<!--- START OF DELETION --->
# readmefetch

**readmefetch** This GitHub Workflow script, written in Python, automatically generates a neofetch-like README based on your GitHub account stats :D

## 🚀 Setup

### 1. Repository Setup
1. **Fork this repository** to your own GitHub account.
2. ⚠️ **Important**: Rename the forked repository to match your GitHub username exactly. 
   - **If you want this to appear on your profile of course - you can name it whatever you want to just check it out, but if you want the fetch to appear on your profile, it has to match your username**
   - Example: `username/username`

### 2. Create a GitHub Token

**Why is this necessary? -> Because the Python Script uses PyGithub which rate limits requests with no tokens to 60 Requests/ Hour and with a Token to 5000 Requests / Hour. Without a Token, the rate limit will be hit really quickly and this script won't work (trust me I tried)**

1. Go to [GitHub Settings → Developer Settings → Personal Access Tokens → Tokens (classic)](https://github.com/settings/tokens).
2. Click **"Generate new token (classic)"**.
3. **Name**: `ReadmeFetch Token` (or any name you prefer).
4. **Expiration**: Choose as needed (recommended: never expire).
5. **Select scopes**:
   - ✅ `workflow`
6. Click **"Generate"**.
7. 📝 **COPY THE TOKEN** - You won't see it again!

### 3. Configure the Repository
1. Go to your fork's **"Settings" → "Secrets and variables" → "Actions"**.
2. Create a new repository secret:
   - **Name**: `GH_TOKEN`
   - **Value**: Your copied token

### 4. Enable Actions
1. Go to the **"Actions"** tab.
2. Click **"I understand my workflows, go ahead and enable them"**.
3. On the left sidebar, go to **"Start Workflow"**.
4. A message saying something like **"This scheduled workflow is disabled because scheduled workflows are disabled by default in forks."** should appear.
   - **This is because I disabled the script, otherwise it would always run on this repo and remove the instructions (if anyone knows a better solution, lmk!)**
5. Click **"Enable workflow"**.
6. Click **"Run workflow"**.
7. Enjoy! 🎉

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
