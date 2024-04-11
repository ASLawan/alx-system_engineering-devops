exec { 'replace_file_extensions':
  command => 'sed -i "s/\.phpp/.php/g" /var/www/html/wp-settings.php',
  path    => ['/bin', '/usr/bin'],
  onlyif  => 'grep -q "\.phpp" /var/www/html/wp-settings.php',
}
