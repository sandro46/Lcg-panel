<template>
  <v-container>
    <v-row>
      <!-- <v-col cols="2">

        <v-form ref="form">
            <v-text-field
              label="Номер договора"
            ></v-text-field>
        </v-form>
        <v-form ref="form">
            <v-text-field
              label="ИНН"
            ></v-text-field>
        </v-form>        
        <v-form ref="form">
            <v-text-field
              label="Внутр. код"
            ></v-text-field>
        </v-form>

      </v-col> -->
      <v-col cols="12" >
        <v-toolbar flat color="white">
          <v-toolbar-title>Сисок дел</v-toolbar-title>
          <v-divider
            class="mx-4"
            inset
            vertical
          ></v-divider>
          <v-spacer></v-spacer>
          <v-text-field
            v-model="search"
            append-icon="mdi-search"
            label="Поиск"
            single-line
            hide-details
          ></v-text-field>
        </v-toolbar>

        <v-data-table 
          :headers="headers" 
          :items="items"
          :search="search"
          item-key="name" 
          class="elevation-1" 
          :loading="loading" loading-text="Loading... Please wait"
        >

       
          <template v-slot:item.action="{ item }">
              <v-icon
                small
                class="mr-2"
                @click="openItem(item)"
              >
                mdi-arrow-right
                
              </v-icon>
          </template>
        </v-data-table>

      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {




  name: 'Agreement',

  data: () => ({
        search: "",
        headers: [
            { text: 'ID', value: 'id', sortable: false },
            { text: 'Номер договора', value: 'agreement_no', sortable: false },
            { text: 'ИНН', align: 'left', sortable: false, value: 'customer.inn' }, 
            { text: 'Фамилия', value: 'customer.f' },
            { text: 'Имя', value: 'customer.i' },
            { text: 'Отчество', value: 'customer.o' },
            { text: 'Основной долг', value: 'main_debt' },
            {text: 'Actions', value: 'action', sortable: false },
        ],
  }),
  computed: {
    items() { 
      return this.$store.getters.agreement_list(this.search)
    },
    loading() { return this.$store.getters.agreement_loading },
  },

  watch: {
      // call again the method if the route changes
      'search': 'checkSearch'
  },
  
  mounted: async function () {
    await this.$store.dispatch('loadAgreementItems')
  },
  methods:{
    checkSearch() {
      if(this.$store.getters.agreement_list(this.search).length == 0) {
        this.$store.dispatch('searchAgreementByString', this.search)
      }
    },
    openItem(item){
      this.$router.push({ path: `/agreement/${item.id}` }) // -> /agreement/123
    }
  }
};
</script>
