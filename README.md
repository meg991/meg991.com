1. Register a domain Godaddy.com
        - meg991.com
2. Use Route 53 to configoure the DNS
        - NS enteries
                ns-913.awsdns-50.net
                ns-299.awsdns-37.com
                ns-1448.awsdns-53.org
                ns-1597.awsdns-07.co.uk
        - Run DNS Checker
        - Created an apex entry
        - Created an www entry       
3. Use Elastic Beanstalk as the Pipeline management
        - Open the tutorial (for windows)
        - Created the local app
        - Tested it locally
        - eb init
                - eb init -p python-3.6 meg991 --region us-west-2
                 - eb create meg-env
                 - profile erm
        - Installed EB cli
        - pip install awsebcli --upgrade
        - Deploy
4. Use git as a version control system
        - https://github.com/meg991/meg991.com
        
