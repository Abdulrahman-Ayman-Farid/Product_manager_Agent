# Deployment Guide for Streamlit Community Cloud

This guide provides step-by-step instructions for deploying the Product Manager Agent to Streamlit Community Cloud.

## Prerequisites

1. **GitHub Account**: You need a GitHub account to host your repository
2. **Streamlit Account**: Sign up at [Streamlit Community Cloud](https://streamlit.io/cloud)
3. **API Keys**: Obtain the required API keys:
   - Groq API Key from [Groq Console](https://console.groq.com/)
   - Tavily API Key from [Tavily](https://tavily.com/)

## Step 1: Prepare Your Repository

1. **Create a GitHub Repository**:
   ```bash
   # Create a new repository on GitHub
   # Clone it locally or push your existing code
   git remote add origin https://github.com/yourusername/product-manager-agent.git
   git branch -M main
   git push -u origin main
   ```

2. **Verify Required Files**:
   Ensure your repository contains:
   - `streamlit_app.py` (main application file)
   - `requirements.txt` (dependencies)
   - `app/` directory with agent code
   - `README.md` (documentation)
   - `.gitignore` (to exclude sensitive files)

## Step 2: Deploy to Streamlit Community Cloud

1. **Access Streamlit Cloud**:
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with your GitHub account

2. **Create New App**:
   - Click "New app"
   - Select your GitHub repository
   - Choose the branch (usually `main`)
   - Set the main file path: `streamlit_app.py`
   - Give your app a custom URL (optional)

3. **Configure App Settings**:
   - Click "Advanced settings" before deploying
   - Set Python version to 3.11 (recommended)
   - Add any additional configuration if needed

## Step 3: Configure Environment Variables

1. **Access App Settings**:
   - After deployment, go to your app's settings
   - Click on the gear icon in the top-right corner
   - Select "Settings"

2. **Add Secrets**:
   - Go to the "Secrets" tab
   - Add your API keys in TOML format:
   ```toml
   GROQ_API_KEY = "your_groq_api_key_here"
   TAVILY_API_KEY = "your_tavily_api_key_here"
   ```

3. **Save and Restart**:
   - Save the secrets
   - The app will automatically restart with the new environment variables

## Step 4: Test Your Deployment

1. **Access Your App**:
   - Your app will be available at: `https://your-app-name.streamlit.app`
   - Or the custom URL you specified

2. **Test Functionality**:
   - Initialize the agent (API keys should be automatically loaded)
   - Test the chat interface
   - Generate sample documents
   - Verify download functionality

## Step 5: Share Your App

1. **Get the Public URL**:
   - Copy the app URL from Streamlit Cloud dashboard
   - Share with users who need access

2. **App Management**:
   - Monitor app usage in the Streamlit Cloud dashboard
   - View logs for debugging
   - Manage app settings and secrets

## Troubleshooting Deployment Issues

### Common Problems and Solutions

1. **Import Errors**:
   ```
   ModuleNotFoundError: No module named 'xyz'
   ```
   - **Solution**: Ensure all dependencies are listed in `requirements.txt`
   - Check for typos in package names
   - Verify package versions are compatible

2. **API Key Issues**:
   ```
   Error: API key not found
   ```
   - **Solution**: Check that secrets are properly configured in Streamlit Cloud
   - Ensure secret names match the environment variable names in your code
   - Verify API keys are valid and have sufficient quota

3. **Memory or Resource Limits**:
   ```
   App crashed due to resource limits
   ```
   - **Solution**: Optimize your code for memory usage
   - Consider using Streamlit's caching mechanisms
   - Reduce model size or complexity if possible

4. **Git Repository Issues**:
   ```
   Repository not found or access denied
   ```
   - **Solution**: Ensure repository is public or Streamlit has access
   - Check repository URL and branch name
   - Verify file paths are correct

### Debugging Tips

1. **Check App Logs**:
   - View real-time logs in Streamlit Cloud dashboard
   - Look for error messages and stack traces

2. **Test Locally First**:
   - Always test your app locally before deploying
   - Use the same Python version as your deployment

3. **Incremental Deployment**:
   - Deploy a minimal version first
   - Add features incrementally
   - Test each addition thoroughly

## Updating Your Deployed App

1. **Code Updates**:
   - Push changes to your GitHub repository
   - Streamlit Cloud will automatically detect changes
   - App will redeploy automatically

2. **Dependency Updates**:
   - Update `requirements.txt` as needed
   - Push changes to trigger redeployment

3. **Configuration Changes**:
   - Update secrets in Streamlit Cloud settings
   - Restart app if necessary

## Best Practices

1. **Security**:
   - Never commit API keys to your repository
   - Use Streamlit's secrets management
   - Keep sensitive information in environment variables

2. **Performance**:
   - Use Streamlit's caching for expensive operations
   - Optimize imports and initialization
   - Monitor app performance and resource usage

3. **User Experience**:
   - Provide clear error messages
   - Add loading indicators for long operations
   - Include helpful documentation and instructions

4. **Maintenance**:
   - Regularly update dependencies
   - Monitor API usage and costs
   - Keep documentation up to date

## Support and Resources

- **Streamlit Documentation**: [docs.streamlit.io](https://docs.streamlit.io)
- **Streamlit Community**: [discuss.streamlit.io](https://discuss.streamlit.io)
- **GitHub Issues**: Use your repository's issue tracker
- **API Provider Support**: Check Groq and Tavily documentation

## Conclusion

Following this guide should result in a successfully deployed Product Manager Agent on Streamlit Community Cloud. The app will be publicly accessible and ready for users to interact with for product management tasks.

Remember to monitor your API usage and costs, especially if the app receives significant traffic. Consider implementing usage limits or authentication if needed for production use.

