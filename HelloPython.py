import os

def Create():
    PipelineEnv = os.environ.get('ServerName', 'TestServer')
    print(PipelineEnv)

# Create()