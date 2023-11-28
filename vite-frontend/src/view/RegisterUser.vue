<template>
  <div class="registration-container">
    <h2>Rejestracja</h2>
    <div class="progress-container">
      <progress :max="steps.length" :value="currentStep"></progress>
      <div class="progress-label">
        Postęp: {{ currentStep }} / {{ steps.length }}
      </div>
    </div>
    <form @submit.prevent="submitForm" class="registration-form">
      <div class="form-group">
        <label>{{ currentForm.text }}</label>
        <input
          :type="currentForm.input.type"
          :style="currentForm.input.style"
          :placeholder="currentForm.input.other.placeholder"
          :maxlength="currentForm.input.other.maxLength"
          v-model="formData[currentStep]"
        />
      </div>
      <div class="button-group">
        <button @click="previousStep" v-if="currentStep > 1" class="btn btn-secondary">Wróć</button>
        <button type="submit" class="btn btn-primary">Dalej</button>
      </div>
    </form>
    
  </div>
</template>

<script>
import { ref, computed } from 'vue';

export default {
  setup() {
    const currentStep = ref(1);
    const formData = ref({});
    
    const steps = [
      {
        text: "Podaj imię",
        input: {
          type: "text",
          style: { },
          other: { maxLength: 10, placeholder: "Wprowadź imię" },
        },
      },
      {
        text: "Podaj adres e-mail",
        input: {
          type: "email",
          style: { },
          other: { maxLength: 50, placeholder: "Wprowadź adres e-mail" },
        },
      },
      {
        text: "Podaj hasło",
        input: {
          type: "password",
          other: { placeholder: "Wprowadź hasło" },
        },
      },
    ];
    
    const currentForm = computed(() => {
      return steps[currentStep.value - 1] || {};
    });
    
    const submitForm = () => {
      formData[currentStep.value] = currentForm.value;
      
      if (currentStep.value < steps.length) {
        currentStep.value++;
      } else {
        //console.log("Rejestracja zakończona");
      }
    };

    const previousStep = () => {
      if (currentStep.value > 1) {
        currentStep.value--;
      }
    };

    return {
        steps,
      currentStep,
      currentForm,
      formData,
      submitForm,
      previousStep,
    };
  },
};
</script>

<style scoped>
.registration-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  text-align: center;
  background-image: var(--mainPage);
  background-size: cover;
}

.registration-form {
  border: 1px solid #ccc;
  padding: 30px;
  border-radius: 5px;
  background-color: #f7f7f7;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  width: 500px;
}

.form-group {
  margin-bottom: 15px;
}

.button-group {
  display: flex;
  justify-content: space-between;
  margin-top: 15px;
}

.btn {
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  color: #fff;
  font-weight: bold;
}

.btn-secondary {
  background-color: #999;
}

.btn-primary {
  background-color: #007bff;
}

.progress-container {
  margin-top: 20px;
  width: 500px;
}

progress {
  width: 100%;
}

.progress-label {
  margin-top: 10px;
  font-weight: bold;
}
</style>
