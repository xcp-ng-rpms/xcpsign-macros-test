#!/bin/bash
set -e
KEYDIR="$(dirname "$0")"

for KEYNAME in \
    LINUX_SIGN_KEY_XCP9 \
    GRUB_SIGN_KEY_XCP9 \
    XEN_SIGN_KEY_XCP9 \
    LINUX_EXT_SIGN_KEY_XCP9 \
    LINUX_THIRD_PARTY_SIGN_KEY_XCP9 \
    SHIM_SIGN_KEY_XCP9 \
    SHIM_EMBEDDED_SIGN_KEY_XCP9
do
    echo "Generating $KEYNAME..."
    openssl req -new -x509 -newkey rsa:2048 -nodes \
        -keyout "$KEYDIR/$KEYNAME.key" \
        -out    "$KEYDIR/$KEYNAME.crt" \
        -days 3650 \
        -subj "/CN=XCP-ng Local Test - $KEYNAME/"

    # DER format — this is what %fetchcert must output
    openssl x509 \
        -in  "$KEYDIR/$KEYNAME.crt" \
        -out "$KEYDIR/$KEYNAME.cer" \
        -outform DER

    echo "  → $KEYNAME.key / .crt / .cer"
done
echo "Done."
