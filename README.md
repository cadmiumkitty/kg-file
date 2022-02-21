# Knowledge Graph Descriptor

Much like [Google Structured Data](https://developers.google.com/search/docs/advanced/structured-data/intro-structured-data) we can place a simple descriptor with a well-known name like `kg.jsonld` into source code repos, crawl the repos, build a part of a knowledge graph and federate across other parts of the knowledge graph built with, for example, Confluence content using [Taxonomies for Confluence add-on](https://marketplace.atlassian.com/1226218).

Alternatively, contents of `kg.jsonld` can simply be pushed via [SPARQL 1.1 Graph Store HTTP Protocol](https://www.w3.org/TR/sparql11-http-rdf-update/) to a graph store via Github Actions or Bitbucket Pipelines.

Another alternative is Bitbucket webhooks, so it is possible to build a single knowledge graph ecosystem around Atlassian tool set.

## Terms

Only two terms are used to describe resources - `dcterms:type` and `dcterms:subject` from [Dublin Core Metadata Terms](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/). Type can be a concept from [SDLC Document Types Taxonomy](https://github.com/cadmiumkitty/sdlc-document-types-taxonomy) or from an other scheme that may be organisation-specific. Subject can be a concept referencing a system, component, service, or anything else from an organization-specific scheme.

## Example

Simplest case of specifying type and subject of a single `README` file and using remote context hosted in this repo:

```
{
  "@context": "https://raw.githubusercontent.com/cadmiumkitty/kg-file/main/kgcontext.jsonld",
  "@graph": [
    {
      "@id": "README.md",
      "type": "https://dalstonsemantics.com/taxonomy/sdlc/readme",
      "subject": "https://dalstonsemantics.com/service/thingymabob"
    }
  ]
}
```

## Alternative in Yaml

A case can be made for something even simpler that will be translated by the crawler/action/pipeline/webhook processor:

```
README.md:
  type: https://dalstonsemantics.com/taxonomy/sdlc/readme
  subject: https://dalstonsemantics.com/service/thingymabob
```