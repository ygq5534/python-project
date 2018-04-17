from datapackage import Package

package = Package('https://datahub.io/core/gdp/datapackage.json')

"""print(package.resource_names)"""

for resource in package.resources:
    if resource.descriptor['datahub']['type'] == 'derived/csv':
        print(resource)

'''package.getResource('resource').read()'''
'''package.save('world_gdp.json')'''
