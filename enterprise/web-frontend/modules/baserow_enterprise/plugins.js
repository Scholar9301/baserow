import { BaserowPlugin } from '@baserow/modules/core/plugins'
import ChatwootSupportSidebarWorkspace from '@baserow_enterprise/components/ChatwootSupportSidebarWorkspace'
import MemberRolesDatabaseContextItem from '@baserow_enterprise/components/member-roles/MemberRolesDatabaseContextItem'
import MemberRolesTableContextItem from '@baserow_enterprise/components/member-roles/MemberRolesTableContextItem'
import EnterpriseFeatures from '@baserow_enterprise/features'
import SnapshotModalWarning from '@baserow_enterprise/components/SnapshotModalWarning'

export class EnterprisePlugin extends BaserowPlugin {
  static getType() {
    return 'enterprise'
  }

  getSidebarWorkspaceComponent(workspace) {
    const supportEnabled = this.app.$hasFeature(
      EnterpriseFeatures.SUPPORT,
      workspace.id
    )
    return supportEnabled ? ChatwootSupportSidebarWorkspace : null
  }

  getAdditionalDatabaseContextComponents(workspace, database) {
    if (
      this.app.$hasFeature(EnterpriseFeatures.RBAC, workspace.id) &&
      this.app.$hasPermission('application.read_role', database, workspace.id)
    ) {
      return [MemberRolesDatabaseContextItem]
    } else {
      return []
    }
  }

  getAdditionalTableContextComponents(workspace, table) {
    if (
      this.app.$hasFeature(EnterpriseFeatures.RBAC, workspace.id) &&
      this.app.$hasPermission('database.table.read_role', table, workspace.id)
    ) {
      return [MemberRolesTableContextItem]
    } else {
      return []
    }
  }

  getExtraSnapshotModalComponents(workspace) {
    const rbacSupport = this.app.$hasFeature(
      EnterpriseFeatures.RBAC,
      workspace.id
    )
    return rbacSupport ? SnapshotModalWarning : null
  }
}
