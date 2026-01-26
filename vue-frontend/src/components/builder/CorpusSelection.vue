<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import { fetchBooksDataset, setCorpus } from '../../api/builder'

const emit = defineEmits<{
  close: []
  submit: []
}>()

interface Book {
  id: string
  title: string
  author: string
}

const books = ref<Book[]>([])
const selectedBooks = ref<string[]>([])
const loading = ref(true)
const error = ref<string | null>(null)
const MAX_SELECTION = 2

onMounted(async () => {
  try {
    const data = await fetchBooksDataset()
    console.log('Books data:', data)
    books.value = data.books || []
    selectedBooks.value = data.active_corpus || []
  } catch (e) {
    error.value = 'Failed to load books'
    console.error(e)
  } finally {
    loading.value = false
  }
})

const canSelectMore = computed(() => selectedBooks.value.length < MAX_SELECTION)

function toggleBook(bookId: string) {
  const index = selectedBooks.value.indexOf(bookId)
  if (index > -1) {
    selectedBooks.value.splice(index, 1)
  } else if (canSelectMore.value) {
    selectedBooks.value.push(bookId)
  }
}

async function handleSubmit() {
  if (selectedBooks.value.length === 0) {
    error.value = 'Please select at least one book'
    return
  }
  
  try {
    loading.value = true
    await setCorpus(selectedBooks.value)
    emit('submit')
    emit('close')
  } catch (e) {
    error.value = 'Failed to update corpus'
    console.error(e)
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="modal-overlay" @click.self="emit('close')">
    <div class="modal-content">
      <div class="modal-header">
        <h2>Select Books (Max {{ MAX_SELECTION }})</h2>
        <button @click="emit('close')" class="close-btn">&times;</button>
      </div>

      <div v-if="loading" class="loading">Loading books...</div>
      
      <div v-else-if="error" class="error">{{ error }}</div>

      <div v-else-if="books.length === 0" class="empty">No books available</div>

      <div v-else class="modal-body">
        <p class="selection-info">
          Selected: {{ selectedBooks.length }} / {{ MAX_SELECTION }}
        </p>

        <div class="books-list">
          <div 
            v-for="book in books" 
            :key="book.id"
            class="book-item"
            :class="{ 
              'selected': selectedBooks.includes(book.id),
              'disabled': !selectedBooks.includes(book.id) && !canSelectMore
            }"
            @click="toggleBook(book.id)"
          >
            <input 
              type="checkbox" 
              :id="book.id"
              :checked="selectedBooks.includes(book.id)"
              :disabled="!selectedBooks.includes(book.id) && !canSelectMore"
              @click.stop
              @change="toggleBook(book.id)"
            />
            <label :for="book.id" class="book-label">
              <span class="book-title">{{ book.title }}</span>
              <span class="book-author">by {{ book.author }}</span>
            </label>
          </div>
        </div>
      </div>

      <div class="modal-footer">
        <button @click="emit('close')" class="btn btn-cancel">Cancel</button>
        <button 
          @click="handleSubmit" 
          :disabled="selectedBooks.length === 0 || loading"
          class="btn btn-submit"
        >
          {{ loading ? 'Submitting...' : 'Submit' }}
        </button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  background: white;
  border-radius: 12px;
  width: 90%;
  max-width: 600px;
  max-height: 80vh;
  display: flex;
  flex-direction: column;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.modal-header {
  padding: 1.5rem;
  border-bottom: 1px solid #e5e7eb;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.modal-header h2 {
  margin: 0;
  font-size: 1.5rem;
  font-weight: 600;
}

.close-btn {
  background: none;
  border: none;
  font-size: 2rem;
  cursor: pointer;
  color: #6b7280;
  line-height: 1;
  padding: 0;
  width: 2rem;
  height: 2rem;
}

.close-btn:hover {
  color: #374151;
}

.modal-body {
  padding: 1.5rem;
  overflow-y: auto;
  flex: 1;
}

.loading, .error, .empty {
  padding: 2rem;
  text-align: center;
}

.error {
  color: #ef4444;
}

.empty {
  color: #6b7280;
}

.selection-info {
  margin-bottom: 1rem;
  font-size: 0.875rem;
  color: #6b7280;
}

.books-list {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.book-item {
  display: flex;
  align-items: flex-start;
  gap: 0.75rem;
  padding: 0.75rem;
  border: 2px solid #e5e7eb;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s;
}

.book-item:hover:not(.disabled) {
  border-color: #3b82f6;
  background: #eff6ff;
}

.book-item.selected {
  border-color: #22c55e;
  background: #f0fdf4;
}

.book-item.disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.book-item input[type="checkbox"] {
  margin-top: 0.25rem;
  cursor: pointer;
  width: 1.25rem;
  height: 1.25rem;
  flex-shrink: 0;
}

.book-label {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
  flex: 1;
  cursor: pointer;
}

.book-title {
  font-weight: 600;
  color: #111827;
}

.book-author {
  font-size: 0.875rem;
  color: #6b7280;
}

.modal-footer {
  padding: 1.5rem;
  border-top: 1px solid #e5e7eb;
  display: flex;
  justify-content: flex-end;
  gap: 0.75rem;
}

.btn {
  padding: 0.5rem 1.5rem;
  border-radius: 6px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
  border: none;
}

.btn-cancel {
  background: #f3f4f6;
  color: #374151;
}

.btn-cancel:hover {
  background: #e5e7eb;
}

.btn-submit {
  background: #3b82f6;
  color: white;
}

.btn-submit:hover:not(:disabled) {
  background: #2563eb;
}

.btn-submit:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
</style>