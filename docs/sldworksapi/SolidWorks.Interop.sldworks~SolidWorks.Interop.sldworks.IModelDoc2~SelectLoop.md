# SelectLoop Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SelectLoop`

Selects the loop that corresponds to the selected edge.
Selects the loop that corresponds to the selected edge.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SelectLoop() 
```

```

Dim instance As IModelDoc2
 
instance.SelectLoop()
```

```

void SelectLoop()
```

```

void SelectLoop(); 
```

Remarks

This method associates the loop with the selected edge in the [ISelectionMgr](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.md); it does not add an item  to the ISelectionMgr. To find out if the selected edge has an associated loop, use [ISelectionMgr::GetSelectedObjectLoop2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectLoop2.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
