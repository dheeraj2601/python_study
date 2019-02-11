import subprocess

cmd = 'grep -nrw %s * | grep -v "script_find_unused_api.py" '
count = 'grep -nrw %s * | grep -v "script_find_unused_api.py" | wc -l'

tupleA = ("timers_set_sdkapi",
          "bgp_timers_unset_sdkapi"
         )

with open ('list1.txt', 'w') as f:
  for i in tupleA:
    f.write ('%s %s\n' % ("API : ", i))
    f.write ( "       ---------------\n")
    f.write (subprocess.check_output (cmd % (i), shell=True))
    f.write ('%s %s' % ("count : ", subprocess.check_output (count % (i), shell=True)))
    f.write ('\n\n')
