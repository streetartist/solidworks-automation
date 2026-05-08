# IGetPointArray Method (ITablePatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~IGetPointArray`

Gets an array of doubles that describe the x, y, and z locations of the repeating elements in this table-driven pattern feature.
Gets an array of doubles that describe the x, y, and z locations of the repeating elements in this table-driven pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetPointArray() As System.Double
```

```

Dim instance As ITablePatternFeatureData
Dim value As System.Double
 
value = instance.IGetPointArray()
```

```

System.double IGetPointArray()
```

```

System.double IGetPointArray(); 
```

#### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles that describe the x, y, and z locations of the repeating elements in this table-driven pattern feature

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

The points returned are based on the table-driven pattern's coordinate system.

The array of doubles, which describe the x, y, and z locations, is the number of repeating elements \* 3:

[ point1x, point1y, point1z, point2x, point2y, point2z, ... ]

To get the number of points, call [ITablePatternFeatureData::GetPointCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~GetPointCount.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITablePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData.md)  
[ITablePatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData_members.md)  
[ITablePatternFeatureData::ISetPointArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~ISetPointArray.md)  
[ITablePatternFeatureData::PointArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~PointArray.md)
