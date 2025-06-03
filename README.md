# Amooba - Primitive Organism Simulation

### About

This program aims to simulate the survival of organisms in a virtual environment. 
Although it is currently only simulating extremely basic factors, it can easily be modified to include other biological functions.

So how does this work? 

### Software used

**Python** for literally almost everything
**MongoDB** for the database

### Running the program

If you look at the root directory, you'll see that it's subdivided as follows.

```
/-|
  |- @amooba
  |- @dev
  |- @intervention
  |- db
```

Each of these directories serves its own purpose, as you will soon see.

`db` - contains database excecutables, the mongodb data directory, and a small script for starting up the database
`@intervention` - After running the program once, it is usually necessary to wipe the database and start over. I recommend using a backup instead of running these scripts, since the former is significantly faster. But if you want to build the database from the ground up, or modify it in some way, these will be greatly useful, if only as templates for something bigger.
`@dev` - contains database backups (you should use initial_db_6_1002001_**parentkeypresent**_90 - 6 organisms, 1002001 places the organisms can be, presence of a parent key which is necessary to work with the code and a base energy value of 90) and notes/figures
`@amooba` - If you simply wish to run the program, all you need to do is run `start.py [arguments]`. It then excecutes `amooba.py`, which creates a seperate instance of an organism *and imports the rest of the files present in the directory as modules*.

There are two ways you can run `start.py`. 
The first is to run `start.py --all` which will start an instance of every *pre-existing* organism in the database. This means if your initial database looks like this:

```
{ "_id" : 0, "energy" : 20 }
{ "_id" : 1, "energy" : 90, "parent" : "amooba0" }
{ "_id" : 2, "energy" : 90, "parent" : "amooba1" }
{ "_id" : 3, "energy" : 90, "parent" : "amooba2" }
{ "_id" : 4, "energy" : 90, "parent" : "amooba3" }
{ "_id" : 5, "energy" : 90, "parent" : "amooba4" }
```

Organisms with IDs 1-5 will start with their own instances (each running as it's own program and occupying it's own memory space) and their own connections to the database. Note that while organism 0 does not start, it is *required* for the program to run properly (because it's the parent of organism 1, and every organism must have a parent so it doesn't eat its parent, or get eaten by its parent).

It is also possible to run `start.py --one [id]` which starts an instance of the organism with that id.

Actually, `start.py --all` runs `start.py --one [id]` repeatedly, iterating through values of `[id]` based on what's there in the database.



### System limits
### Experimentable values
### Expected errors
### Interesting experiments and results
