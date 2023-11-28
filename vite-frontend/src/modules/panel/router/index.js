import Panel from "@/view/UserPanel.vue";
import Profil from "../view/ProfilPage.vue";
import Statistics from "../view/UserStatistics.vue";
import Learning from "../view/LearningPage.vue";
import Equipment from "../view/EquipmentUser.vue";


const PanelRouter = {
  path: "/panel",
  component: Panel,
  children: [
    {
      path: "",
      components: {
        default: Statistics,
      },
    },
    {
      path: "profil",
      components: {
        default: Profil,
      },
    },
    {
      path: "learning",
      components: {
        default: Learning,
      },
    },
    {
      path: "equipment",
      components: {
        default: Equipment,
      },
    },
  ],
};
export default PanelRouter;
