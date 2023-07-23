<template>
  <div class="checkbox">
    <label class="checkbox_contents label_position_right">
      <input
      :id="id"
      :value="value"
      type="checkbox"
      v-model="checkedModel"
      :checked="checked"
      :disabled="disabled"
      :required="required"
      @change="changeEvent"
      />
      <span class="lever">
        <FontAwesomeIcon :icon="faCheck" class="check_icon"></FontAwesomeIcon>
      </span>
              <slot />
    </label>
  </div>
</template>

<script setup lang="ts">
import { computed } from "vue";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { faCheck } from '@fortawesome/free-solid-svg-icons'

interface Props {
  id?: string
  disabled?: boolean
  required?: boolean
  checked?: boolean
  modelValue?: string | boolean
  value?: string | boolean | number | object

}
const props = withDefaults(defineProps<Props>(), {
  id: '',
  disabled: false,
  required: true,
  checked: false,
  modelValue: '',
  value: undefined
})

const emit = defineEmits(['checked', 'update:modelValue'])

const changeEvent = (event: any) => {
  if (event.target.checked) {
    emit('checked')
  }
}

const checkedModel = computed({
  get: () => props.modelValue,
  set: (value) => { emit('update:modelValue', value) }
})
</script>

<style scoped>
.checkbox {
  display: inline-block;

  .checkbox_contents {
    cursor: pointer;
    font-size: 1.4rem;
    text-align: center;
    display: flex;
    align-items: center;

    input[type='checkbox'] {
      display: none;

      &:checked + .lever {
        background: #282828;
      }

      &:disabled + .lever {
        background: #dddddd;
      }
    }

    &.label_position_right {
      .lever {
        margin-right: 0.5rem;
      }
    }

    .lever {
      font-size: 1rem;
      border-radius: 3px;
      border: 1px solid #cccccc;
      vertical-align: middle;
      background-color: #ffffff;

      .check_icon {
        color: #ffffff;
        width: 15px;
        height: 15px;
        padding: 2px;
        vertical-align: middle;
      }
    }
  }
}
</style>
