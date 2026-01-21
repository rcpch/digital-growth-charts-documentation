import os
import subprocess


def _repo_root():
    return os.path.abspath(os.path.dirname(__file__))


def _git_live_head():
    try:
        repo_root = _repo_root()
        full_hash = subprocess.check_output(
            ["git", "rev-parse", "live"],
            cwd=repo_root,
            text=True,
        ).strip()
        short_hash = subprocess.check_output(
            ["git", "rev-parse", "--short", "live"],
            cwd=repo_root,
            text=True,
        ).strip()
        if full_hash and short_hash:
            return full_hash, short_hash
    except Exception:
        pass
    return None, None


def define_env(env):
    @env.macro
    def latest_commit_link(path):
        full_hash, short_hash = _git_live_head()
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
