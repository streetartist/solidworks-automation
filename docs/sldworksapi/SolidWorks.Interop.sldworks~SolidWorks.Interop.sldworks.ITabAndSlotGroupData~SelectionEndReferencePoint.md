# SelectionEndReferencePoint Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~SelectionEndReferencePoint`

Gets or sets the end location of this Tab and Slot group.
Gets or sets the end location of this Tab and Slot group.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SelectionEndReferencePoint As System.Object
```

```

Dim instance As ITabAndSlotGroupData
Dim value As System.Object
 
instance.SelectionEndReferencePoint = value
 
value = instance.SelectionEndReferencePoint
```

```

System.object SelectionEndReferencePoint {get; set;}
```

```

property System.Object^ SelectionEndReferencePoint {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

[IVertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md) or [ISketchPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITabAndSlotGroupData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData.md)  
[ITabAndSlotGroupData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData_members.md)  
[ITabAndSlotGroupData::SelectionStartReferencePoint Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~SelectionStartReferencePoint.md)
