# Art Factory incoming artifacts

Temporary, unreviewed source images and extracted PNGs produced by OpenTeam are uploaded under this directory.

- `art/incoming/<run-id>/<stage>/...` is staging space, **not** approved art.
- `art/queue.json` remains authoritative for the four required asset paths, canvas sizes and ground anchors.
- Only the final UPLOADER acceptance can replace files under `public/art/` and change asset status to `approved`.
- Art Factory uses GitHub links to hand off files; do not paste credentials or tokens into agent prompts or this repository.
