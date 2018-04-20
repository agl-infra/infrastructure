#${params.userFlag}
echo -e  'data_resource_group="'${params.ResourceGroupName}'"\n'\
		'data_vnet="'${params.VnetName}'"\n'\
        'data_subnet="'${params.SubnetName}'"\n'\
        'image_publisher="'${params.ImagePublisher}'"\n'\
        'image_offer="'${params.ImageOffer}'"\n'\
        'image_sku="'${params.ImageSku}'"\n'\
        'vm_size="'${params.VmSize}'"\n'\
        'vm_name="'${params.VmName}'"\n'\
        'managed_disk_size="'${params.ManagedDiskSize}'"\n'\
        'subscription_id="'${params.SubscriptionId}'"\n'\
        'business_owner_tag="'${params.BusinessOwner}'"\n'\
        'technical_owner_tag="'${params.TechnicalOwner}'"\n'\
        'cost_code_tag="'${params.CostCode}'"\n'\
        'schedule_type_tag="'${params.ScheduleType}'"\n'\
        'project_tag="'${params.Project}'"\n'\
        'os_name="'${params.OperatingSystem}'"\n'> variables.tfvars

echo ${params.CrNumber} > cr.txt
