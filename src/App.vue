<template>
  <v-app id="inspire">
    <v-navigation-drawer
      v-model="drawer"
      app
    >
      <v-list dense>
        <router-link to="/" >
          <v-list-item link>
            <v-list-item-action>
              <v-icon>mdi-home</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Главная</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </router-link>
        <router-link to="/agreement" >
          <v-list-item link>
            <v-list-item-action>
              <v-icon>mdi-clipboard-outline</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Список дел</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </router-link>
        <router-link to="/load-manager" >
          <v-list-item link>
            <v-list-item-action>
              <v-icon>mdi-plus</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Загрузки</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </router-link>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar
      app
      color="indigo"
      dark
      dense
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-toolbar-title>LCG</v-toolbar-title>

      
    </v-app-bar>

    <v-content>
      <v-container
        fluid
        align="start"
        justify="start"
      >
        <v-row
          align="start"
          justify="start"
        >
          <router-view/>
        </v-row>
      </v-container>
    </v-content>
    <!-- <v-footer
      color="indigo"
      app
    >
      <span class="white--text">&copy; 2019</span>
    </v-footer> -->
  </v-app>
</template>

<script>
  export default {
    props: {
      source: String,
    },
    data: () => ({
      drawer: null,
    }),
  }
</script>

<style>
  a{
    text-decoration: none;
  }
</style>