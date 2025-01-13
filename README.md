<!--- START OF DELETION --->
# readmefetch

**readmefetch** This GitHub Workflow script, written in Python, automatically generates a neofetch-like README based on your GitHub account stats :D

## 🚀 Setup

### 1. Repository Setup
1. **Fork this repository** to your own GitHub account.
2. ⚠️ **Important**: Rename the forked repository to match your GitHub username exactly.
   - Example: `username/username`

### 2. Create a GitHub Token
1. Go to [GitHub Settings → Developer Settings → Personal Access Tokens → Tokens (classic)](https://github.com/settings/tokens).
2. Click **"Generate new token (classic)"**.
3. **Name**: `ReadmeFetch Token` (or any name you prefer).
4. **Expiration**: Choose as needed (recommended: never expire).
5. **Select scopes**:
   - ✅ `workflow` (Full repository access)
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
5. Click **"Enable workflow"**.
6. Click **"Run workflow"**.
7. Enjoy! 🎉

⚠️ **Note**: It might take a couple of seconds until your new README appears! 😊

## ⚙️ Configuration

Customize your profile by editing `config.json`:
Remove keys to exclude them from your README.

```json
{
  "show_stats": true,          // Show GitHub statistics
  "show_languages": true,      // Display language usage
  "show_contributions": true,  // Show contribution graph
  "custom_note": "",           // Add a personal message
  "ascii_art": "default"       // "default" or "minimal"
  // etc...
}
```


## Example Output

<!--- END OF DELETION --->

<div align='center'>
  <img src='out/fetch.png' alt='Github Fetch'>
</div>
