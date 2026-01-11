# Microsoft ToDo-example for personal-accounts
An example of how to get Microsoft ToDo Tasks using the Graph API for personal account.

## Entra ID setup
Log into https://entra.microsoft.com and register a new app or use an existing one. Make sure you allow the app to be used with personal accounts.
On the Overview page, copy the Application (client) ID and paste it in line 16 (client_id="YOUR-CLIENT-ID",)
In Microsoft Entra, click on "API Permissions" in the sidebar and add the following permissions to the app.
<img width="677" height="174" alt="image" src="https://github.com/user-attachments/assets/2c1688fd-0b23-4c54-98b6-16158f8bfe30" />
Once added, grant admin consent to the changes using the checkmark over the box.
Lastly, click on "Authentication (Preview)" in the sidebar and next to "Redirect URI configuration" click on "Settings". 
Make sure the app includes personal accounts to use the api.
