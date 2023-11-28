<template>
  <div ref="container" style="width: 100%; height: 100%;"></div>
</template>

<script>
import * as THREE from "three";

export default {
  mounted() {
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer({ antialias: true });

    renderer.setSize(this.$refs.container.clientWidth, this.$refs.container.clientHeight);
    this.$refs.container.appendChild(renderer.domElement);

    renderer.setClearColor(0x000000, 0);

    camera.position.set(0, 3, 8);
    camera.lookAt(0, 1, 0);

    // Materiał dla skrzyni (brązowy)
    const boxMaterial = new THREE.MeshBasicMaterial({ color: 0x8B4513 });

    // Geometria dla skrzyni
    const boxGeometry = new THREE.BoxGeometry(6, 4, 4);

    const group = new THREE.Group();

    // Skrzynia
    const box = new THREE.Mesh(boxGeometry, boxMaterial);
    group.add(box);

    // Materiał dla wieka (biały)
    const lidMaterial = new THREE.MeshBasicMaterial({ color: 0x60391c });

    // Geometria dla wieka
    const lidGeometry = new THREE.BoxGeometry(6, 1, 4);

    // Wieko
    const lid = new THREE.Mesh(lidGeometry, lidMaterial);
    lid.position.set(0, 2.5, 0); // Umieść wieko na skrzyni
    group.add(lid);

    scene.add(group);

    // Renderowanie
    const animate = () => {
      requestAnimationFrame(animate);

      // Obrót grupy (czyli skrzyni wraz z wiekiem)
      group.rotation.y += 0.01;

      renderer.render(scene, camera);
    };

    animate();

    window.addEventListener("resize", () => {
      const newWidth = this.$refs.container.clientWidth;
      const newHeight = this.$refs.container.clientHeight;

      camera.aspect = newWidth / newHeight;
      camera.updateProjectionMatrix();

      renderer.setSize(newWidth, newHeight);
    });
  },
};
</script>
