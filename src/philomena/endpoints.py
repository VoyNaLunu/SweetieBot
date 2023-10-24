from collections import namedtuple

Endpoint = namedtuple("Endpoint", "method path")

endpoints = {
  "comments": Endpoint("GET", "/api/v1/json/comments/"),
  "images": Endpoint("GET", "/api/v1/json/images/"),
  "post_images": Endpoint("POST", "/api/v1/json/images/"),
  "featured_images": Endpoint("GET", "/api/v1/json/images/featured/"),
  "tags": Endpoint("GET", "/api/v1/json/tags/"),
  "posts": Endpoint("GET", "/api/v1/json/posts/"),
  "profiles": Endpoint("GET", "/api/v1/json/profiles/"),
  "filters": Endpoint("GET", "/api/v1/json/filters/"),
  "system_filters": Endpoint("GET", "/api/v1/json/filters/system/"),
  "user_filters": Endpoint("GET", "/api/v1/json/filters/user"),
  "oembed": Endpoint("GET", "/api/v1/json/oembed/"),
  "search_comments": Endpoint("GET", "/api/v1/json/search/comments/"),
  "search_galleries": Endpoint("GET", "/api/v1/json/search/galleries/"),
  "search_posts": Endpoint("GET", "/api/v1/json/search/posts/"),
  "search_images": Endpoint("GET", "/api/v1/json/search/images/"),
  "search_tags": Endpoint("GET", "/api/v1/json/search/tags/"),
  "search_reverse": Endpoint("POST", "/api/v1/json/search/reverse/"),
}
