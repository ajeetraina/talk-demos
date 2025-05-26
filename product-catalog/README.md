## Demonstrating Product Catalog Workshop

```
git clone https://github.com/dockersamples/catalog-service-node
```

## Change to directory

```
cd catalog-service-node
```

## Initial Setup

```
cd demo/sdlc-e2e
./setup.sh
```

You will see the following result:

```
./setup.sh
==> Setting up branch a demo branch named demo-20250302-ajeetsraina
Switched to a new branch 'temp'
Deleted branch main (was 22b87e4).
branch 'main' set up to track 'origin/main'.
Switched to a new branch 'main'
Deleted branch temp (was 22b87e4).
Already up to date.
Switched to a new branch 'demo-20250302-ajeetsraina'
==> Applying patch and creating a commit
[demo-20250302-ajeetsraina dbd80f5] Demo prep
 4 files changed, 141 insertions(+), 378 deletions(-)
==> Installing npm dependencies
npm warn deprecated inflight@1.0.6: This module is not supported, and leaks memory. Do not use it. Check out lru-cache if you want a good and tested way to coalesce async requests by a key value, which is much more comprehensive and powerful.
npm warn deprecated glob@7.2.3: Glob versions prior to v9 are no longer supported

> container-supported-development@1.0.0 prepare
> husky install

husky - Git hooks installed

added 658 packages, and audited 659 packages in 11s

85 packages are looking for funding
  run `npm fund` for details

8 vulnerabilities (3 low, 1 moderate, 4 high)

To address issues that do not require attention, run:
  npm audit fix

To address all issues, run:
  npm audit fix --force

Run `npm audit` for details.
==> Downloading container images
[+] Pulling 52/52
 ✔ mock-inventory Pulled                                                                                                                                                             27.7s
 ✔ demo-client Pulled                                                                                                                                                                 2.1s
 ✔ postgres Pulled                                                                                                                                                                   24.8s
 ✔ pgadmin Pulled                                                                                                                                                                    33.8s
 ✔ aws Pulled                                                                                                                                                                         3.8s
 ✔ kafka-ui Pulled                                                                                                                                                                   33.0s
 ✔ kafka Pulled                                                                                                                                                                       3.8s






==> Deleting postgres:17.2 container image
Error response from daemon: No such image: postgres:17.2
==> Configuring DBC (if this fails, ask to be added to the dockerdevrel organization)
./setup.sh: line 37: unexpected EOF while looking for matching `"'
./setup.sh: line 39: syntax error: unexpected end of file
➜  sdlc-e2e git:(demo-20250302-ajeetsraina)
```


## Bringing up Compose services

```
docker compose up -d
```


<img width="1351" alt="image" src="https://github.com/user-attachments/assets/764cf9ef-e088-4679-b786-d032f5a9b842" />


## Starting the Catalog API

```
npm install
npm run dev
```



<img width="730" alt="image" src="https://github.com/user-attachments/assets/b34a346f-4ade-401e-80fc-6bf328cdad8b" />


## Accessing Kafka

You will find that it misses UPC code:

<img width="1497" alt="image" src="https://github.com/user-attachments/assets/6f1801c1-ef8b-47aa-99aa-d6d89b55ad4c" />

## Adding UPC

Open `ProductService.js` under `/catalog-service-node/src/services` and add upc entry on line 52

Try adding new products and see UPC code gets reflected.

<img width="1221" alt="image" src="https://github.com/user-attachments/assets/d0951acd-0f48-4cb6-b889-4d26aba9886f" />


## Postgres URL

```
postgresql://postgres:postgres@host.docker.internal:5432/catalog
```

