# IGetSketchPaths Method (ISketchSegment)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~IGetSketchPaths`

Gets the sketch paths in this sketch segment.
Gets the sketch paths in this sketch segment.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetSketchPaths( _
   ByVal Count As System.Integer _
) As SketchPath
```

```

Dim instance As ISketchSegment
Dim Count As System.Integer
Dim value As SketchPath
 
value = instance.IGetSketchPaths(Count)
```

```

SketchPath IGetSketchPaths( 
   System.int Count
)
```

```

SketchPath^ IGetSketchPaths( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of sketch paths

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [sketch paths](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath.md)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [ISketchSegment::GetSketchPathCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~GetSketchPathCount.md) to get the value of Count.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md)  
[ISketchSegment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment_members.md)  
[ISketchSegment::GetSketchPaths Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~GetSketchPaths.md)
