#puppet manifest to set higher the ulimit for mginx server
exec {'set_nginx_ulimit':
  command => '/bin/sed -t "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin:/bin/',

}

exec {'nginx-restart':
  command => '/etc/init.d/nginx restart',
  path    => '/etc/init.d',
}
