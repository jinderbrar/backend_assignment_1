# Backend Assignment Task

This repository contain the **Bitespeed Backend Task Identity Reconciliation**

## NOTE:
- Code is implemented in Python and Django web framework is used
- For the simplicity purpose *sqlite* database have used with is the default for django.


## RESUME : [Harjinder_Singh__Resume](https://drive.google.com/file/d/1g3_yBQDdc7AwR2qbq34BR1hLCflRMxTK/view)

## Default Setup
I have added a default database entries that can help. Below is the default data that you will find in sqlite table.

| id | email                    | phone_number | link_precedence | created_at                 | updated_at                 | deleted_at | linked_id_id  |   |   |
|----|--------------------------|--------------|-----------------|----------------------------|----------------------------|------------|---------------|---|---|
| 1  | lorraine@hillvalley.edu  | 123456       | primary         | 2023-06-19 10:22:18.792741 | 2023-06-19 10:22:18.792843 | null       | null          |   |   |
| 2  | mcfly@hillvalley.edu     | 123456       | secondary       | 2023-06-19 10:22:19.152725 | 2023-06-19 10:22:19.152793 | null       | 1             |   |   |
| 3  | george@hillvalley.edu    | 919191       | primary         | 2023-06-19 10:22:19.292691 | 2023-06-19 10:22:19.292791 | null       | null          |   |   |
| 4  | biffsucks@hillvalley.edu | 717171       | secondary       | 2023-06-19 10:22:19.447645 | 2023-06-19 10:22:19.447718 | null       | 3             |   |   |



## HOW TO RUN

Web server will be running at port `8000` make sure its free. To run start the docker container with `docker-compose up -d`

## Example Curl
- only email
  - `curl --location 'localhost:8000/identify' --form 'email="lorraine@hillvalley.edu"'`
- only phoneNumber
  - `curl --location 'localhost:8000/identify' --form 'phoneNumber="123456"'`
- both email and phone number
  - `curl --location 'localhost:8000/identify' --form 'email="george@hillvalley.edu"' --form 'phoneNumber="919191"'`

<hr>

### Contact info

**Email** : hjbrar7@gmail.com

**Linkedin** : [jinderbrar](https://linkedin.com/in/jinderbrar)

**Github** : [jinderbrar](https://github.com/jinderbrar)

