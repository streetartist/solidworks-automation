# ISetFixedPoint Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~ISetFixedPoint`

Sets the fixed-point x, y, z coordinates for this jog feature.
Sets the fixed-point x, y, z coordinates for this jog feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetFixedPoint( _
   ByRef Point As System.Double _
) 
```

```

Dim instance As IJogFeatureData
Dim Point As System.Double
 
instance.ISetFixedPoint(Point)
```

```

void ISetFixedPoint( 
   ref System.double Point
)
```

```

void ISetFixedPoint( 
   System.double% Point
) 
```

#### Parameters

*Point*
:   - in-process, unmanaged C++: Pointer to an array of fixed-point coordinates

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IJogFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData.md)  
[IJogFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData_members.md)  
[IJogFeatureData::IGetFixedPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~IGetFixedPoint.md)  
[IJogFeatureData::FixedPoint Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~FixedPoint.md)
