# ICommandGroup Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup_members`

Allows add-in applications to create toolbars and menu items, including flyout toolbars and submenus, and add them to the ICommandManager.
The following tables list the members exposed by [ICommandGroup](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [CommandID](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~CommandID.md) | Gets the command ID for the specified item in the CommandGroup. |
| Property | [CustomNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~CustomNames.md) | Gets or sets the custom names in the CommandGroup. |
| Property | [DockingState](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~DockingState.md) | Gets or sets the docking state of the toolbar in the CommandGroup. |
| Property | [HasEnabledButton](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~HasEnabledButton.md) | Gets whether any buttons in this CommandGroup are enabled. |
| Property | [HasMenu](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~HasMenu.md) | Gets or sets whether this CommandGroup has a menu. |
| Property | [HasToolbar](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~HasToolbar.md) | Gets or sets whether this CommandGroup has a toolbar. |
| Property | [IconList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~IconList.md) | Gets or sets the paths for the icons for the toolbar buttons and separators for this CommandGroup. |
| Property | [LargeIconList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~LargeIconList.md) | Obsolete. Superseded by [ICommandGroup::IconList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~IconList.md). |
| Property | [LargeMainIcon](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~LargeMainIcon.md) | Obsolete. Superseded by [ICommandGroup::MainIconList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~MainIconList.md). |
| Property | [MainIconList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~MainIconList.md) | Gets or sets the paths for the icons for the buttons for this CommandGroup. |
| Property | [MenuPosition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~MenuPosition.md) | Gets or sets the position of the CommandGroup for the specified document templates. |
| Property | [Name](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~Name.md) | Gets the name of the CommandGroup. |
| Property | [NumberOfGroupItems](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~NumberOfGroupItems.md) | Gets the number of items in the CommandGroup. |
| Property | [SelectType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~SelectType.md) | This property:   - gets the type of object selected on the context sensitive, pop-up menu. - sets the type of object that the user must select to show the context sensitive, pop-up menu. |
| Property | [ShowInDocumentType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~ShowInDocumentType.md) | Gets or sets the types of documents to show this CommandGroup. |
| Property | [SmallIconList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~SmallIconList.md) | Obsolete. Superseded by [ICommandGroup::IconList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~IconList.md). |
| Property | [SmallMainIcon](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~SmallMainIcon.md) | Obsolete. Superseded by [ICommandGroup::MainIconList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~MainIconList.md). |
| Property | [ToolbarId](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~ToolbarId.md) | Gets the toolbar ID of this CommandGroup. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [Activate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~Activate.md) | Activates the CommandGroup. |
| Method | [AddCommandItem](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~AddCommandItem.md) | Obsolete. Superseded by [ICommandGroup::AddComandItem2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~AddCommandItem2.md). |
| Method | [AddCommandItem2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~AddCommandItem2.md) | Adds a combination menu item and toolbar item to a CommandGroup. |
| Method | [AddSpacer](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~AddSpacer.md) | Obsolete. Superseded by [ICommandGroup::AddSpacer2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~AddSpacer2.md). |
| Method | [AddSpacer2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~AddSpacer2.md) | Adds a spacer between items in a CommandGroup. |
| Method | [GetToolbarVisibility](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~GetToolbarVisibility.md) | Gets whether this toolbar is visible. |
| Method | [SetToolbarVisibility](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~SetToolbarVisibility.md) | Sets the visibility of the toolbar in the CommandGroup. |

[Top](#top)

 

See Also

#### Reference

[ICommandGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
