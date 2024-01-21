# Ensure Python and pip3 are installed
package { 'python3':
  ensure => installed,
}

package { 'python3-pip':
  ensure => installed,
  require => Package['python3'],
}

# Install the compatible version of Werkzeug
exec { 'install-werkzeug':
  command => '/usr/bin/pip3 install Werkzeug==2.0.1',
  unless  => '/usr/bin/pip3 freeze | grep Werkzeug==2.0.1',
  path    => ['/usr/bin', '/bin', '/usr/sbin', '/sbin'],
  require => Package['python3-pip'],
}

# Install Flask version 2.1.0
exec { 'install-flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  unless  => '/usr/bin/pip3 freeze | grep Flask==2.1.0',
  path    => ['/usr/bin', '/bin', '/usr/sbin', '/sbin'],
  require => Exec['install-werkzeug'],
}

