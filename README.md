# jupyter_deployer
This is a jupyter notebook bundler extension, which can deploy .ipynb files on a remote server using flask.
</br>To use it, first put the folder server_deployer under your python site-packages.
</br>Then enable it :

    jupyter bundlerextension enable --sys-prefix --py server_deployer
 
</br>Finally, edit the config.py in order to let the extension know which server you want to deploy.
