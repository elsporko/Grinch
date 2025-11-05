from k_means_constrained import KMeansConstrained
from django.db.models.query import QuerySet
from django.db import transaction
from .models import PickList
from route.models import Route
import numpy as np
import pandas as pd

def get_route_clusters(num_clusters: int, picklist: QuerySet[PickList])-> dict:
        TOLERANCE : int = 2 # Set the  acceptable off by for number of clusters

        data = pd.DataFrame(list(picklist.values('order_id','lat', 'lon')))
        #print (f"data: {data}")
        #convert queryset to dataframe
        features = data[['lat', 'lon']]
        X = np.array(features)
        print(f'size X: {len(X)}')
        print(f'size_maximum: {num_clusters + TOLERANCE}')
        print(f'size_minimum: {num_clusters - TOLERANCE}')

        print(f'~~~~~~~~ num_clusters: {num_clusters}')

        clf = KMeansConstrained(
            n_clusters=num_clusters,
            size_min=(len(X)/num_clusters) - TOLERANCE,
            size_max=(len(X)/num_clusters) + TOLERANCE,
            random_state=0
        )
        clf.fit_predict(X)
        labels = clf.labels_

        #send bat into dataframe and display it
        data['cluster'] = labels
        return data[['order_id', 'lat', 'lon', 'cluster']].to_dict(orient='records')
        #display the number of members in each clustering
        #_clusters = data.groupby('cluster')['no'].count()

def assign_route_data_service()->None:
    routes = list(Route.objects.exclude(active=False))
    picklist = PickList.objects.exclude(lat=0.0).exclude(lon=0.0)#.values('order_id','lat', 'lon')
    print(f"routes: {list(routes)}")
    route_data = get_route_clusters(len(routes), picklist)

    cluster_route_map = {i: routes[i] for i in range(len(routes))}
    order_id_picklist_map = {pick.order_id: pick for pick in list(picklist)}
    print(f'order_id_picklist_map: {order_id_picklist_map}')

    for data in route_data:
          pick = order_id_picklist_map.get(data['order_id'])
          pick.route = cluster_route_map.get(data['cluster'])

    with transaction.atomic():
          PickList.objects.bulk_update(order_id_picklist_map.values(), ['route'])
    return route_data