from setuptools import setup

package_name = 'arm_teleop_keyboard'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='arun',
    maintainer_email='arun@todo.todo',
    description='Keyboard teleop for 3DOF arm',
    license='Apache License 2.0',
    entry_points={
        'console_scripts': [
            'teleop = arm_teleop_keyboard.teleop:main'
        ],
    },
)