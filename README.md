1. pip install virtualenv ->to able to use venv
2. python -m venv .venv -to generate the venv file - the .venv is just the filename can be given any

3. .\.venv\Scripts\activate -> to activate environment

4. pip list ->to see dependcy

5. to give out the list
pip list > requirement.txt
- requirement file will be generated with the
dependcy in it

6. now to install the generated list we write
pip install -r requirements.txt

7. deactivate -> command to go out of venv
