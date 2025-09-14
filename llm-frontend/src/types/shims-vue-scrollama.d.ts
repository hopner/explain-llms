// src/types/shims-vue-scrollama.d.ts
declare module 'vue-scrollama' {
  import { DefineComponent } from 'vue'
  const Scrollama: DefineComponent<Record<string, unknown>, {}, any>
  export default Scrollama
}
