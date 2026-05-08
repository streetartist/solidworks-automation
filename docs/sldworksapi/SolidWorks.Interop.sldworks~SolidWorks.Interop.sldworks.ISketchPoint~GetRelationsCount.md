# GetRelationsCount Method (ISketchPoint)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~GetRelationsCount`

Gets the number of sketch relations for this sketch point.
Gets the number of sketch relations for this sketch point.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetRelationsCount() As System.Integer
```

```

Dim instance As ISketchPoint
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

Number of sketch relations for this sketch point

Remarks

Call this method before calling [ISketchPoint::IGetRelations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~IGetRelations.md) to get the size of the array for that method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.md)  
[ISketchPoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint_members.md)  
[ISketchPoint::GetRelations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~GetRelations.md)
