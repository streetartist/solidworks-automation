# GetSketchPointsCount Method (IHoleSeriesFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~GetSketchPointsCount`

Gets the number of center-hole sketch points in this hole series.
Gets the number of center-hole sketch points in this hole series.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSketchPointsCount() As System.Integer
```

```

Dim instance As IHoleSeriesFeatureData2
Dim value As System.Integer
 
value = instance.GetSketchPointsCount()
```

```

System.int GetSketchPointsCount()
```

```

System.int GetSketchPointsCount(); 
```

#### Return Value

Number of center-hole sketch points in this hole series

Remarks

Call this method before calling [IHoleSeriesFeatureData::IGetSketchPoints](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~IGetSketchPoints.md) to get the size of the array for that method.

Example

See the examples in [IHoleSeriesFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IHoleSeriesFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2.md)  
[IHoleSeriesFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2_members.md)  
[IHoleSeriesFeatureData2::GetSketchPoints Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~GetSketchPoints.md)
