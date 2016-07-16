#!/usr/bin/perl -w 
use strict; 
use Sys::HostAddr;
use Data::Dumper; 
 
my $sysaddr=Sys::HostAddr->new(); 

my $ip_addr=$sysaddr->ip(); 
#print Dumper($ip_addr); 
foreach my $interface(keys %{$ip_addr}) 
{ 
	foreach my $aref(@{$ip_addr->{$interface}}) 
        { 
		printf("$interface  $aref->{address}\n"); 
                #print Dumper($aref); 
	} 
}
