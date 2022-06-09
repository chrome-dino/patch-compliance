$content = Get-Content -Path $Args[0]
foreach ($item in $content){
	$host_split = $item.Split("/")
	$computer = $host_split[0]
	$os = $host_split[1]
	if(Test-Connection -ComputerName $computer){
		Get-HotFix -ComputerName ${computer} > "./patch_compliance/src/patch_compliance/host_data/host_${computer}.txt"
		Add-Content "./patch_compliance/src/patch_compliance/host_data/host_${computer}.txt" "`n${os}"
	}else{
		Write-Output "Failed to connect to : ${item}"
	}
}
