# PointArray Property (ITablePatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~PointArray`

Gets or sets the array of points that describe the x,y, and z locations of the repeating elements in the table-driven pattern feature.
Gets or sets the array of points that describe the x,y, and z locations of the repeating elements in the table-driven pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PointArray As System.Object
```

```

Dim instance As ITablePatternFeatureData
Dim value As System.Object
 
instance.PointArray = value
 
value = instance.PointArray
```

```

System.object PointArray {get; set;}
```

```

property System.Object^ PointArray {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of doubles that describe the x, y, and z locations of the repeating elements in the table-driven pattern

Remarks

The points returned are based on the table-driven pattern's coordinate system.

The array of doubles describe the x, y, and z locations of the repeating elements in the table-driven pattern. The size of the array is the number of repeating elements \* 3:

[ point1x, point1y, point1z, point2x, point2y, point2z, ... ]

Use [ITablePatternFeatureData:: GetPointCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~GetPointCount.md) to get the number of points in the array.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Example

See the [ITablePatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData.md) example.

Example

[Get Points of Repeating Elements in Table-driven Pattern (C#)](Get_Points_of_Repeating_Elements_in_Table-driven_Pattern_Example_CSharp.htm)  
[Get Points of Repeating Elements in Table-driven Pattern (VB.NET)](Get_Points_of_Repeating_Elements_in_Table-driven_Pattern_Example_VBNET.htm)  
[Get Points of Repeating Elements in Table-driven Pattern (VBA)](Get_Points_of_Repeating_Elements_in_Table-driven_Pattern_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITablePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData.md)  
[ITablePatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData_members.md)  
[ITablePatternFeatureData::IGetPointArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~IGetPointArray.md)  
[ITablePatternFeatureData::ISetPointArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~ISetPointArray.md)
