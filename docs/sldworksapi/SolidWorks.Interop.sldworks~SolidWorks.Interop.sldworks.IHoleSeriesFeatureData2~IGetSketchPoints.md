# IGetSketchPoints Method (IHoleSeriesFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~IGetSketchPoints`

Gets the center-hole sketch points in this hole series.
Gets the center-hole sketch points in this hole series.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetSketchPoints( _
   ByVal NCount As System.Integer _
) As SketchPoint
```

```

Dim instance As IHoleSeriesFeatureData2
Dim NCount As System.Integer
Dim value As SketchPoint
 
value = instance.IGetSketchPoints(NCount)
```

```

SketchPoint IGetSketchPoints( 
   System.int NCount
)
```

```

SketchPoint^ IGetSketchPoints( 
   System.int NCount
) 
```

#### Parameters

*NCount*
:   Number of center-hole sketch points

#### Return Value

- in-process, unmanaged C++: Pointer to an array of center-hole [sketch points](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.md)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [IHoleSeriesFeatureData2::GetSketchPointsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~GetSketchPointsCount.md) to get the value for NCount.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IHoleSeriesFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2.md)  
[IHoleSeriesFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2_members.md)  
[IHoleSeriesFeatureData2::GetSketchPoints Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~GetSketchPoints.md)
