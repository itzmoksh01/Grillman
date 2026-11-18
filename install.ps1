# Grillman installer for Windows PowerShell (NOT yet tested on Windows; please report issues).
# Usage: .\install.ps1 [-Target claude|codex|cursor|gemini|agents|all] [-Project]
param(
  [ValidateSet('claude','codex','cursor','gemini','agents','all')][string]$Target = 'claude',
  [switch]$Project
)
$ErrorActionPreference = 'Stop'
$Src  = Split-Path -Parent $MyInvocation.MyCommand.Path
$Base = if ($Project) { (Get-Location).Path } else { $HOME }

function Put-Skill($dir) {
  New-Item -ItemType Directory -Force -Path $dir | Out-Null
  $dest = Join-Path $dir 'grillman'
  if (Test-Path $dest) { Remove-Item -Recurse -Force $dest }
  Copy-Item -Recurse (Join-Path $Src 'skills\grillman') $dest
  Write-Host "skill   -> $dest"
}
function Put-File($from, $to) {
  New-Item -ItemType Directory -Force -Path (Split-Path -Parent $to) | Out-Null
  Copy-Item $from $to -Force
  Write-Host "command -> $to"
}

$targets = if ($Target -eq 'all') { @('claude','codex','cursor','gemini','agents') } else { @($Target) }
foreach ($t in $targets) {
  switch ($t) {
    'claude' { Put-Skill (Join-Path $Base '.claude\skills'); Put-File (Join-Path $Src 'commands\grillman.md') (Join-Path $Base '.claude\commands\grillman.md') }
    'codex'  { Put-Skill (Join-Path $Base '.codex\skills');  Put-File (Join-Path $Src 'commands\grillman.md') (Join-Path $Base '.codex\prompts\grillman.md') }
    'cursor' { Put-Skill (Join-Path $Base '.cursor\skills'); Put-File (Join-Path $Src 'commands\grillman.md') (Join-Path $Base '.cursor\commands\grillman.md') }
    'gemini' { Put-Skill (Join-Path $Base '.gemini\skills'); Put-File (Join-Path $Src 'commands\grillman.toml') (Join-Path $Base '.gemini\commands\grillman.toml') }
    'agents' { Put-Skill (Join-Path $Base '.agents\skills') }
  }
}
Write-Host 'Done. Restart the agent, then run /grillman with your brief (or attach the files).'
