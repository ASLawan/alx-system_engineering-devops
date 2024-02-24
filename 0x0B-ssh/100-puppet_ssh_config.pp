# Configure shh client to use private key for authentication
exec { 'echo':
  path    => 'usr/bin:/bin',
  command => 'echo "  IdentityFile ~/.shh/school\n  PasswordAuthentication no" >> /etc/ssh/shh_config',
  returns => [0, 1],
}
