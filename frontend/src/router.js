import Vue from "vue";
import VueRouter from "vue-router";
import { adminRoot } from "./constants/config";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    component: () => import("./views/home"),
  },
  {
    path: "/app",
    component: () => import("./views/app"),
    redirect: `${adminRoot}/main`,
    children: [
      {
        path: 'main',
        component: () => import('./views/app/Main')
      },
      {
        path: 'search/:keyword',
        component: () => import('./views/app/Search')
      },
      {
        path: 'songDetail/:songID',
        component: () => import('./views/app/SongDetail')
      },
      {
        path: 'albumDetail/:albumID',
        component: () => import('./views/app/AlbumDetail')
      },
      {
        path: 'artistDetail/:artistID',
        component: () => import('./views/app/ArtistDetail')
      },
      {
        path: 'profile',
        component: () => import('./views/app/Profile')
      },
    ]
  },
  {
    path: "/error",
    component: () => import("./views/Error")
  },
  {
    path: "*",
    component: () => import("./views/Error")
  },
  
];

const router = new VueRouter({
  linkActiveClass: "active",
  routes,
  mode: "history",
});
export default router;
