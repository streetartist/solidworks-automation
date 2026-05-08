# RemoveVisibleBox Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RemoveVisibleBox`

Removes the visible bounding box set by IModelDocExtension::SetVisibleBox and resets the size of the bounding box to the size calculated by SOLIDWORKS for a part or an assembly.
Removes the visible bounding box set by [IModelDocExtension::SetVisibleBox](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetVisibleBox.md) and resets the size of the bounding box to the size calculated by SOLIDWORKS for a part or an assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub RemoveVisibleBox() 
```

```

Dim instance As IModelDocExtension
 
instance.RemoveVisibleBox()
```

```

void RemoveVisibleBox()
```

```

void RemoveVisibleBox(); 
```

Example

[Set Visible Bounding Box for Zoom to Fit (C#)](Set_Visible_Bounding_Box_for_Zoom_to_Fit_Example_CSharp.htm)  
[Set Visible Bounding Box for Zoom to Fit (VB.NET)](Set_Visible_Bounding_Box_for_Zoom_to_Fit_Example_VBNET.htm)  
[Set Visible Bounding Box for Zoom to Fit (VBA)](Set_Visible_Bounding_Box_for_Zoom_to_Fit_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::GetVisibleBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetVisibleBox.md)
