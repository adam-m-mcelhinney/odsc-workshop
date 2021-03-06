import argparse
import os
from hydrosdk import sdk

if __name__ == '__main__': 
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--model-version', required=True)
    parser.add_argument('--model-name', required=True)
    parser.add_argument('--hydrosphere-address', required=True)
    
    args = parser.parse_args()
    arguments = args.__dict__

    app_name = '{}-app'.format(arguments['model_name'])
    model = '{}:{}'.format(arguments['model_name'], arguments['model_version'])

    application = sdk.Application.singular(app_name, model)

    result = application.apply(arguments['hydrosphere_address'])
    print(result)