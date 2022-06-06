$content = Get-Content -Path $Args[0]
for each($host in $content){
	$host_split = $host.Split("/")
	$computer = $host_split[0]
	$os = $host_split[1]
	if(Test-Connection -ComputerName $host){
		Get-HotFix -ComputerName ${computer} > "./host_data/host_${computer}.txt"
		Add-Content "./host_data/host_${computer}.txt" "`n${os}"
	}else{
		Write-Output "Failed to connect to : $(items)"
	}
}