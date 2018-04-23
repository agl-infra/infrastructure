ip=$(cat vm-output.txt | grep Private_IP | cut -d '=' -f2 | awk '{$1=$1};1')
#ssh -t 'root@10.228.10.7' 'ssh-keygen -R '$ip''
#ssh -t 'root@10.228.10.7' 'sshpass -f password.txt ssh-copy-id agl-user@'$ip''
ssh -t 'root@10.228.10.7' 'ssh-copy-id agl-user@'$ip''
#echo '###########'
ssh -t 'root@10.228.10.7' ip="$ip" bash -s<<'SSH_EOF'
ssh -t  agl-user@$ip 'echo AGL@12345678 | sudo -S sh -c "echo '10.228.10.5 azsal0047.4uepctfschkudburuyfkqje5le.px.internal.cloudapp.net'>> /etc/hosts"'
SSH_EOF
echo '####1234#####'
ssh -t 'root@10.228.10.7' 'cd chef-repo && knife bootstrap '$ip' -N '$ip' -x agl-user -P AGL@12345678 --sudo --run-list recipe[installagents]'
