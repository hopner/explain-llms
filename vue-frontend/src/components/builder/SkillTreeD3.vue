<script setup lang="ts">
import * as d3 from 'd3'
import { onMounted, ref, watch, nextTick } from 'vue'
import { fetchSkillTree, addFeatureToConfig, removeFeatureFromConfig } from '../../api/builder'
import { useRouter } from 'vue-router'
import { featureToRoute } from '../../router/featureRoutes'
import CorpusSelection from './CorpusSelection.vue'

const props = defineProps<{
    boundingBox?: { width: number; height: number }
    rootPosition?: { x?: number }
}>()

const svgRef = ref<SVGSVGElement | null>(null)
const data = ref<any>(null)
const router = useRouter()
const error = ref<string | null>(null)

const showCorpusModal = ref(false)

const LAYOUT = {
    width: 1000,
    height: 800,
    minWidth: 600,
    minHeight: 300,
    margin: { top: 60, right: 100, bottom: 50, left: 50 },
    nodeSpacing: { x: 120, y: 50 },
    minBoxWidth: 80,
    boxHorizontalPadding: 20,
    boxVerticalPadding: 12,
    rectRx: 8,
    fontSize: 13,
    fontFamily: "Inter, system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial",
}

onMounted(async () => {
    data.value = await fetchSkillTree()
    await nextTick()
    drawTree(data.value)
})

watch(() => [props.boundingBox, props.rootPosition], async () => {
    if (!data.value) return
    await nextTick()
    drawTree(data.value)
}, { deep: true })

function drawTree(treeData: any) {
    const width = props.boundingBox?.width ?? LAYOUT.width
    const height = props.boundingBox?.height ?? LAYOUT.height
    const margin = LAYOUT.margin

    if (!svgRef.value) return
    const svg = d3.select(svgRef.value as unknown as SVGSVGElement)
        .attr('width', width)
        .attr('height', height)
        .style('background', 'transparent')

    svg.selectAll('*').remove() // clear old tree

    if (treeData?.status === 'locked') {
      d3.select(svgRef.value).selectAll('*').remove()
      return
    }
    
    const root = d3.hierarchy(treeData, (d: any) => {
      if (!Array.isArray(d.children)) return null
      const visibleChildren = d.children.filter((c: any) => c?.status !== 'locked')
      return visibleChildren.length ? visibleChildren : null
    })

    const NODE_SPACING = { x: LAYOUT.nodeSpacing.x, y: LAYOUT.nodeSpacing.y }
    const treeLayout = d3.tree().nodeSize([NODE_SPACING.x, NODE_SPACING.y])
    treeLayout(root)

    const xs = root.descendants().map((n: any) => n.x)
    const availableWidth = width - margin.left - margin.right

    const desiredRootX = (props.rootPosition && typeof props.rootPosition.x === 'number')
        ? props.rootPosition.x
        : availableWidth / 2

    const meanX = xs.reduce((a: number, b: number) => a + b, 0) / Math.max(1, xs.length)
    const actualRootX = (typeof (root as any).x === 'number') ? (root as any).x : meanX
    const centerOffsetX = desiredRootX - actualRootX

    const g = svg.append('g').attr('transform', `translate(${margin.left + centerOffsetX},${margin.top})`)

    g.selectAll('.link')
        .data(root.links())
        .join('path')
        .attr('class', 'link')
        .attr('d', d3.linkVertical<any, any>()
            .x(d => d.x)
            .y(d => d.y)
        )
        .attr('stroke', '#888')
        .attr('fill', 'none')

    const nodes = g.selectAll('.node')
        .data(root.descendants())
        .join('g')
        .attr('class', 'node')
        .attr('transform', d => `translate(${d.x},${d.y})`)

    nodes.each(function (this: any, d: any) {
        const g = d3.select(this)
        const label = d.data.name.replace(/_/g, ' ')
        const textLength = label.length * 7.2 // rough per-character width
        const boxWidth = Math.max(80, textLength + 20)

        const button = g.append('g')
            .attr('class', 'button')
            .style('cursor', d.data.status === 'available' || d.data.status === 'selected' ? 'pointer' : 'default')
            .on('mouseover', function () { d3.select(this).select('rect.visible').attr('fill-opacity', 0.85) })
            .on('mouseout', function () { d3.select(this).select('rect.visible').attr('fill-opacity', 1) })
            .on('click', function () {
                if (d.data.status === 'available') selectAlternative(d.data.name)
                else if (d.data.status === 'selected') removeSelected(d.data.name)
            })

        button.append('rect')
            .attr('x', -boxWidth / 2)
            .attr('y', -15)
            .attr('rx', 8)
            .attr('width', boxWidth)
            .attr('height', 30)
            .attr('fill', (() => {
                switch (d.data.status) {
                    case 'selected': return '#22c55e'
                    case 'available': return '#3b82f6'
                    default: return '#6b7280'
                }
            })())

        button.append('text')
            .attr('text-anchor', 'middle')
            .attr('alignment-baseline', 'middle')
            .attr('fill', '#e5e5e5')
            .attr('font-size', 13)
            .attr('font-weight', 600)
            .text(label)
    })


}

async function selectAlternative(featureId: string) {
    try {
        if (featureId === 'select_corpus') {
            showCorpusModal.value = true
            return
        }

        const routeName = featureToRoute(featureId)
        router.push({ name: routeName })
        await addFeatureToConfig(featureId)
    } catch (e) {
        error.value = 'Could not add improvement.'
    }
}

async function handleCorpusSubmit() {
    data.value = await fetchSkillTree()
    await nextTick()
    drawTree(data.value)
}

async function removeSelected(featureId: string) {
    try {
        const confirmed = window.confirm('Are you sure you want to remove this improvement and all its dependent improvements?')
        if (!confirmed) return

        const removed = await removeFeatureFromConfig(featureId)
        window.alert(`Removed the following improvements: ${removed.length ? removed.join(', ') : 'None'}`)

        data.value = await fetchSkillTree()
        await nextTick()
        drawTree(data.value)
    } catch (e) {
        error.value = 'Could not remove improvement.'
    }
}
</script>

<template>
    <div class="flex justify-center p-8">
        <svg ref="svgRef"></svg>
        <CorpusSelection v-if="showCorpusModal" @close="showCorpusModal = false" @submit="handleCorpusSubmit" />
    </div>
</template>

<style scoped>
.link {
    stroke-width: 2px;
}

.node text {
    font-size: 12px;
    font-weight: 500;
    pointer-events: none !important;
    user-select: none;
    -webkit-user-select: none;
    -moz-user-select: none;
}

svg {
    width: 100%;
    height: auto;
    overflow: visible;
}

.node rect {
    transition: fill 0.25s ease, transform 0.2s ease;
}

.node rect:hover {
    transform: scale(1.05);
}

.node text {
    font-family: 'Inter', sans-serif;
    letter-spacing: 0.02em;
}
</style>
