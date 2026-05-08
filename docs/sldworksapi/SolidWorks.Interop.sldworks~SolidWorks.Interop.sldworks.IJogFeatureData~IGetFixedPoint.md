# IGetFixedPoint Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~IGetFixedPoint`

Gets the fixed-point x, y, z coordinates for this jog feature.
Gets the fixed-point x, y, z coordinates for this jog feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetFixedPoint() As System.Double
```

```

Dim instance As IJogFeatureData
Dim value As System.Double
 
value = instance.IGetFixedPoint()
```

```

System.double IGetFixedPoint()
```

```

System.double IGetFixedPoint(); 
```

#### Return Value

- in-process, unmanaged C++: Pointer to an array of fixed-point coordinates

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
[IJogFeatureData::ISetFixedPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~ISetFixedPoint.md)  
[IJogFeatureData::FixedPoint Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~FixedPoint.md)
