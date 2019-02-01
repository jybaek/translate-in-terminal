#!/bin/sh

pip install -r requirements.txt 1>/dev/null
run_script="${HOME}/bin/.translate"

cat <<EOF >${run_script}
#!/bin/bash

if [ "\$#" != "1" ];then
  echo "Usage: \$0 \"User message\""
  exit 255
fi

python $(pwd)/translatebot.py --comments "\$@" | pbcopy
pbpaste
EOF

if [ -f "${run_script}" ];then
  chmod +x ${run_script}
fi

echo "\n ** Install successed **\n"
echo " Usage: $(basename ${run_script}) \"Write text\"\n"
