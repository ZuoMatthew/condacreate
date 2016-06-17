from __future__ import absolute_import, division, print_function

try:
    from subprocess import check_output
except ImportError:
    import subprocess
    def check_output(*popenargs, **kwargs):
        """Backported from Python 2.7 as it's implemented as pure python on stdlib."""

        process = subprocess.Popen(stdout=subprocess.PIPE, *popenargs, **kwargs)
        output, unused_err = process.communicate()
        retcode = process.poll()
        if retcode:
            cmd = kwargs.get("args")
            if cmd is None:
                cmd = popenargs[0]
            error = subprocess.CalledProcessError(retcode, cmd)
            error.output = output
            raise error
        return output


def shell_out(cmd=None, **kwargs):
    """
    Thin layer on check_output to return data as strings

    Parameters
    ----------
    cmd : list
        command to run
    kwargs:
        passed directly to check_output

    Returns
    -------
    result : str
        result of shell command
    """
    return check_output(cmd, **kwargs).decode('utf-8')
