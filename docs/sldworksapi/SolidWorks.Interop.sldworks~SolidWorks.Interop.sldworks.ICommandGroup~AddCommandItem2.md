# AddCommandItem2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~AddCommandItem2`

Adds a combination menu item and toolbar item to a CommandGroup.
Adds a combination menu item and toolbar item to a CommandGroup.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddCommandItem2( _
   ByVal Name As System.String, _
   ByVal Position As System.Integer, _
   ByVal HintString As System.String, _
   ByVal ToolTip As System.String, _
   ByVal ImageListIndex As System.Integer, _
   ByVal CallbackFunction As System.String, _
   ByVal EnableMethod As System.String, _
   ByVal UserID As System.Integer, _
   ByVal MenuTBOption As System.Integer _
) As System.Integer
```

```

Dim instance As ICommandGroup
Dim Name As System.String
Dim Position As System.Integer
Dim HintString As System.String
Dim ToolTip As System.String
Dim ImageListIndex As System.Integer
Dim CallbackFunction As System.String
Dim EnableMethod As System.String
Dim UserID As System.Integer
Dim MenuTBOption As System.Integer
Dim value As System.Integer
 
value = instance.AddCommandItem2(Name, Position, HintString, ToolTip, ImageListIndex, CallbackFunction, EnableMethod, UserID, MenuTBOption)
```

```

System.int AddCommandItem2( 
   System.string Name,
   System.int Position,
   System.string HintString,
   System.string ToolTip,
   System.int ImageListIndex,
   System.string CallbackFunction,
   System.string EnableMethod,
   System.int UserID,
   System.int MenuTBOption
)
```

```

System.int AddCommandItem2( 
   System.String^ Name,
   System.int Position,
   System.String^ HintString,
   System.String^ ToolTip,
   System.int ImageListIndex,
   System.String^ CallbackFunction,
   System.String^ EnableMethod,
   System.int UserID,
   System.int MenuTBOption
) 
```

#### Parameters

*Name*
:   Name of the item to add to the CommandGroup

*Position*
:   Position of the item within the CommandGroup

    **NOTE:** Specify 0 to add this item to the beginning of the CommandGroup, or specify -1 to add it to the end of the CommandGroup. This argument specifies the position of the item in relation to its immediate parent item.

*HintString*
:   Text displayed in the SOLIDWORKS status bar when the pointer is on the item

*ToolTip*
:   ToolTip displayed when the pointer is on the item

*ImageListIndex*
:   Index number of the image for the item in the parent CommandGroup (see **Remarks**)

*CallbackFunction*
:   Function to call when this item is selected (see **Remarks**)

*EnableMethod*
:   Optional function that controls the state of the item; if specified, then SOLIDWORKS calls this function before displaying the item 

    | **If your method  returns...** | **Then SOLIDWORKS...** |
    | --- | --- |
    | 0 | Deselects and disables the item |
    | 1 | Deselects and enables the item; this is the default state if no update function is specified |
    | 2 | Selects and disables the item |
    | 3 | Selects and enables the item |
    | 4 | Not supported |

    (see **Remarks**)

*UserID*
:   User-defined command ID or 0 if not used

*MenuTBOption*
:   Command item type as defined in [swCommandItemType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCommandItemType_e.html)

#### Return Value

Index of the item within the CommandGroup as assigned by SOLIDWORKS

Remarks

See [Add-in Callback and Enable Methods](sldworksapiprogguide.chm::/OVERVIEW/Add-in_Callbacks.htm) to learn how to specify CallbackFunction and EnableMethod.

ImageListIndex is 0-based. The size of the index is equal to number of the images in the image files for that CommandGroup. See [ICommandGroup::IconList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~IconList.md) for details. You can use -1 for ImageListIndex to specify that no icon is needed for a command item of type swCommandItemType\_e.swMenuItem; however, command items of type swCommandItemType\_e.swToolbarItem always need an icon.

Example

[Create Flyouts in the CommandManager (C#)](Create_Flyouts_in_the_CommandManager_Example_CSharp.htm)  
[Create Flyouts in the CommandManager (VB.NET)](Create_Flyouts_in_the_CommandManager_Example_VBNET.htm)  
[Create Submenus in the CommandManager (C#)](Create_Submenus_in_the_CommandManager_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICommandGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup.md)  
[ICommandGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup_members.md)  
[ICommandGroup::CommandID Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~CommandID.md)  
[ISldWorks::GetCommandID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCommandID.md)  
[ICommandGroup::HasEnabledButton Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~HasEnabledButton.md)
