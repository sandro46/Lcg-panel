<template>
    
  <v-container>
    <v-row>
        <v-col>
            <v-slide-group  show-arrows>
                
                <v-slide-item
                    v-for="tag in tags"
                    :key="tag.id"
                >
                    <v-btn
                        class="mx-2"
                        active-class="purple white--text"
                        depressed
                        rounded
                        @click="openAgreement(tag.id)"
                    >
                        {{ tag.id }}
                    </v-btn>
                </v-slide-item>
            </v-slide-group>
        </v-col>
    </v-row>
      <v-row>
          <v-col>
                <v-card> 
                    <v-simple-table :dense="true">
                        <template v-slot:default>
                            <thead>
                                <tr>
                                    <th class="text-left" colspan=1 >Информация о должнике</th>
                                </tr>
                                <tr>
                                    <td class="text-left" colspan=1 >
                                        
                                    </td>
                                </tr>
                            </thead>
                            <tbody>    
                                <tr>
                                    <td>Фамилия</td>
                                    <td>{{ ('customer' in agreement ? agreement.customer['f'] : '') }}</td>
                                </tr>
                                <tr>
                                    <td>Имя</td>
                                    <td>{{ 'customer' in agreement ? agreement.customer.i : '' }}</td>
                                </tr>
                                <tr>
                                    <td>Отчество</td>
                                    <td>{{ 'customer' in agreement ? agreement.customer.o : '' }}</td>
                                </tr>
                                <tr>
                                    <td>agreement_id</td>
                                    <td>{{ agreement.id }}</td>
                                </tr>
                                <tr>
                                    <td>Контрагент</td>
                                    <td>CCG</td>
                                </tr>
                                <tr>
                                    <td>Номер договора</td>
                                    <td>{{ agreement.agreement_no }}</td>
                                </tr>
                                <tr>
                                    <td>Дата договора</td>
                                    <td>{{ agreement.agreement_from }}</td>
                                </tr>
                            </tbody>
                        </template>
                    </v-simple-table>                
              </v-card> 
          </v-col>
          <v-col>
              <v-card>                
                <v-simple-table :dense="true">
                    <template v-slot:default>
                        <thead>
                            <tr>
                                <th class="text-left" colspan=2 >Информация о долге</th>
                            </tr>
                        </thead>
                        <tbody>    
                            <tr>
                                <td>Текущая сумма задолженности</td>
                                <td>{{ numFormat.format(agreement.current_debt) }}</td>
                            </tr>
                            <tr>
                                <td>Основной долг</td>
                                <td>{{ numFormat.format(agreement.current_main_debt) }}</td>
                            </tr>
                            <tr>
                                <td>Проценты</td>
                                <td>{{ numFormat.format(agreement.current_percent) }}</td>
                            </tr>
                            <tr>
                                <td>Комиссия</td>
                                <td>{{ numFormat.format(agreement.current_commission) }}</td>
                            </tr>
                            <tr>
                                <td>Пеня</td>
                                <td>{{ numFormat.format(agreement.current_penalty) }}</td>
                            </tr>
                            <tr>
                                <td>Штраф за несоблюдение условий</td>
                                <td>{{ numFormat.format(agreement.current_penalty_agreement) }}</td>
                            </tr>
                            <tr>
                                <td>Судебные издержки(гос./пошлина)</td>
                                <td>{{ numFormat.format(agreement.current_court_costs) }}</td>
                            </tr>
                            <tr>
                                <td>Долг на начало</td>
                                <td>{{ numFormat.format(agreement.main_debt +
                                                        agreement.court_costs +
                                                        agreement.percent +
                                                        agreement.commission +
                                                        agreement.penalty) }}</td>
                            </tr>
                            <tr>
                                <td>Сумма платежей</td>
                                <td>{{ numFormat.format(sum_agreement_payments) }}</td>
                            </tr>
                        </tbody>
                    </template>
                </v-simple-table>
              </v-card>
          </v-col>
      </v-row>
                    <!-- <v-dialog v-model="chngProcdialog" persistent max-width="700px">
                        <v-card>
                            <v-card-title>
                                <span class="headline">{{ chngProcformTitle }}</span>
                            </v-card-title>

                            <v-card-text>
                                <v-textarea
                                    v-model="contact_data.comment"
                                    outlined
                                    label="Комментарий"
                                >
                                </v-textarea>
                            </v-card-text>

                            <v-card-actions>
                                <v-spacer></v-spacer>
                                <v-btn color="blue darken-1" text @click="chngProcdialog = false">Cancel</v-btn>
                                <v-btn color="blue darken-1" text @click="save_contact">Save</v-btn>
                            </v-card-actions>
                        </v-card>
                    </v-dialog> -->
      <v-row>
          <v-col>
              <v-card>                
                <v-simple-table :dense="true">

                    <template v-slot:default>
                        <thead>
                            <tr>
                                <th class="text-left" colspan=2 >Информация о кредите</th>
                            </tr>
                        </thead>
                        <tbody>    
                            <tr>
                                <td>Этап обработки</td>
                                <td>
                                    <v-select
                                        v-model="agreement.process_type"
                                        :items="proc_types"
                                        :dense="true"
                                        item-text="name"
                                        item-value="id"
                                        v-on:change="changeAgreement"
                                    ></v-select>
                                </td>
                            </tr>
                            <tr>
                                <td>Тип продукта</td>
                                <td>{{ agreement.product_type }}</td>
                            </tr>
                            <tr>
                                <td>Сумма выдачи</td>
                                <td>{{ numFormat.format(agreement.initial_debt) }}</td>
                            </tr>
                            <tr>
                                <td>Кем выдан исполнительный документ</td>
                                <td></td>
                            </tr>
                            <tr>
                                <td>Дата Вступления в силу нотариальной надписи</td>
                                <td>{{ agreement.nadpis_start_date }}</td>
                            </tr>
                            <tr>
                                <td>Дата Выдачи исполнительного листа</td>
                                <td>{{ agreement.ispol_date }}</td>
                            </tr>
                            <tr>
                                <td>Номер исполнительного листа</td>
                                <td>{{ agreement.ispol_doc_no }}</td>
                            </tr>
                        </tbody>
                    </template>
                </v-simple-table>
              </v-card>
          </v-col>
          <v-col>
                <v-card>
                    <v-data-table 
                        dense 
                        :headers="payment_headers" 
                        :items="payments" 
                        item-key="name" 
                        class="elevation-1"
                        :sort-by="['Дата']"
                        :sort-desc="[false]"
                    >
                        <template v-slot:item.amount="{ item }">
                            <span>{{ numFormat.format(item.amount) }}</span>
                        </template>
                    </v-data-table>
                </v-card>
          </v-col>
      </v-row>
      <v-row>
          <v-col>
                <v-card>
                    
                    <v-simple-table :dense="true">
                        <thead>
                            <tr>
                                <th class="text-left" colspan=2 >Информация о ЧСИ</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>ФИО</td>
                                <td>        
                                    <template>           
                                        <v-select
                                            :items="ref_csi"
                                            item-text="name"
                                            item-value="id"
                                            v-model="agreement.csi"
                                            dense
                                            label=""
                                            v-on:change="changeAgreement"
                                            return-object
                                        >
                                            <template slot='selection' slot-scope='{ item }'>
                                                {{ item.region.name }} ({{ item.fio }})
                                            </template>
                                            <template slot='item' slot-scope='{ item }'>
                                                {{ item.region.name }} ({{ item.fio }})
                                            </template>
                                        </v-select>
                                    </template>
                                </td>
                            </tr>
                            <tr>
                                <td>Телефон</td>
                                <td>{{ agreement.csi ? agreement.csi.phone  : '-' }}</td>
                            </tr>
                            <tr>
                                <td>Номер лицензии</td>
                                <td>{{ agreement.csi ? agreement.csi.no  : '-' }}</td>
                            </tr>
                            <tr>
                                <td>Регион</td>
                                <td>{{ agreement.csi ? agreement.csi.region.name  : '-' }}</td>
                            </tr>
                        </tbody>
                        <thead>
                            <tr>
                                <th class="text-left" colspan=2 >Действия ЧСИ</th>
                            </tr>
                        </thead>                      
                        <tbody>
                            <tr>
                                <td colspan=2>
                                    <v-switch
                                        v-model="agreement.arrest_of_salary"
                                        true-value='Y'
                                        false-value='N'
                                        label="Арест ЗП"
                                        v-on:change="changeAgreement"
                                        dense
                                    ></v-switch>
                                </td>
                            </tr>
                            <tr>
                                <td colspan=2 align='center'>
                                    <v-switch
                                        v-model="agreement.arrest_of_property"
                                        true-value='Y'
                                        false-value='N'
                                        label="Арест имущества"
                                        v-on:change="changeAgreement"
                                        dense
                                    ></v-switch>
                                </td>
                            </tr>
                            <tr>
                                <td colspan=2>
                                    <v-switch
                                        v-model="agreement.arrest_of_accounts"
                                        true-value='Y'
                                        false-value='N'
                                        label="Арест счетов"
                                        v-on:change="changeAgreement"
                                        dense
                                    ></v-switch>
                                </td>
                            </tr>
                            <tr>
                                <td colspan=2>
                                    <v-switch
                                        v-model="agreement.arrest_of_deparure"
                                        true-value='Y'
                                        false-value='N'
                                        label="Запрет на выезд"
                                        v-on:change="changeAgreement"
                                        dense
                                    ></v-switch>
                                </td>
                            </tr>
                            <tr>
                                <td style="height: 70px;">
                                    <date-picker 
                                        v-model="agreement.give_csi_dt"
                                        v-on:change="changeAgreement"   
                                        :lang="lang" 
                                        value-type="format" 
                                        format="DD.MM.YYYY">
                                    </date-picker>
                                </td>
                                <td style="height: 70px;">Дата передачи </td>
                            </tr>
                            <tr>
                                <td style="height: 70px;">
                                    <date-picker 
                                        v-model="agreement.recall_csi_dt" 
                                        v-on:change="changeAgreement" 
                                        :lang="lang" 
                                        value-type="format" 
                                        format="DD.MM.YYYY">
                                    </date-picker>
                                </td>
                                <td style="height: 70px;">Дата отзыва </td>
                            </tr>
                            <tr>
                                <td style="height: 70px;">
                                    <date-picker 
                                        v-model="agreement.stop_actions_csi_dt" 
                                        v-on:change="changeAgreement" 
                                        :lang="lang" 
                                        value-type="format" 
                                        format="DD.MM.YYYY">
                                    </date-picker>
                                </td>
                                <td style="height: 70px;">Дата приостановления действий </td>
                            
                            </tr>
                            <tr>
                                <td style="height: 70px;">
                                    <date-picker 
                                        v-model="agreement.return_ispol_doc_dt" 
                                        v-on:change="changeAgreement" 
                                        :lang="lang" 
                                        value-type="format" 
                                        format="DD.MM.YYYY">
                                    </date-picker>
                                </td>
                                <td style="height: 70px;">Дата возврата испол. документа</td>
                            </tr>
                            
                        </tbody>
                    </v-simple-table>
                </v-card>
          </v-col>
          <v-col>
                <v-card>  
                  
                    <v-data-table 
                        dense 
                        :headers="contact_headers" 
                        :items="contacts" 
                        item-key="id" 
                        :single-expand="singleExpand"
                        :expanded.sync="expanded"
                        show-expand
                        class="elevation-1"
                    >
                    <template v-slot:expanded-item="{ headers, item }">
                        <td :colspan="headers.length">{{ item.comment }}</td>
                    </template>
                    <template v-slot:item.installment_amt="{ item }">
                        <span>{{ numFormat.format(item.installment_amt) }}</span>
                    </template>
                    <template v-slot:top>
                        <v-toolbar flat color="white">
                                    
                            <v-card-title>
                                <v-text-field
                                    label="Поиск"
                                    single-line
                                    hide-details
                                ></v-text-field>
                            </v-card-title> 
                            <v-spacer></v-spacer>
                            <v-dialog v-model="dialog" persistent max-width="700px">
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
                                                :value="contact_load_overlay"  
                                                :z-index="5"
                                                >
                                                <v-progress-circular
                                                    indeterminate
                                                    color="purple"
                                                ></v-progress-circular>
                                                </v-overlay>                  
                                                <v-col class="d-flex" cols="12" >
                                                    <v-select
                                                        v-model="contact_data.type"
                                                        :items="contact_type"
                                                        item-text="name"
                                                        item-value="id"
                                                        label="Тип контакта"
                                                    ></v-select>
                                                </v-col>
                                            </v-row> 
                                            <v-row v-if="contact_data.type == 1">
                                                <v-col> 
                                                    <v-row>
                                                        <v-col>
                                                            <v-radio-group v-model="add_phone_style" :mandatory="false" row>
                                                                <v-radio label="Существующий" value="old"></v-radio>
                                                                <v-radio label="Новый" value="new"></v-radio>
                                                            </v-radio-group>
                                                        </v-col>
                                                    </v-row>  
                                                    <v-row v-if="add_phone_style == 'old'">
                                                        <v-col>
                                                            <v-select 
                                                                
                                                                v-model="contact_data.phone_id"
                                                                :items="customer_phones"
                                                                item-text="phone"
                                                                item-value="id"
                                                                label="Телефон"
                                                            ></v-select>
                                                        </v-col>
                                                    </v-row>
                                                    <v-row v-if="add_phone_style == 'new' ">
                                                        <v-col>
                                                            <v-text-field
                                                                label="Номер телефона"
                                                                placeholder="Placeholder"
                                                                v-model="contact_data.new_phone"
                                                                outlined
                                                                dense
                                                            ></v-text-field>   
                                                        </v-col>    
                                                        <v-col>                                 
                                                            <v-select
                                                                v-model="contact_data.new_phone_type"
                                                                :items="phone_types"
                                                                item-text="name"
                                                                item-value="id"
                                                                label="Тип телефона"
                                                                dense
                                                            ></v-select>
                                                        </v-col>
                                                    </v-row>
                                                </v-col>
                                            </v-row>                  
                                            <v-row>                  
                                                <v-col class="d-flex" cols="12" >                                        
                                                    <v-select
                                                        v-model="contact_data.result"
                                                        :items="contact_result"
                                                        item-text="name"
                                                        item-value="id"
                                                        label="Результат контакта"
                                                    ></v-select>
                                                </v-col>
                                            </v-row>
                                            <v-row v-if="contact_data.result == 1">
                                                <v-col>          
                                                    <v-text-field
                                                        label="Сумма отсрочки"
                                                        outlined
                                                        dense
                                                        v-model="contact_data.installment_amt"
                                                    ></v-text-field>
                                                </v-col>
                                                <v-col>
                                                    <v-menu
                                                        v-model="menu2"
                                                        :close-on-content-click="false"
                                                        :nudge-right="40"
                                                        transition="scale-transition"
                                                        offset-y
                                                        min-width="290px"
                                                    >
                                                        <template v-slot:activator="{ on }">
                                                            <v-text-field
                                                                v-model="contact_data.installment_dt_to"
                                                                label="Дата отсрочки"
                                                                outlined
                                                                dense
                                                                readonly
                                                                v-on="on"
                                                            ></v-text-field>
                                                        </template>
                                                        <v-date-picker v-model="contact_data.installment_dt_to" @input="menu2 = false"></v-date-picker>
                                                    </v-menu>
                                                </v-col>
                                            </v-row>       
                                            <v-row>
                                                <v-col>
                                                    <v-textarea
                                                        v-model="contact_data.comment"
                                                        outlined
                                                        label="Комментарий"
                                                    >
                                                    </v-textarea>
                                                </v-col>
                                            </v-row>
                                        </v-container>
                                    </v-card-text>

                                    <v-card-actions>
                                        <v-spacer></v-spacer>
                                        <v-btn color="blue darken-1" text @click="close_contact_modal">Отмена</v-btn>
                                        <v-btn color="blue darken-1" text @click="save_contact">Сохранить</v-btn>
                                    </v-card-actions>
                                </v-card>
                            </v-dialog>
                        </v-toolbar>
                    </template>

                    </v-data-table>
                </v-card>
          </v-col>
      </v-row>
  </v-container>
</template>

<script>
    /*eslint-disable */
    // import moment from 'moment'
    import DatePicker from 'vue2-datepicker';
    import 'vue2-datepicker/index.css';
    
    export default {
        components: { DatePicker },
        name: 'Card',

        data: () => ({
            headers: [
                {
                    text: 'Dessert (100g serving)',
                    align: 'start',
                    sortable: false,
                    value: 'name',
                },
                { text: 'Calories', value: 'calories' },
                { text: 'Fat (g)', value: 'fat' },
                { text: 'Carbs (g)', value: 'carbs' },
                { text: 'Protein (g)', value: 'protein' },
                { text: 'Iron (%)', value: 'iron.val' },
                { text: '', value: 'data-table-expand' },
            ], 
        
            singleExpand: true,
            expanded: [],
            numFormat: new Intl.NumberFormat('ru-RU'),
            lang: {
                formatLocale: {
                    monthsShort: ['Янв', 'Фев', 'Мар', 'Апр', 'Май', 'Июнь', 'Июл', 'Авг', 'Сен', 'Окт', 'Ноя', 'Дек'],
                },
            },
            dialog: false,
            formTitle: "Добавить контакт",
            chngProcdialog: false,
            chngProcformTitle: "Коментарий к изменеию стадии",
            contact_load_overlay: false,
            add_phone_style: 'old',
            contact_headers: [                
                { text: 'Дата', value: 'created' },
                { text: 'Тип', value: 'type.name' },
                { text: 'Рузультат', value: 'result.name' },
                { text: 'Отсрочка', value: 'installment_amt' },
                { text: '', value: 'data-table-expand' },
            ],
            payment_headers: [                
                { text: 'Дата', value: 'created' },
                { text: 'Сумма', value: 'amount' }
            ],
            testDate: "2020-04-21",
            menu: false,
            modal: false,
            menu2: false,
            menu3: false,
            menu4: false,
            menu5: false,
            menu6: false,
            menu7: false,
        }),

        computed: {
            agreement() { 
                let a = this.$store.getters.agreement_Card(this.$route.params.id)
                return  a ? a : {}
            },
            tags(){
                let a = this.$store.getters.all_customer_agreements(this.$route.params.id)
                return  a ? a : {}
            },
            payments() { 
                let a = this.$store.getters.agreement_payments
                return  a ? a : {}
            },
            sum_agreement_payments() { 
                let a = this.$store.getters.sum_agreement_payments
                return  a ? a : 0
            },
            ref_csi(){
                return this.$store.getters.ref_csi
            },
            proc_types(){
                return this.$store.getters.ref_process_type
            },
            contacts(){
                return this.$store.getters.contacts
            },
            contact_type(){
                return this.$store.getters.ref_contact_type
            },
            contact_result(){
                return this.$store.getters.ref_contact_result
            },
            contact_data(){
                let o = this.$store.getters.contactData
                return o ? o : {}
            },
            customer_phones(){
                let o = this.$store.getters.customer_phones
                return o ? o : []
            },
            phone_types(){
                let o = this.$store.getters.ref_customer_phone_type
                return o ? o : []
            },
        },
        
        created () {
            this.fetchData()
        },

        watch: {
            // call again the method if the route changes
            '$route': 'fetchData'
        },

        methods: {
            close_contact_modal(){
                this.dialog = false
                this.contact_load_overlay = false
            },
            fetchData(){
                this.$store.dispatch('getAgreementByID', this.$route.params.id)
                this.$store.dispatch('getAgreementPaymentsByAgreementID', this.$route.params.id)
                this.$store.dispatch('loadProcessTypes')
                this.$store.dispatch('loadContactTypes')
                this.$store.dispatch('loadCustomerPhoneTypes')
                this.$store.dispatch('loadRefCsi')
                this.$store.commit('setContactAgreement', this.$route.params.id)
                this.$store.dispatch('loadContactResults')
                this.$store.dispatch('loadCustomerPhonesByAgreement', this.$route.params.id)
            },
            openAgreement(id){
                if(id == this.$route.params.id) return
                this.$router.push({ path: `/agreement/${id}` }) // -> /agreement/123
            },
            // changeProcType(){
            //     // this.chngProcdialog = true
            //     await this.$store.dispatch('changeProcType', this.$route.params.id)
            // },
            async changeAgreement(){
                // debugger
                await this.$store.dispatch('changeAgreement', this.$route.params.id)
            },
            async save_contact(){
                // debugger;
                this.contact_load_overlay = true
                await this.$store.dispatch('saveContactData')
                await this.close_contact_modal()
                return true
            }
        }
    }
</script>