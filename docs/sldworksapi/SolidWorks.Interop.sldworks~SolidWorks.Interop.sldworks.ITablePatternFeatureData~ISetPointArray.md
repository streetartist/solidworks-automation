# ISetPointArray Method (ITablePatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~ISetPointArray`

Sets the points that describe the x, y, and z locations of the repeating elements in the table-driven pattern feature.
Sets the points that describe the x, y, and z locations of the repeating elements in the table-driven pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetPointArray( _
   ByVal FeatCount As System.Integer, _
   ByRef ArrayDataIn As System.Double _
) 
```

```

Dim instance As ITablePatternFeatureData
Dim FeatCount As System.Integer
Dim ArrayDataIn As System.Double
 
instance.ISetPointArray(FeatCount, ArrayDataIn)
```

```

void ISetPointArray( 
   System.int FeatCount,
   ref System.double ArrayDataIn
)
```

```

void ISetPointArray( 
   System.int FeatCount,
   System.double% ArrayDataIn
) 
```

#### Parameters

*FeatCount*
:   Number of seed features for the table-driven pattern feature

*ArrayDataIn*
:   - in-process, unmanaged C++: Pointer to an array of points that describe the x, y, and z locations of the repeating elements in the table-driven pattern

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

The array of doubles, which describe the x, y, and z locations, is the number of repeating elements \* 3:

[ point1x, point1y, point1z, point2x, point2y, point2z, ... ]

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITablePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData.md)  
[ITablePatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData_members.md)  
[ITablePatternFeatureData::IGetPointArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~IGetPointArray.md)  
[ITablePatternFeatureData::PointArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~PointArray.md)  
[ITablePatternFeatureData::GetPointCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~GetPointCount.md)
