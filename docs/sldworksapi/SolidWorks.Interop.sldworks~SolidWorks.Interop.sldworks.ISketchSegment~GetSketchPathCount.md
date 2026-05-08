# GetSketchPathCount Method (ISketchSegment)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~GetSketchPathCount`

Gets the number of sketch paths for this sketch segment
Gets the number of sketch paths for this sketch segment

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSketchPathCount() As System.Integer
```

```

Dim instance As ISketchSegment
Dim value As System.Integer
 
value = instance.GetSketchPathCount()
```

```

System.int GetSketchPathCount()
```

```

System.int GetSketchPathCount(); 
```

#### Return Value

Number of sketch paths

Remarks

Call this method before calling [ISketchSegment::IGetSketchPaths](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~IGetSketchPaths.md) to get the size of the array for that method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md)  
[ISketchSegment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment_members.md)  
[ISketchSegment::GetSketchPaths Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~GetSketchPaths.md)
