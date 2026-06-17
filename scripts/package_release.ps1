param(
    [string]$OutputDir = "dist"
)

$ErrorActionPreference = "Stop"

$root = Resolve-Path (Join-Path $PSScriptRoot "..")
$outputPath = Join-Path $root $OutputDir
$packageRoot = Join-Path $outputPath "wiki-llm-starter"
$zipPath = Join-Path $outputPath "wiki-llm-starter.zip"

function Assert-InsideRoot {
    param(
        [string]$PathToCheck,
        [string]$AllowedRoot
    )

    $fullPath = [System.IO.Path]::GetFullPath($PathToCheck)
    $fullRoot = [System.IO.Path]::GetFullPath($AllowedRoot)
    if (-not $fullPath.StartsWith($fullRoot, [System.StringComparison]::OrdinalIgnoreCase)) {
        throw "Refusing to operate outside output directory: $fullPath"
    }
}

Assert-InsideRoot -PathToCheck $packageRoot -AllowedRoot $outputPath
Assert-InsideRoot -PathToCheck $zipPath -AllowedRoot $outputPath

if (Test-Path -LiteralPath $packageRoot) {
    Remove-Item -LiteralPath $packageRoot -Recurse -Force
}

New-Item -ItemType Directory -Path $packageRoot | Out-Null

Copy-Item -LiteralPath (Join-Path $root "START_HERE.ko.md") -Destination (Join-Path $packageRoot "START_HERE.ko.md")
Copy-Item -LiteralPath (Join-Path $root "CLAUDE.md") -Destination (Join-Path $packageRoot "CLAUDE.md")

New-Item -ItemType Directory -Path (Join-Path $packageRoot "docs") | Out-Null
$docs = @(
    "acceptance-checklist.ko.md",
    "deployment.ko.md",
    "life-application-guide.ko.md",
    "llm-wiki-rules.ko.md",
    "ontology-guide.ko.md",
    "skill-routing.ko.md",
    "user-manual.ko.md",
    "vibe-coding-operation-strategy.ko.md"
)
foreach ($doc in $docs) {
    Copy-Item -LiteralPath (Join-Path $root "docs\$doc") -Destination (Join-Path $packageRoot "docs\$doc")
}

New-Item -ItemType Directory -Path (Join-Path $packageRoot "scripts") | Out-Null
$scripts = @(
    "lint_wiki.py",
    "ontology_reasoner.py",
    "package_release.ps1"
)
foreach ($script in $scripts) {
    Copy-Item -LiteralPath (Join-Path $root "scripts\$script") -Destination (Join-Path $packageRoot "scripts\$script")
}

Copy-Item -LiteralPath (Join-Path $root "templates") -Destination (Join-Path $packageRoot "templates") -Recurse

New-Item -ItemType Directory -Path (Join-Path $packageRoot ".agents") | Out-Null
Copy-Item -LiteralPath (Join-Path $root ".agents\skills") -Destination (Join-Path $packageRoot ".agents\skills") -Recurse

New-Item -ItemType Directory -Path (Join-Path $packageRoot ".codex") | Out-Null
Copy-Item -LiteralPath (Join-Path $root ".codex\skills") -Destination (Join-Path $packageRoot ".codex\skills") -Recurse

if (Test-Path -LiteralPath $zipPath) {
    Remove-Item -LiteralPath $zipPath -Force
}

Compress-Archive -LiteralPath $packageRoot -DestinationPath $zipPath

Write-Host "Created package: $zipPath"
