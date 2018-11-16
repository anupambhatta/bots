#!/usr/bin/env python
import sys
import os
import botsinit
import botsglobal


def start():
    # NOTE: bots directory should always be on PYTHONPATH - otherwise it will not start.
    # ***command line arguments**************************
    usage = '''
    This is "%(name)s", developed by Jagged Peak Inc.
    A utility to read a plugin. Enter a comma separated list of plugin files.
    Usage:
        %(name)s -c<config_directory> -d<plugin_directory> <pluginfile(s)>
    Options:
        -c<directory>   directory for configuration files (default: config).
        -d<directory>   directory for plugin file(s) default: D:/BOTS/plugins
        
    ''' % {'name': os.path.basename(sys.argv[0]), 'version': botsglobal.version}

    configdir = 'config'
    plugindir = 'D:/BOTS/plugins'
    pluginfiles = ''

    # Handle cmd arguments
    for arg in sys.argv[1:]:
        if arg.startswith('-c'):
            configdir = arg[2:]
            if not configdir:
                print 'Error: configuration directory indicated, but no directory name.'
                sys.exit(1)
            if arg.startswith('-d'):
                plugindir = arg[2:]
            if not configdir:
                print 'Error: plugin directory indicated, but no directory name.'
                sys.exit(1)
        else:
            pluginfiles = arg

    if not pluginfiles:
        print 'Plugin file was not entered. See usage'
        print usage
        sys.exit(1)

    # Init required vars and libs
    botsinit.generalinit(configdir)  # find locating of bots, configfiles, init paths etc.
    process_name = 'plug_read'
    botsglobal.logger = botsinit.initserverlogging(process_name)
    import pluglib  # import here, import at start of file gives error; first initialize.

    # Call read plugin for each file
    pluginfiles_list = pluginfiles.split(',')
    for pluginfile in pluginfiles_list:
        plugin_file_path = os.path.join(plugindir, pluginfile)
        pluglib.read_plugin(plugin_file_path)


if __name__ == '__main__':
    start()
