# Models

```
BaseModel:
  # Database UID
  id: int
  
  # Entry create date timestamp
  dt_create: datetime


Release:
  # Name of the album
  name: str

  # Release date of the record
  dt_release: datetime 

  # Artist's/band's name
  artist: str

  # Release genres
  genres: list[str]

  # Release type (Album or EP)
  type: str

  # Wheter the user has listened to the release or not
  status_listened: bool

  # If listened, the date in which the user listened to the album
  listened_date: datetime
```
# Tables
*SQLite specific due to data type constraints*

| release |  |            |        |      |                 |               | 
|  -  |   -  | -          | -      | -    | -               | -             | 
| id  | name | dt_release | artist | type | status_listened | listened_date | 
| INTEGER | TEXT | TEXT | TEXT | INTEGER | INTEGER | TEXT |


| genre | |
| - | - |
| id | id_release |
| INTEGER | INTEGER |

# CLI

## Stories

- The user can:
  - use the CLI with arguments to create, search, updatea and delete record entries.
  - use the CLI without arguments, in that case, a menu will appear for navigation.
  - provide a RYM URL to add a release automatically (web scrape).

- Options:
  - --list
    - all -> Lists all releases
    - listened -> Lists all releases with `status_listened` marked as `true`
    - pending -> Lists all releases with `status_listened` marked as `false`
    - (Plans on adding a query option)
  - --find
    - artist -> (ID number or name) Lists all releases of artist
    - release -> (ID number or name) Lists the release 
  - --add
    - release_name, dt_release, artist_name, genres, type -> Saves the release
    - Any argument from above example missing -> Warns the user of blank fields
    - URL -> If it's RYM URL, scrapes it and then saves the release
    - Nothing -> Asks the user for each field
  - --delete
    - id -> Asks the user for confirmation, then deletes release entry
    - release -> Asks the user for confirmation, then deletes release entry
    - artist -> List artist's releases, then user selects which one it wants to delete, asks the user for confirmation, then deletes release entry
  - --update
    - id -> Show release entry, then asks for what field to update
    - release -> Show release entry, then asks for what field to update