Name:    xcpsign-macros-test
Version: 1.0
Release: 0.cop.1.0.cop1.1%{dist}
Summary: Local signing macros for XCP-ng kernel build testing
License: MIT
BuildArch: noarch

# this is a DEV package containing TEST/DEV keys, this should never be use in production 
# No dependencies, sbsign is pulled in by the kernel spec itself
# or pre-installed in the build container.

Source0:  macros.xcpsign
Source1:  fetchcert
Source2:  xcpsign
Source3:  LINUX_SIGN_KEY_XCP9.key
Source4:  LINUX_SIGN_KEY_XCP9.crt
Source5:  LINUX_SIGN_KEY_XCP9.cer
Source6:  GRUB_SIGN_KEY_XCP9.key
Source7:  GRUB_SIGN_KEY_XCP9.crt
Source8:  GRUB_SIGN_KEY_XCP9.cer
Source9:  XEN_SIGN_KEY_XCP9.key
Source10: XEN_SIGN_KEY_XCP9.crt
Source11: XEN_SIGN_KEY_XCP9.cer
Source12: LINUX_EXT_SIGN_KEY_XCP9.key
Source13: LINUX_EXT_SIGN_KEY_XCP9.crt
Source14: LINUX_EXT_SIGN_KEY_XCP9.cer
Source15: LINUX_THIRD_PARTY_SIGN_KEY_XCP9.key
Source16: LINUX_THIRD_PARTY_SIGN_KEY_XCP9.crt
Source17: LINUX_THIRD_PARTY_SIGN_KEY_XCP9.cer
Source18: SHIM_SIGN_KEY_XCP9.key
Source19: SHIM_SIGN_KEY_XCP9.crt
Source20: SHIM_SIGN_KEY_XCP9.cer
Source21: SHIM_EMBEDDED_SIGN_KEY_XCP9.key
Source22: SHIM_EMBEDDED_SIGN_KEY_XCP9.crt
Source23: SHIM_EMBEDDED_SIGN_KEY_XCP9.cer

%description
Local replacement for the production xcpsign-macros package.
Provides %%fetchcert and %%sign RPM macros that use locally stored
test keys instead of the production signing service.


%install
install -D -m 644 %{_sourcedir}/macros.xcpsign \
    %{buildroot}%{_rpmmacrodir}/macros.xcpsign

install -D -m 755 %{_sourcedir}/fetchcert \
    %{buildroot}/usr/local/bin/fetchcert

install -D -m 755 %{_sourcedir}/xcpsign \
    %{buildroot}/usr/local/bin/xcpsign

# Install the test keys into the default keystore path
%define keystore /etc/xcpsign/keys
install -d -m 755 %{buildroot}%{keystore}

for KEYNAME in \
    LINUX_SIGN_KEY_XCP9 \
    GRUB_SIGN_KEY_XCP9 \
    XEN_SIGN_KEY_XCP9 \
    LINUX_EXT_SIGN_KEY_XCP9 \
    LINUX_THIRD_PARTY_SIGN_KEY_XCP9 \
    SHIM_SIGN_KEY_XCP9 \
    SHIM_EMBEDDED_SIGN_KEY_XCP9
do
    install -m 644 %{_sourcedir}/$KEYNAME.key  %{buildroot}%{keystore}/
    install -m 644 %{_sourcedir}/$KEYNAME.crt  %{buildroot}%{keystore}/
    install -m 644 %{_sourcedir}/$KEYNAME.cer  %{buildroot}%{keystore}/
done

%files
%{_rpmmacrodir}/macros.xcpsign
/usr/local/bin/fetchcert
/usr/local/bin/xcpsign
%dir /etc/xcpsign/
%dir /etc/xcpsign/keys/
/etc/xcpsign/keys/*.key
/etc/xcpsign/keys/*.crt
/etc/xcpsign/keys/*.cer

%changelog
* Fri Jun 05 2026 Oparowski Corentin <corentin.oparowski@vates.tech> - 1.0-0.cop.1
- xcpsign-macros-test for dev secureboot testing