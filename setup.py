from setuptools import setup, find_packages

# Read the contents of your README file (if you have one)
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='llm-confidence',  # Replace with your desired package name
    version='0.2.0',
    author='Ruth Miller',  # Replace with your name or organization
    author_email='ruth.miller@bluedotcorp.com',  # Replace with your email
    description='A Python package for extracting confidence scores from LLM models outputs, particularly using log probabilities',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/VATBox/llm-confidence',  # Replace with your GitHub repo link
    packages=find_packages(),  # Automatically find and include all packages
    license='Apache 2.0',  # License declaration
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',  # Specify your minimum Python version
    install_requires=[
        'numpy',
        'pandas',
    ],
    keywords='logprobs handler confidence json ai llm machine-learning',  # Relevant keywords for your package
    project_urls={  # Additional links you want to provide
        'Bug Tracker': 'https://github.com/VATBox/llm-confidence/issues',  # Link to issue tracker
    },
)
