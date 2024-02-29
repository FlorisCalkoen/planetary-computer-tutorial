# planetary-computer-tutorial

## Accessing the content on Planetary Computer 

1. Open the Planetary Computer [JupyterHub](https://pccompute.westeurope.cloudapp.azure.com/)
2. Open a shell by clicking on the `+` sign and select "terminal"
3. Run the following command: 
   ```bash
   mkdir -p ~/dev/
   cd ~/dev
   ```
4. Fork the tutorial [repository](https://github.com/floriscalkoen/planetary-computer-tutorial)
5. Go back to the Planetary Computer shell, clone your forked tutorial repository to Planetary Computer by running: 
   ```bash 
   git clone https://github.com/<GITHUB_USER>/planetary-computer-tutorial.git
   ```
7. Now you can find the repository in the file browser on the left. 
8. Add a token and storage account in the .env file to access the datasets that you need.
   You can ask Floris Calkoen for a token. If you are unfamiliar with vim keybindings,
   press "i" to go into insert mode and use it as your regular text editor. 
   ```bash
   cp ~/dev/planetary-computer-tutorial/.env.example ~/dev/planetary-computer-tutorial/.env
   vim ~/dev/planetary-computer-tutorial/.env
   ```

## Pushing your changes to GitHub from Planetary Computer 

1. You need to configure Git by SSH to commit your changes to Github. 
2. https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=linux
3. `sh-keygen -t ed25519 -C "<YOUR_EMAIL>"`
5. Enter, enter, enter. 
6. `chmod 600 ~/.ssh/id_ed25519`
7. ssh-add ~/.ssh/id_ed25519
8. Follow
   [these](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)
   instructions to add the ssh key to your GitHub profile.
9. Add your remote fork as origin: 
    ```bash
    git remote set-url origin git@github.com:<USER_NAME>/planetary-computer-tutorial.git
    ```
10. Once you re-start your Planetary Computer hub you might have to change the permissions
   on the file again by running: 
    ```bash
    chmod 600 ~/.ssh/id_ed25519
    ```