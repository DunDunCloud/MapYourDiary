<template>
    <modal name="my-first-modal">
        <div>Modal TestModal TestModal TestModal TestModal Test</div>
    </modal>
</template>

<script>
export default {
    name: 'MyModal',
    methods: {
        show () {
            this.$modal.show('my-first-modal');
        },
        hide () {
            this.$modal.hide('my-first-modal');
        }
    },
    mount () {
        this.show()
    }
}
</script>