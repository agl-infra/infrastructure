ip=$(cat vm-output.txt | grep Private_IP | cut -d '=' -f2 | awk '{$1=$1};1')
ssh-keygen -R $ip
sshpass -p $password ssh-copy-id $username@$ip -o StrictHostKeyChecking=no -f
ssh -t  $username@$ip 'echo '$password' | sudo -S sh -c "echo '10.228.10.5 azsal0047.4uepctfschkudburuyfkqje5le.px.internal.cloudapp.net'>> /etc/hosts"'
ssh -t 'root@10.228.10.7' 'cd chef-repo && knife bootstrap '$ip' -N '$ip' -x '$username' -P '$password' --sudo  --no-host-key-verify --run-list recipe[installagents]'
