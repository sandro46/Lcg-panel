<template>

    <v-dialog v-model="csi_actions_dialog" persistent max-width="800px">
        <template v-slot:activator="{ on }">

            <v-btn v-if="mode == 'addItem'" color="primary" dark class="mb-2" v-on="on">
                <v-icon>mdi-plus</v-icon>
            </v-btn>     
            <v-icon v-if="mode == 'editItem'" small v-on="on">
                mdi-pencil
            </v-icon>         

        </template>
        <v-card>

            <v-card-title>
                <span class="headline">Добавить действие ЧСИ {{mode}}</span>
            </v-card-title>



            <v-simple-table :dense="true">
                <thead>
                    <tr>
                        <th class="text-left" colspan=2 >Действия ЧСИ</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>ЧСИ</td>
                        <td>        
                            <template>           
                                <v-select
                                    :items="ref_csi"
                                    item-text="name"
                                    item-value="id"
                                    v-model="csi_action_data.csi"
                                    dense
                                    label=""
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
                        <td colspan=2>
                            <v-switch
                                v-model="csi_action_data.arrest_of_salary"
                                true-value='Y'
                                false-value='N'
                                label="Арест ЗП"
                                dense
                            ></v-switch>
                        </td>
                    </tr>
                    <tr>
                        <td colspan=2 align='center'>
                            <v-switch
                                v-model="csi_action_data.arrest_of_property"
                                true-value='Y'
                                false-value='N'
                                label="Арест имущества"
                                dense
                            ></v-switch>
                        </td>
                    </tr>
                    <tr>
                        <td colspan=2>
                            <v-switch
                                v-model="csi_action_data.arrest_of_accounts"
                                true-value='Y'
                                false-value='N'
                                label="Арест счетов"
                                dense
                            ></v-switch>
                        </td>
                    </tr>
                    <tr>
                        <td colspan=2>
                            <v-switch
                                v-model="csi_action_data.arrest_of_deparure"
                                true-value='Y'
                                false-value='N'
                                label="Запрет на выезд"
                                dense
                            ></v-switch>
                        </td>
                    </tr>
                    <tr>
                        <td style="height: 70px;">
                            <date-picker 
                                v-model="csi_action_data.give_csi_dt"
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
                                v-model="csi_action_data.recall_csi_dt" 
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
                                v-model="csi_action_data.stop_actions_csi_dt" 
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
                                v-model="csi_action_data.return_ispol_doc_dt" 
                                :lang="lang" 
                                value-type="format" 
                                format="DD.MM.YYYY">
                            </date-picker>
                        </td>
                        <td style="height: 70px;">Дата возврата испол. документа</td>
                    </tr>
                    <tr>
                        <td colspan="2">
                            <v-textarea
                                v-model="csi_action_data.comment"
                                outlined
                                label="Комментарий ЧСИ"
                                style='padding-top: 10px;'
                            >
                            </v-textarea>
                        </td>
                    </tr>
                </tbody>
            </v-simple-table>


                <v-card-text>
                <v-container>
                    <v-overlay
                        :absolute="true"
                        :opacity="0.46"
                        :value="csi_actions_load_overlay"  
                        :z-index="5"
                    >
                        <v-progress-circular
                            indeterminate
                            color="purple"
                        ></v-progress-circular>
                    </v-overlay> 
                    
                </v-container>
            </v-card-text>

            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="close_csi_actions_modal">Отмена</v-btn>
                <v-btn v-if="mode == 'addItem'" color="blue darken-1" text @click="save_csi_action">Сохранить</v-btn>
                <v-btn v-if="mode == 'editItem'" color="blue darken-1" text @click="edit_csi_action">Сохранить</v-btn>
            </v-card-actions>

        </v-card>
    </v-dialog>

</template>

<script>

    import DatePicker from 'vue2-datepicker';
    import 'vue2-datepicker/index.css';

    export default {
        components: { DatePicker },
        name: 'Csi_action_modal',

        props:{
            csi_action_data: {
                type: Object
            },
            ref_csi: {
                type: Array,
                required: true,
            },
            lang: {
                type: Object,
                required: true
            },
            mode: {
                type: String
            }
        },

        data: () => ({
            csi_actions_dialog: false,
            csi_actions_load_overlay: false
        }),
        methods: {

            close_csi_actions_modal() {
                this.csi_actions_dialog = false
                this.csi_actions_load_overlay = false
            },
            async save_csi_action(){
                this.csi_actions_load_overlay = true
                await this.$store.dispatch('saveCsiAction', this.csi_action_data)
                await this.close_csi_actions_modal()
                return true
            },
            async edit_csi_action(){
                this.csi_actions_load_overlay = true
                await this.$store.dispatch('editCsiAction', this.csi_action_data)
                await this.close_csi_actions_modal()
                return true
            },

        }
    }

</script>

