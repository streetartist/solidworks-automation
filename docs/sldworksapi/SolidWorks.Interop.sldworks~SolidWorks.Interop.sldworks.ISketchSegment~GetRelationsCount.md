# GetRelationsCount Method (ISketchSegment)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~GetRelationsCount`

Gets the number of sketch relations for this sketch segment.
Gets the number of sketch relations for this sketch segment.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetRelationsCount() As System.Integer
```

```

Dim instance As ISketchSegment
Dim value As System.Integer
 
value = instance.GetRelationsCount()
```

```

System.int GetRelationsCount()
```

```

System.int GetRelationsCount(); 
```

#### Return Value

Number of sketch relations for this sketch segment

Remarks

Call this method before calling [ISketchSegment::IGetRelations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~IGetRelations.md) to get the size of the array for that method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md)  
[ISketchSegment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment_members.md)  
[ISketchSegment::GetRelations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~GetRelations.md)
