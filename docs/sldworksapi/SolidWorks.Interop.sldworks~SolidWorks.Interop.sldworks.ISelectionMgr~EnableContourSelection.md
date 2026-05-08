# EnableContourSelection Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~EnableContourSelection`

Enables and disables contour selection.
Enables and disables contour selection.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property EnableContourSelection As System.Boolean
```

```

Dim instance As ISelectionMgr
Dim value As System.Boolean
 
instance.EnableContourSelection = value
 
value = instance.EnableContourSelection
```

```

System.bool EnableContourSelection {get; set;}
```

```

property System.bool EnableContourSelection {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to enable contour selection, false to disable it

Remarks

This property enables you to select regions that are defined by single, multiple, open, or closed sketch boundaries. See the SOLIDWORKS Help for more information about selecting contours.

Example

[Enable Contour Selection (VBA)](Enable_Contour_Selection_Example_VB.htm)  
[Enable Contour Selection (VB.NET)](Enable_Contour_Selection_Example_VBNET.htm)  
[Enable Contour Selection (C#)](Enable_Contour_Selection_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.md)  
[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.md)  
[ISelectionMgr::EnableSelection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~EnableSelection.md)
