# SelectionStartReferencePoint Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~SelectionStartReferencePoint`

Gets or sets the start location of this Tab and Slot group.
Gets or sets the start location of this Tab and Slot group.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SelectionStartReferencePoint As System.Object
```

```

Dim instance As ITabAndSlotGroupData
Dim value As System.Object
 
instance.SelectionStartReferencePoint = value
 
value = instance.SelectionStartReferencePoint
```

```

System.object SelectionStartReferencePoint {get; set;}
```

```

property System.Object^ SelectionStartReferencePoint {
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
[ITabAndSlotGroupData::SelectionEndReferencePoint Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~SelectionEndReferencePoint.md)
