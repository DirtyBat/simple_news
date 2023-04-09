<template>
  <div>
    <el-upload
      :headers="getHeader"
      :with-credentials="false"
      :multiple="multiple"
      :limit="limit"
      name="pic"
      class="quill-upload"
      accept=".JPG, .PNG, .JPEG, .jpg, .png, .jpeg"
      :action="serviceUrl"
      style="display: none;width:0;"
      :show-file-list="false"
      :on-success="success"
      :before-upload="beforeAvatarUpload"
    >
      <!-- <el-button size="small" type="primary">点击上传</el-button> -->
      <i class="el-icon-upload"></i>
      <div class="el-upload__text">
        将文件拖到此处，或
        <em>点击上传</em>
      </div>
      <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过500kb</div>
    </el-upload>
    <quill-editor
      ref="myQuillEditor"
      :content="content"
      v-model="editorData"
      :options="editorOption"
    ></quill-editor>
  </div>
</template>
<script>
import Vue from "vue";
import "quill/dist/quill.core.css";
import "quill/dist/quill.snow.css";
import "quill/dist/quill.bubble.css";
// import Quill from 'quill';
// import { quillEditor } from "vue-quill-editor";
// import { ImageDrop } from "quill-image-drop-module";
// import ImageResize from 'quill-image-resize-module';
// // Quill.register('modules/imageResize', ImageResize);
// Quill.register("modules/imageDrop", ImageDrop);

import { quillEditor, Quill } from "vue-quill-editor";
import { ImageDrop } from "quill-image-drop-module";
import imageResize from 'quill-image-resize-module'
Quill.register('modules/imageResize', imageResize)
Quill.register("modules/imageDrop", ImageDrop);
Vue.use(quillEditor);

export default {
  name: "editor",
  components: { quillEditor },
  props: ["getHeader", "content", "limit", "multiple"],
  data() {
    // 富文本配置
    const toolbarOptions = [
      ["bold", "italic", "underline", "strike"], // toggled buttons
      ["blockquote", "code-block"],

      [{ header: 1 }, { header: 2 }], // custom button values
      [{ list: "ordered" }, { list: "bullet" }],
      [{ script: "sub" }, { script: "super" }], // superscript/subscript
      [{ indent: "-1" }, { indent: "+1" }], // outdent/indent
      [{ direction: "rtl" }], // text direction

      [{ size: ["small", false, "large", "huge"] }], // custom dropdown
      [{ header: [1, 2, 3, 4, 5, 6, false] }],

      [{ color: [] }, { background: [] }], // dropdown with defaults from theme
      [{ font: [] }],
      [{ align: [] }],
      ["image"]
    ];
    return {
      serviceUrl: process.env.API_ROOT + "api/pic",
      editorOption: {
        placeholder: "请输入内容",
        modules: {
          imageDrop: true,
          imageResize: true,
          toolbar: {
            container: toolbarOptions,
            handlers: {
              // 重写点击组件上的图片按钮要执行的代码
              image: function(value) {
                document.querySelector(".quill-upload .el-icon-upload").click();
              }
            }
          }
        }
      },
      editorData: ""
    };
  },
  methods: {
    beforeAvatarUpload(file) {
      this.$emit("beforeAvatarUpload", file);
    },
    success(res, file, fileList) {
      // res为图片服务器返回的数据
      // 获取富文本组件实例
      let vm = this;
      let quill = this.$refs.myQuillEditor.quill;
      // 获取光标所在位置
      const pos = quill.selection.savedRange.index; //这个得注意下，网上很多都是不对的
      // 插入图片到光标位置
      quill.insertEmbed(pos, "image", this.serviceUrl + "?code=" + res["code"]);
      // 调整光标到最后
      quill.setSelection(length + 1);
      // loading动画消失
      this.quillUpdateImg = false;
    }
  },
  watch: {
    serviceUrl(val) {
      this.serviceUrl = val;
    },
    getHeader(val) {
      this.getHeader = val;
    },
    editorData(val) {
      this.$emit("getEditorData", this.editorData);
    },
    content(val) {
      this.content = val;
    }
  }
};
</script>

<style scoped>
.quill-editor {
  height: 55vh;
  margin-bottom: 70px;
}
</style>