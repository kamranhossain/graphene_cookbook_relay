# Graphene Cookbook Relay

Example Application with  graphene_django and relay with reformatting structure.
This repo is the walkthrough in the docs of graphene_django with relay. Its also have filtering capacities. There are some typos on docs and some deprecated codes. All these things fixed in this repo. So please follow the docs and this repo to make your code error free.

### Setup Steps

1. git clone https://github.com/kamranhossain/graphene_cookbook_relay.git
2. cd graphene_cookbook
3. virtualenv venv
4. source venv/bin/activate
5. pip install -Ur requirments/base.txt
6. python manage.py makemigrations
7. python manage.py migrate
8. python manage.py createsuperuser
9. python manage.py runserver
10. Go to localhost:8000/graphql and type your first query!
```graphql
query {
  allIngredients {
    edges {
      node {
        id,
        name
      }
    }
  }
}
```


11. The above will return the names & IDs for all ingredients. But perhaps you want a specific ingredient:
```graphql
query {
  # Graphene creates globally unique IDs for all objects.
  # You may need to copy this value from the results of the first query
  ingredient(id: "SW5ncmVkaWVudE5vZGU6MQ==") {
    name
  }
}
```
12. You can also get each ingredient for each category:

```graphql
query {
  allCategories {
    edges {
      node {
        name,
        ingredients {
          edges {
            node {
              name
            }
          }
        }
      }
    }
  }
}
```

13. Or you can get only ‘meat’ ingredients containing the letter ‘e’:

```graphql
query {
  # You can also use `category: "CATEGORY GLOBAL ID"`
  allIngredients(name_Icontains: "e", category_Name: "Meat") {
    edges {
      node {
        name
      }
    }
  }
}
```


