#!/bin/bash

curl https://api.tfl.gov.uk/Line/district,northern,piccadilly,central/Disruption 2> /dev/null | jq -r '.[] | .description' > /tmp/tubestatus.out

if [ -s /tmp/tubestatus.out ]
then
  sudo setterm --term linux --blank=poke < /dev/tty1
  printf "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n" > /dev/tty1
  cat /tmp/tubestatus.out | while read line rest
  do
    case "$line" in
      Piccadilly|piccadilly)	fg=white; bg=blue;;
      Central|central)		fg=white; bg=red;;
      Northern|northern)	fg=black; bg=white;;
      District|district)	fg=white; bg=green;;
      *)			fg=white; bg=black;;
    esac
    sudo setterm --term linux --background=$bg --foreground=$fg  < /dev/tty1
    echo "" > /dev/tty1
    echo "$line $rest" > /dev/tty1
    sudo setterm --term linux --background=black --foreground=white < /dev/tty1
  done
  i=1
  while [ "$i" -lt "24" ]
  do
    echo "" > /dev/tty1
    sleep 2
    i=$((i+1))
  done
fi
