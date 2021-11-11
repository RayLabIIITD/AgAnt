"""
This example client takes a PDB file, sends it to the REST service, which
creates HSSP data. The HSSP data is then output to the console.

Example:

    python pdb_to_hssp.py 1crn.pdb http://www.cmbi.umcn.nl/xssp/
"""

import argparse
import json
import requests
import time
import glob

def pdb_to_hssp(pdb_file_path, rest_url,pa):
    # Read the pdb file data into a variable
    files = {'file_': open(pdb_file_path, 'rb')}

    # Send a request to the server to create hssp data from the pdb file data.
    # If an error occurs, an exception is raised and the program exits. If the
    # request is successful, the id of the job running on the server is
    # returned.
    url_create = '{}api/create/pdb_file/dssp/'.format(rest_url)
    r = requests.post(url_create, files=files)
    r.raise_for_status()

    job_id = json.loads(r.text)['id']
    print ("Job submitted successfully. Id is: '{}'".format(job_id))

    # Loop until the job running on the server has finished, either successfully
    # or due to an error.
    ready = False
    while not ready:
        # Check the status of the running job. If an error occurs an exception
        # is raised and the program exits. If the request is successful, the
        # status is returned.
        url_status = '{}api/status/pdb_file/dssp/{}/'.format(rest_url,
                                                                  job_id)
        r = requests.get(url_status)
        r.raise_for_status()

        status = json.loads(r.text)['status']
        print("Job status is: '{}'".format(status))

        # If the status equals SUCCESS, exit out of the loop by changing the
        # condition ready. This causes the code to drop into the `else` block
        # below.
        #
        # If the status equals either FAILURE or REVOKED, an exception is raised
        # containing the error message. The program exits.
        #
        # Otherwise, wait for five seconds and start at the beginning of the
        # loop again.
        if status == 'SUCCESS':
            ready = True
        elif status in ['FAILURE', 'REVOKED']:
            raise Exception(json.loads(r.text)['message'])
        else:
            time.sleep(5)
    else:
        # Requests the result of the job. If an error occurs an exception is
        # raised and the program exits. If the request is successful, the result
        # is returned.
        url_result = '{}api/result/pdb_file/dssp/{}/'.format(rest_url,
                                                                  job_id)
        r = requests.get(url_result)
        r.raise_for_status()
        result = json.loads(r.text)['result']
        print(type(result))
        open(pa+pdb_file_path[-8:-4]+".dssp",'w').write(result)
        # Return the result to the caller, which prints it to the screen.
        return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create HSSP from a PDB file')
    for filename in glob.glob("ant_bind/*.pdb"):
        path=filename
        url="https://www3.cmbi.umcn.nl/xssp/"
        result = pdb_to_hssp(path, url,"ant_bind/")
    for filename in glob.glob("ago_bind/*.pdb"):
        path=filename
        url="https://www3.cmbi.umcn.nl/xssp/"
        result = pdb_to_hssp(path, url,"ago_bind/")
#result = pdb_to_hssp(args.pdb_file_path, args.rest_url)
        #print (result)