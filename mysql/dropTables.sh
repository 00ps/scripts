#!/bin/sh
if [ -z "$1" ]
then
        echo -e "**************************\n" 
        echo -e " Missing database name!! \n Script usage:\n $0 [database]\n"
        echo -e "**************************\n"
        exit 1
fi
if [ ! -f ~/.my.cnf ]
then
	echo -e "***********************************************************"
	echo -e "This script requires a .my.cnf file in you home directory\n to be able to log on the DB"
	echo -e "***********************************************************"
	exit 1
fi
MYSQL="mysql --defaults-file=~/.my.cnf -D $1"
$MYSQL -BNe "show tables" | awk '{print "set foreign_key_checks=0; drop table `" $1 "`;"}' | $MYSQL
unset MYSQL
