#!/bin/bash

setterm --term linux --blank=1 < /dev/tty1
trap "setterm --term linux --cursor on < /dev/tty1 ; exit" 2

curl https://api.tfl.gov.uk/Line/district,northern,piccadilly,central/Disruption 2> /dev/null | jq -r '.[] | .description' > /tmp/tubestatus.out

if [ -s /tmp/tubestatus.out ]
then
  setterm --term linux --blank=poke < /dev/tty1
  setterm --term linux --cursor off < /dev/tty1
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
    setterm --term linux --background=$bg --foreground=$fg  > /dev/tty1
    echo "" > /dev/tty1
    echo "$line $rest" > /dev/tty1
    setterm --term linux --background=black --foreground=white > /dev/tty1
  done
  i=1
  while [ "$i" -lt "31" ]
  do
    echo "" > /dev/tty1
    sleep 2
    i=$((i+1))
  done
fi
setterm --term linux --cursor on < /dev/tty1
