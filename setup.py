from setuptools import setup

setup(
    name='twitter_media_upload',
    url='https://github.com/twitterdev/large-video-upload-python',
    version='0.0.3',
    description='Uploading large video files asynchronously with the Twitter API.',
    author='Twitter Dev',
    author_email='foo@bar.com',
    license='MIT',
    packages=['twitter_media_upload'],
    install_requires=['oauthlib', 'requests', 'requests-oauthlib'],
)
