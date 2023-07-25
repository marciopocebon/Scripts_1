#!/bin/bash

# get_parameters
while IFS= read -r domain || [ -n "$domain" ]; do
    echo "Scanning domain: $domain"
    python3 ParamSpider/paramspider.py -d "$domain" --level high 
done < subs/all_subs_resolved.txt

# Analyze Parameters 
cat output/* | sort -u > parameters.txt
Cat parameters.txt |kxss

# fast Fuzzing for vulns with nuclei 
nuclei -l parameters.txt -t nuclei_templates/ -et nuclei_templates/Others -et nuclei_templates/cves
