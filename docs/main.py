import os
import subprocess

def _repo_root():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

def _git_latest_commit(path):
    try:
        repo_root = _repo_root()
        output = subprocess.check_output(
            [
                "git",
                "log",
                "-n",
                "1",
                "--pretty=format:%H|%h",
                "--",
                path,
            ],
            cwd=repo_root,
            text=True,
        ).strip()
        if "|" in output:
            full_hash, short_hash = output.split("|", 1)
            return full_hash, short_hash
    except Exception:
        pass
    return None, None

def define_env(env):
    @env.macro
    def latest_commit_link(path):
        full_hash, short_hash = _git_latest_commit(path)
        if full_hash and short_hash:
            url = (
                "https://github.com/rcpch/digital-growth-charts-documentation/commit/"
                + full_hash
            )
            return f"[{short_hash}]({url})"
        fallback = (
            "https://github.com/rcpch/digital-growth-charts-documentation/commits/live/"
            + path
        )
        return f"[{path}]({fallback})"
