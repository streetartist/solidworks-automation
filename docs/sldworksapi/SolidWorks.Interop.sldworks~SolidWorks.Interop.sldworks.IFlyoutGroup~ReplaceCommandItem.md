# ReplaceCommandItem Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup~ReplaceCommandItem`

Replaces a command item at the specified position.
Replaces a command item at the specified position.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ReplaceCommandItem( _
   ByVal Position As System.Integer, _
   ByVal Name As System.String, _
   ByVal HintString As System.String, _
   ByVal ImageListIndex As System.Integer, _
   ByVal CallbackFunction As System.String, _
   ByVal UpdateCallbackFunction As System.String _
) As System.Integer
```

```

Dim instance As IFlyoutGroup
Dim Position As System.Integer
Dim Name As System.String
Dim HintString As System.String
Dim ImageListIndex As System.Integer
Dim CallbackFunction As System.String
Dim UpdateCallbackFunction As System.String
Dim value As System.Integer
 
value = instance.ReplaceCommandItem(Position, Name, HintString, ImageListIndex, CallbackFunction, UpdateCallbackFunction)
```

```

System.int ReplaceCommandItem( 
   System.int Position,
   System.string Name,
   System.string HintString,
   System.int ImageListIndex,
   System.string CallbackFunction,
   System.string UpdateCallbackFunction
)
```

```

System.int ReplaceCommandItem( 
   System.int Position,
   System.String^ Name,
   System.String^ HintString,
   System.int ImageListIndex,
   System.String^ CallbackFunction,
   System.String^ UpdateCallbackFunction
) 
```

#### Parameters

*Position*
:   0-based index of the item to replace in the flyout

*Name*
:   Name of the item to add to the flyout

*HintString*
:   Text displayed in the SOLIDWORKS status bar when the pointer is on the item

*ImageListIndex*
:   Index of the image in the icon list assigned to the parent flyout (see **Remarks**)

*CallbackFunction*
:   Function to call when this item is selected

*UpdateCallbackFunction*
:   Optional function that controls the state of the item; if specified, then SOLIDWORKS calls this function before displaying the item

    |  |  |
    | --- | --- |
    | If your method returns... | Then the SOLIDWORKS software... |
    | 0 | Deselects and disables the item |
    | 1 | Deselects and enables the item; this is the default state if no update function is specified |
    | 2 | Selects and disables the item |
    | 3 | Selects and enables the item |
    | 4 | Hides the item |

Remarks

ImageListIndex is 0-based. The size of the index is equal to the number of images in the large or small graphic file for that flyout. See [IFlyoutGroup::LargeIconList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup~LargeIconList.md) and [IFlyoutGroup::SmallIconList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup~SmallIconList.md) for details.

You can use -1 for ImageListIndex to specify that no icon is needed.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFlyoutGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup.md)  
[IFlyoutGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup_members.md)  
[IFlyoutGroup::RemoveAllCommandItems Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup~RemoveAllCommandItems.md)  
[IFlyoutGroup::RemoveCommandItem Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup~RemoveCommandItem.md)  
[IFlyoutGroup::AddCommandItem Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup~AddCommandItem.md)
