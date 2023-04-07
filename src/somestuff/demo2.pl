#!/usr/bin/perl -w


use Bio::DB::GenBank

$db_obj = Bio::DB::GenBank->new;

#$seq_obj = $db_obj->get_Seq_by_id(2);
#print $seq_obj->seq;


$seq_obj = $db_obj->get_Seq_by_version("J01673.1");
#$seq_obj = $db_obj->get_Seq_by_version("NP_055179");
print $seq_obj->seq;
print "\n";


