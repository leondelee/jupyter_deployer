def _jupyter_bundlerextension_paths():
    '''API for notebook bundler installation on notebook 5.0+'''
    return [{
                'name': 'server_deploy',
                'label': 'Deploy as',
                'module_name': 'server_deploy.deploy',
                'group': 'deploy'
            }
]
