#!/bin/sh

if ./terraform --version; then
    echo "terraform already installed"
else
	echo -e "\n"
	echo "************************************************"
	echo '                Terraform Download              '
	echo "************************************************"
	echo -e "\n"

	wget https://releases.hashicorp.com/terraform/0.11.7/terraform_0.11.7_linux_386.zip

	unzip -o terraform_0.11.7_linux_386.zip

	rm -rf terraform_0.11.7_linux_386.zip
fi

echo -e "\n"
echo "************************************************"
echo '                Terraform Init                 '
echo "************************************************"
echo -e "\n"

./terraform init


echo -e "\n"
echo "************************************************"
echo '                Terraform Apply                 '
echo "************************************************"
echo -e "\n"

./terraform apply -auto-approve \
                  -var-file=variables.tfvars \
                  -var client_id=${client_id} \
                  -var client_secret=${client_secret} \
                  -var subscription_id=${subscription_id} \
                  -var tenant_id=${tenant_id} \
		  -var username=${username} \
		  -var password=${password}


echo -e "\n"
echo "************************************************"
echo '                  Terraform Show                '
echo "************************************************"
echo -e "\n"

./terraform show



echo -e "\n"
echo "************************************************"
echo '                Creating Output.json            '
echo "************************************************"
echo -e "\n"


./terraform output -json > vm-output.json
./terraform output  > vm-output.txt
