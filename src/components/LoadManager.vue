<template>
  <v-container>
    <v-row>
      <v-col cols="12" >
   
        <v-data-table
            :headers="headers"
            :items="items"
            sort-by="Дата"
            class="elevation-1"
        >
          <template v-slot:top>
            <v-toolbar flat color="white">
              <v-toolbar-title>Журнал загрузок</v-toolbar-title>
              <v-divider
                class="mx-4"
                inset
                vertical
              ></v-divider>
              <v-spacer></v-spacer>
              <v-dialog v-model="dialog" persistent max-width="500px">
                <template v-slot:activator="{ on }">
                  <v-btn color="primary" dark class="mb-2" v-on="on">
                      <v-icon>mdi-plus</v-icon>
                  </v-btn>
                </template>
                <v-card>
                  <v-card-title>
                    <span class="headline">{{ formTitle }}</span>
                  </v-card-title>

                  <v-card-text>
                    <v-container>
                      <v-row>        
                        <v-overlay
                          :absolute="true"
                          :opacity="0.46"
                          :value="overlay"  
                          :z-index="5"
                        >
                          <v-progress-circular
                            indeterminate
                            color="purple"
                          ></v-progress-circular>
                        </v-overlay>                  
                        <v-col class="d-flex" cols="12" >
                          <v-select
                            v-model="defaultItem.select"
                            :items="defaultItem.types"
                            item-text="name"
                            item-value="id"
                            label="Тип загрузки"
                          ></v-select>
                        </v-col>
                      </v-row>
                      <v-row>                        
                        <v-col class="d-flex" cols="12" >
                          <v-file-input v-model="defaultItem.file" show-size label="Файл"></v-file-input>
                        </v-col>
                      </v-row>
                    </v-container>
                  </v-card-text>

                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="blue darken-1" text @click="close">Отмена</v-btn>
                    <v-btn color="blue darken-1" text @click="save">Сохранить</v-btn>
                  </v-card-actions>
                </v-card>
              </v-dialog>
            </v-toolbar>
          </template>
        <template v-slot:no-data>
            Журнал пуст
        </template>
        </v-data-table>
      </v-col>
    </v-row>
  </v-container>

</template>

<script>
  export default {
    data: () => ({
      dialog: false,
      headers: [
        { text: 'Дата', align: 'left', value: 'created' } ,
        { text: 'Имя файла', value: 'file_name' },
        { text: 'Тип', value: 'type.name' },
        { text: 'Статус', value: 'status.name' },
        // { text: 'Файл', value: 'action', sortable: false },
      ],
      editedIndex: -1,
      editedItem: {
        file: {},
        type: 1,
      },
      overlay: false,
    }),

    computed: {
      formTitle () {
        return this.editedIndex === -1 ? 'New Item' : 'Edit Item'
      },
      items() { return this.$store.getters.load_list },
      defaultItem() { return this.$store.getters.loaderDefaultItem }
    },

    watch: {
      dialog (val) {
        val || this.close()
      },
    },

    created () {
      this.$store.dispatch('loaderLoadRefs')
      this.$store.dispatch('loadLoaderItems')
    },

    methods: {


      close () {
        this.dialog = false
        setTimeout(() => {
          this.$store.commit('closeLoaderModal')
        }, 300)
      },

      async save () {
          this.overlay = true
          await this.$store.dispatch('saveLoadData')
          this.overlay = false
          await this.close()
      },
    },
  }
</script>