const InputForm = {
    template: `
        <div class="input-form">
            <div class="notification has-background-white" v-if="visible" style="position: fixed; bottom: -1px;right: 40px;">
                <form @submit="submitForm" class="ui form">
                    <div class="field">
                        <div class="control">
                            <input class="input" v-model="fields.nama" type="text" placeholder="Add a name!" />
                            <span style="color: red">{{ fieldErrors.nama }}</span>
                        </div>
                    </div>
                    <div class="field">
                        <div class="control">
                            <input class="input" v-model="fields.nomor" type="text" placeholder="What's your phone number?" />
                            <span style="color: red">{{ fieldErrors.nomor }}</span>
                        </div>
                    </div>
                    <div class="field">
                        <div class="control">
                            <input class="textarea" v-model="fields.message" type="text" placeholder="What's your message?" />
                            <span style="color: red">{{ fieldErrors.message }}</span>
                        </div>
                    </div>
                    <div class="control">
                        <button class="button">Submit</button>
                    </div>
                </form>
            </div>

            <button class="button has-background-primary" is-paddingless style="
                  position: fixed;
                  width: 170px;
                  height: 40px;
                  bottom: 5px;
                  right: 10px;
                  color: #fff;
                  border-radius: 50px;
                  text-align: center;
                  cursor: pointer;
                  box-shadow: 2px 2px 3px #999;"

                  @click="visibleForm(!visible)">

                <div class="media-left is-paddingless">
                    <img
                      src="https://trickuweb.com/whatsapp.png"
                      alt=""
                      height="30px"
                      width="30px"
                    />
                </div>
                <div class="media-content is-paddingless">
                    <p class="subtitle is-size-7 has-text-centered has-text-white">Butuh Bantuan?</p>
                </div>
            </button>
        </div>`,
  props: ['visible'],
  emits: ['change-visible'],
  data() {
    return {
      fields: {
        nama: '',
        nomor: '',
        message: '',
      },
      fieldErrors: {
        nama: undefined,
        nomor: undefined,
        message: undefined,
      },
    }
  },
  methods: {
    submitForm(evt) {
      evt.preventDefault();

      this.fieldErrors = this.validateForm(this.fields);
      if (Object.keys(this.fieldErrors).length) return;

      var data = {
          'nama': this.fields.nama,
          'nomor': this.fields.nomor,
          'message': this.fields.message,
      };

      var url = "https://api.whatsapp.com/send?phone=6289608372301&text="
          + "FORMAT TANYA" + "%0a"
          + "%0a"
          + "Name: " + data.nama + "%0a"
          + "nomor: " + data.nomor + "%0a"
          + "message: " + data.message  + "%0a";

      window.open(url, '_blank').focus();

      this.fields.nama = '';
      this.fields.nomor = '';
      this.fields.message = '';
    },
    validateForm(fields) {
      const errors = {};
      if (!fields.nama) errors.nama = "Name Required";
      if (!fields.nomor) errors.nomor = "Phone Number Required";
      if (!fields.message) errors.message = "Message Required";

      return errors;
    },
    visibleForm() {
        this.$emit('change-visible', {
        });
    },
  }
}

var app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data () {
        return {
            mainImage: "",
            testimonis: [],
            isActive: false,
            visible: false,
        }
    },
    components: {
        "input-form": InputForm,
    },
    async mounted () {
        const response = await axios
            .get(`https://www.myproject.192.168.56.5.xip.io/en/webpage/testimoni/`)
            .then(function(response) {
                return response.data;
            });
            this.mainImage = this.mainImage + response[0].picture;
            for (result of response) {
                this.testimonis.push(result);
            };
    },
    methods: {
        changeMainImage(image) {
            this.mainImage = image;
        },
        goto(refName) {
            var element = this.$refs[refName];
            var top = element.offsetTop;

            window.scrollTo(0, top);
        },
        changeVisible(event){
            this.visible = !this.visible;
        }
    },
});