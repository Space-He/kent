#!/usr/bin/env perl

use strict;
use warnings;
use File::Basename;

my $topLevel = "/hive/data/genomes/asmHubs";

my %betterName;	# key is asmId, value is common name
my $hubName = "vertebrate";
my $Name = "Vertebrate";
my $srcDocDir = "${hubName}sAsmHub";

my $home = $ENV{'HOME'};
my $srcDir = "$home/kent/src/hg/makeDb/doc/$srcDocDir";
my $commonNameList = "$hubName.asmId.commonName.tsv";
my $commonNameOrder = "$hubName.commonName.asmId.orderList.tsv";

open (FH, "<$srcDir/${commonNameList}") or die "can not read $srcDir/${commonNameList}";
while (my $line = <FH>) {
  chomp $line;
  my ($asmId, $name) = split('\t', $line);
  $betterName{$asmId} = $name;
}
close (FH);

my @orderList;	# asmId of the assemblies in order from the *.list files
# the order to read the different .list files:
my $assemblyCount = 0;

open (FH, "<$srcDir/${commonNameOrder}") or die "can not read ${commonNameOrder}";
while (my $line = <FH>) {
  chomp $line;
  my ($commonName, $asmId) = split('\t', $line);
  push @orderList, $asmId;
  ++$assemblyCount;
}
close (FH);

my $destDir = "/hive/data/genomes/asmHubs";

my $orderKey = 1;
foreach my $asmId (reverse(@orderList)) {
  my $accessionDir = substr($asmId, 0 ,3);
  $accessionDir .= "/" . substr($asmId, 4 ,3);
  $accessionDir .= "/" . substr($asmId, 7 ,3);
  $accessionDir .= "/" . substr($asmId, 10 ,3);
  $accessionDir .= "/" . $asmId;
  $destDir = "/hive/data/genomes/asmHubs/$accessionDir";
  my $buildDir = "/hive/data/genomes/asmHubs/refseqBuild/$accessionDir";
  if ( ! -d "${destDir}" ) {
    `mkdir -p "${destDir}"`;
  }
  printf STDERR "ln -s '${buildDir}' '${destDir}'\n";
  `rm -f "${destDir}/bbi"`;
  `rm -f "${destDir}/ixIxx"`;
  `rm -fr "${destDir}/html"`;
  `mkdir -p "${destDir}/html"`;
  `rm -f "${destDir}/${asmId}.2bit"`;
  `rm -f "${destDir}/${asmId}.agp.gz"`;
  `rm -f "${destDir}/${asmId}.chrom.sizes"`;
  `rm -f "${destDir}/${asmId}_assembly_report.txt"`;
  `rm -f "${destDir}/${asmId}.trackDb.txt"`;
  `rm -f "${destDir}/${asmId}.genomes.txt"`;
  `rm -f "${destDir}/${asmId}.hub.txt"`;
  `rm -f "${destDir}/${asmId}.groups.txt"`;
  `ln -s "${buildDir}/bbi" "${destDir}/bbi"`;
  `ln -s "${buildDir}/ixIxx" "${destDir}/ixIxx"`;
  `ln -s ${buildDir}/html/*.html "${destDir}/html/"`;
   my $jpgFiles =`ls ${buildDir}/html/*.jpg 2> /dev/null | wc -l`;
   chomp $jpgFiles;
   if ($jpgFiles > 0) {
    `rm -f ${destDir}/html/*.jpg`;
    `ln -s ${buildDir}/html/*.jpg "${destDir}/html/"`;
   }
#  `ln -s ${buildDir}/html/*.png "${destDir}/genomes/${asmId}/html/"`;
  `ln -s "${buildDir}/${asmId}.2bit" "${destDir}/"`;
  `ln -s "${buildDir}/${asmId}.agp.gz" "${destDir}/"`;
  `ln -s "${buildDir}/${asmId}.chrom.sizes" "${destDir}/"`;
  `ln -s "${buildDir}/download/${asmId}_assembly_report.txt" "${destDir}/"`;
  `ln -s "${buildDir}/${asmId}.trackDb.txt" "${destDir}/"`;
  `ln -s "${buildDir}/${asmId}.genomes.txt" "${destDir}/"`;
  `ln -s "${buildDir}/${asmId}.hub.txt" "${destDir}/"`;
  `ln -s "${buildDir}/${asmId}.groups.txt" "${destDir}/"`;
}

__END__

my $hubDir = "/gbdb/hubs/$hubName";

`rm -f "${hubDir}/index.html"`;
`ln -s "${destDir}/index.html" "${hubDir}/index.html"`;
`rm -f "${hubDir}/testIndex.html"`;
`ln -s "${destDir}/testIndex.html" "${hubDir}/testIndex.html"`;
`rm -f "${hubDir}/testAsmStats${Name}.html"`;
`ln -s "${destDir}/testAsmStats${Name}.html" "${hubDir}/testAsmStats${Name}.html"`;

__END__
;
  my $asmReport="$buildDir/download/${asmId}_assembly_report.txt";
  my $descr=`grep -i "organism name:" $asmReport | head -1 | sed -e 's#.*organism name: *##i; s# (.*\$##;'`;
  chomp $descr;
  my $orgName=`grep -i "organism name:" $asmReport | head -1 | sed -e 's#.* name: .* (##; s#).*##;'`;
  chomp $orgName;
  $orgName = $betterName{$asmId} if (exists($betterName{$asmId}));

  printf "genome %s\n", $asmId;
  printf "trackDb genomes/%s/%s.trackDb.txt\n", $asmId, $asmId;
  printf "groups groups.txt\n";
  printf "description %s\n", $orgName;
  printf "twoBitPath genomes/%s/%s.2bit\n", $asmId, $asmId;
  printf "organism %s\n", $descr;
  my $chrName=`head -1 $buildDir/$asmId.chrom.sizes | awk '{print \$1}'`;
  chomp $chrName;
  my $bigChrom=`head -1 $buildDir/$asmId.chrom.sizes | awk '{print \$NF}'`;
  chomp $bigChrom;
  my $oneThird = int($bigChrom/3);
  my $tenK = $oneThird + 10000;
  $tenK = $bigChrom if ($tenK > $bigChrom);
  my $defPos="${chrName}:${oneThird}-${tenK}";
  if ( -s "$asmId/defaultPos.txt" ) {
    $defPos=`cat "$asmId/defaultPos.txt"`;
    chomp $defPos;
  }
  printf "defaultPos %s\n", $defPos;
  printf "orderKey %d\n", $orderKey++;
  printf "scientificName %s\n", $descr;
  printf "htmlPath genomes/%s/html/%s.description.html\n", $asmId, $asmId;
  printf "\n";
  my $localGenomesFile = "$buildDir/${asmId}.genomes.txt";
  open (GF, ">$localGenomesFile") or die "can not write to $localGenomesFile";
  printf GF "genome %s\n", $asmId;
  printf GF "trackDb %s/%s.trackDb.txt\n", $asmId, $asmId;
  printf GF "groups groups.txt\n";
  printf GF "description %s\n", $orgName;
  printf GF "twoBitPath %s/%s.2bit\n", $asmId, $asmId;
  printf GF "organism %s\n", $descr;
  printf GF "defaultPos %s\n", $defPos;
  printf GF "orderKey %d\n", $orderKey++;
  printf GF "scientificName %s\n", $descr;
  printf GF "htmlPath %s/html/%s.description.html\n", $asmId, $asmId;
  close (GF);
}

__END__

description Mastacembelus armatus
twoBitPath GCA_900324485.2_fMasArm1.2/trackData/addMask/GCA_900324485.2_fMasArm1.2.masked.2bit
organism Zig-Zag eel
defaultPos LR535842.1:14552035-14572034
orderKey 1
scientificName Mastacembelus armatus
htmlPath GCA_900324485.2_fMasArm1.2/html/GCA_900324485.2_fMasArm1.2.description.html

# head -25 GCA_002180035.3_HG00514_prelim_3.0_assembly_report.txt

# Assembly name:  HG00514_prelim_3.0
# Organism name:  Homo sapiens (human)
# Isolate:  HG00514
# Sex:  female
# Taxid:          9606
# BioSample:      SAMN04229552
# BioProject:     PRJNA300843
# Submitter:      The Genome Institute at Washington University School of Medicine
# Date:           2018-05-22
# Assembly type:  haploid
# Release type:   major
# Assembly level: Chromosome
# Genome representation: full
# WGS project:    NIOH01
# Assembly method: Falcon v. November 2016
# Expected final version: no
# Genome coverage: 80.0x
# Sequencing technology: PacBio RSII
# GenBank assembly accession: GCA_002180035.3
#
## Assembly-Units:
## GenBank Unit Accession       RefSeq Unit Accession   Assembly-Unit name
## GCA_002180045.3              Primary Assembly
