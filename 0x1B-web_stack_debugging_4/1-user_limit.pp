#set holberton user file limit 
exec {'set_holberton_user_hard_file_limit':
  command => 'sed -i "/^holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

exec {'set_holberton_user_soft_file_limit':
  command => 'sed -i "/^holberton soft/s/4/50000/" /etc/security.limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
