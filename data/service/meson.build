prefixdir = get_option('prefix')
userunitdir = prefixdir / 'lib/systemd/user'
libexecdir = prefixdir / get_option('libexecdir')
summary(
    {
        'prefixdir': prefixdir,
        'userunitdir': userunitdir,
        'libexecdir': libexecdir
    },
)

# Configure and install Systemd service file
configure_file(
    input: 'yumex-updater.service.in',
    output: 'yumex-updater.service',
    configuration: configuration_data(
        {
            'LIBEXECDIR': libexecdir,
        },
    ),
    install: true,
    install_dir: userunitdir,
)
