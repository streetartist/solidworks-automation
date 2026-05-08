# IGetSketchRegions Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSketchRegions`

Gets the sketch regions in this sketch.
Gets the sketch regions in this sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetSketchRegions( _
   ByVal Count As System.Integer _
) As SketchRegion
```

```

Dim instance As ISketch
Dim Count As System.Integer
Dim value As SketchRegion
 
value = instance.IGetSketchRegions(Count)
```

```

SketchRegion IGetSketchRegions( 
   System.int Count
)
```

```

SketchRegion^ IGetSketchRegions( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of sketch regions

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [sketch regions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRegion.md)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [ISketch::GetSketchRegionCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchRegionCount.md) to get Count.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)  
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.md)  
[ISketch::GetSketchRegions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchRegions.md)
