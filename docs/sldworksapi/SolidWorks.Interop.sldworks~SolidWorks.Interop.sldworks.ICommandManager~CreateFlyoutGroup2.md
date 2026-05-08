# CreateFlyoutGroup2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~CreateFlyoutGroup2`

Creates a new flyout in the CommandManager and context-sensitive menus.
Creates a new flyout in the CommandManager and context-sensitive menus.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateFlyoutGroup2( _
   ByVal UserID As System.Integer, _
   ByVal Title As System.String, _
   ByVal ToolTip As System.String, _
   ByVal Hint As System.String, _
   ByVal MainIconList As System.Object, _
   ByVal IconList As System.Object, _
   ByVal CallbackFunction As System.String, _
   ByVal UpdateCallbackFunction As System.String _
) As FlyoutGroup
```

```

Dim instance As ICommandManager
Dim UserID As System.Integer
Dim Title As System.String
Dim ToolTip As System.String
Dim Hint As System.String
Dim MainIconList As System.Object
Dim IconList As System.Object
Dim CallbackFunction As System.String
Dim UpdateCallbackFunction As System.String
Dim value As FlyoutGroup
 
value = instance.CreateFlyoutGroup2(UserID, Title, ToolTip, Hint, MainIconList, IconList, CallbackFunction, UpdateCallbackFunction)
```

```

FlyoutGroup CreateFlyoutGroup2( 
   System.int UserID,
   System.string Title,
   System.string ToolTip,
   System.string Hint,
   System.object MainIconList,
   System.object IconList,
   System.string CallbackFunction,
   System.string UpdateCallbackFunction
)
```

```

FlyoutGroup^ CreateFlyoutGroup2( 
   System.int UserID,
   System.String^ Title,
   System.String^ ToolTip,
   System.String^ Hint,
   System.Object^ MainIconList,
   System.Object^ IconList,
   System.String^ CallbackFunction,
   System.String^ UpdateCallbackFunction
) 
```

#### Parameters

*UserID*
:   Unique user-defined ID for the new flyout

*Title*
:   Name of the flyout to create

*ToolTip*
:   ToolTip for the new flyout

*Hint*
:   Text displayed in SOLIDWORKS status bar when a user's mouse pointer is over the flyout

*MainIconList*
:   Array of strings for the paths to the image files for this flyout button (see **Remarks**)

*IconList*
:   Array of strings for the paths to the image files containing all of the flyout toolbar buttons and separators (see **Remarks**)

*CallbackFunction*
:   Function to call when the flyout is selected

*UpdateCallbackFunction*
:   Optional update function that controls the state of the item; if specified, then SOLIDWORKS calls this function before displaying the item (see **Remarks**)

    | If the update  function returns... | Then SOLIDWORKS... |
    | --- | --- |
    | 0 | Disables the item |
    | 1 | Enables the item; this is the default state if no update function is specified |

#### Return Value

[IFlyoutGroup](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup.md)

Remarks

After creating the flyout, display it on a CommandManager tab by calling [ICommandTabBox::AddCommands](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTabBox~AddCommands.md). Call:

- [IFlyoutGroup::AddContextMenuFlyout](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup~AddContextMenuFlyout.md) to add the flyout to context menus.
- [IFlyoutGroup::AddCommandItem](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup~AddCommandItem.md) to add menu items to the flyout group.

If any flyout menu items are enabled, then the flyout button cannot be disabled by the flyout group's UpdateCallbackFunction. The sensitivity of the top-level flyout button is always determined by its enabled menu items. Disabled flyout menu items do not appear in the flyout menu. If there are no flyout menu items, then control of the top-level flyout button is returned to the flyout group's UpdateCallbackFunction.

This method supports scaling for high resolution screens with high resolution operating system scaling options.

The array of strings for the paths to the image files for MainIconList and IconList can contain images of the following sizes:

- 20 x 20 pixels
- 32 x 32 pixels
- 40 x 40 pixels
- 64 x 64 pixels
- 96 x 96 pixels
- 128 x128 pixels

The order in which you specify the image files must be the same for MainIconList and IconList. For example, if you specify an array of paths to 20 x 20 pixels, 32 x 32 pixels, and 40 x 40 pixels images for MainIconList, then you must specify an array of paths to 20 x 20 pixels, 32 x 32 pixels, and 40 x 40 pixels images for IconList. The images should use a 256-color palette.

Example

[Create Flyouts in the CommandManager (C#)](Create_Flyouts_in_the_CommandManager_Example_CSharp.htm)  
[Create Flyouts in the CommandManager (VB.NET)](Create_Flyouts_in_the_CommandManager_Example_VBNET.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICommandManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager.md)  
[ICommandManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager_members.md)  
[ICommandManager::GetFlyoutGroup Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetFlyoutGroup.md)  
[ICommandManager::GetFlyoutGroups Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetFlyoutGroups.md)  
[ICommandManager::RemoveFlyoutGroup Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~RemoveFlyoutGroup.md)  
[ICommandManager::NumberOfFlyoutGroups Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~NumberOfFlyoutGroups.md)  
[ISldWorks::GetImageSize Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetImageSize.md)
