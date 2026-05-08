# IGetSketchPoints2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSketchPoints2`

Gets the sketch points in this sketch.
Gets the sketch points in this sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetSketchPoints2( _
   ByVal Count As System.Integer _
) As SketchPoint
```

```

Dim instance As ISketch
Dim Count As System.Integer
Dim value As SketchPoint
 
value = instance.IGetSketchPoints2(Count)
```

```

SketchPoint IGetSketchPoints2( 
   System.int Count
)
```

```

SketchPoint^ IGetSketchPoints2( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of sketch points in this sketch

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [sketch points](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.md) in this sketch

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Call [ISketch::GetSketchPointsCount2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchPointsCount2.md) before calling this method to get the number of sketch points in this sketch.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)  
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.md)  
[ISketch::GetSketchPoints2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchPoints2.md)  
[ISketch::GetUserPoints2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetUserPoints2.md)  
[ISketch::GetUserPointsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetUserPointsCount.md)  
[ISketch::IGetUserPoints2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetUserPoints2.md)  
[ISketch::IEnumSketchPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IEnumSketchPoints.md)  
[ISketchPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.md)  
[ISketch::MergePoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~MergePoints.md)
