# TabFace Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~TabFace`

Gets or sets the tab face that defines the tab thickness.
Gets or sets the tab face that defines the tab thickness.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TabFace As System.Object
```

```

Dim instance As ITabAndSlotGroupData
Dim value As System.Object
 
instance.TabFace = value
 
value = instance.TabFace
```

```

System.object TabFace {get; set;}
```

```

property System.Object^ TabFace {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

[IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

Remarks

The value of this property is a planar face that is shared with [ITabAndSlotGroupData::SelectionTabEdge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~SelectionTabEdge.md) of thickness, [ITabAndSlotGroupData::TabThickness](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~TabThickness.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITabAndSlotGroupData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData.md)  
[ITabAndSlotGroupData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData_members.md)
