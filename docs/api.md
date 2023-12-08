# API Layout & Verbs

## V1 of the API

* `/api/v1/`
  * `GET` (A list of endpoints)
* `/api/v1/schema/`
  * `GET` (Maybe...)

### Accounts

* `/api/v1/accounts/login/`
  * `POST`
* `/api/v1/accounts/signup/`
  * `POST`
* `/api/v1/accounts/reset_password/`
  * `POST`
* `/api/v1/accounts/logout/`
  * `POST`

### Teams

* `/api/v1/teams/`
  * `GET`
  * `POST` (Create team)
* `/api/v1/teams/:pk/`
  * `GET`
  * `PUT`
  * `DELETE`
* `/api/v1/teams/:pk/members/`
  * `GET`
  * `POST`
* `/api/v1/teams/:pk/members/:pk/`
  * `GET`
  * `PUT`
  * `DELETE`
* `/api/v1/teams/:pk/invites/`
  * `GET`
  * `POST` (Create invite)
* `/api/v1/teams/:pk/invites/:pk/`
  * `GET`
  * `POST` (Accept invite)

### Competitions

* `/api/v1/competitions/`
  * `GET`
* `/api/v1/competitions/:pk/`
  * `GET`
* `/api/v1/competitions/:pk/commits/`
  * `GET` (Stream of commits - maybe websockets?)
* `/api/v1/competitions/:pk/entries/`
  * `GET`
  * `POST` (Create entry)
* `/api/v1/competitions/:pk/entries/:pk/`
  * `GET`
  * `PUT`
  * `DELETE`
* `/api/v1/competitions/:pk/sponsors/`
  * `GET`
* `/api/v1/competitions/:pk/results/`
  * `GET`
* `/api/v1/competitions/:pk/results/:pk/`
  * `GET`
