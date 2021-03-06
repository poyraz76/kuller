#!/bin/bash 
#
# Prelink wrapper script
# Author: Andres Roldan <aroldan@debian.org>

# Needed to avoid annoying message in coreutils >= 6.0
export LC_ALL='C'

# Recommended minimun free space, 50MB
min_size=50000

will_prelink="$(for i in $(awk '! /#/ && ! /^-b/ && NF >= 1 {print $NF}' < /etc/prelink.conf); do test -e "$i" && echo "$i"; done)"
have_warn=0

df -P $will_prelink | sort | uniq | {
    have_warn=0
    while read part x x size x mount_point; do
	if $(echo $part | grep -qv "^/"); then
	    continue;
	fi

	if [ $size -le "$min_size" ]; then
	    echo "Partition $part ($mount_point) has only $size KB free." >&2
	    have_warn=1
	fi
    done
    
    exit $have_warn     # Exit from piped subshell
}

if [ "$?" -eq "1" ]; then
    answer="No"
    echo
    echo "!! WARNING !!"
    echo "It's recommended to have at least $min_size KB of disk space."
    echo "Prelink would _really_ damage the ELF files on those partitions."
    read -t 20 -p "Do you really want to run prelink? (yes/No): " answer
    
    if [ "$answer" = "yes" ]; then
	echo "You were warned. Running prelink..."
	exec /usr/sbin/prelink.bin "$@"
    else
	echo
	echo "Aborting prelink."
	exit 1
    fi
fi >&2

exec /usr/sbin/prelink.bin "$@"

