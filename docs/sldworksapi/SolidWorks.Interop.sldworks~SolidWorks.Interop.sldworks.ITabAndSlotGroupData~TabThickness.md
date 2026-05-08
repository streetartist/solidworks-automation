# TabThickness Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~TabThickness`

Gets or sets the tab thickness.
Gets or sets the tab thickness.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TabThickness As System.Double
```

```

Dim instance As ITabAndSlotGroupData
Dim value As System.Double
 
instance.TabThickness = value
 
value = instance.TabThickness
```

```

System.double TabThickness {get; set;}
```

```

property System.double TabThickness {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Tab thickness

Remarks

This property defines the thickness of [ITabAndSlotGroupData::TabFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~TabFace.md), which is a planar face shared with [ITabAndSlotGroupData::SelectionTabEdge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~SelectionTabEdge.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITabAndSlotGroupData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData.md)  
[ITabAndSlotGroupData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData_members.md)
