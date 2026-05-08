# IGetSplinesInterpolate Method (ISketch)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSplinesInterpolate`

Gets the spline points by interpolation instead of by tessellation as is done by ISketch::GetSplines and ISketch::IGetSplines.
Gets the spline points by interpolation instead of by tessellation as is done by [ISketch::GetSplines](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplines.md) and [ISketch::IGetSplines](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSplines.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetSplinesInterpolate() As System.Double
```

```

Dim instance As ISketch
Dim value As System.Double
 
value = instance.IGetSplinesInterpolate()
```

```

System.double IGetSplinesInterpolate()
```

```

System.double IGetSplinesInterpolate(); 
```

#### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

To determine the size of the array returned, call [ISketch:GetSplineInterpolateCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplinesInterpolate.md).

The return value is an array of doubles formatted as:

[ [NumSplinePoints, [x, y, z] ], ]

This complete set of data repeats itself for each spline found in the sketch. For each spline, the array returned contains the number of spline points in the spline, and the X,Y,Z value for each of those points.

The [x,y,z] parameter is an array of NumSplinePoints. For example, if your sketch has two splines and each spline has three points, then the data would be in the following format:

[ 3, x1\_1, y1\_1, z1\_1, x2\_1, y2\_1, z2\_1, x3\_1, y3\_1, z3\_1, 3, x1\_2, y1\_2, z1\_2, x2\_2, y2\_2, z2\_2, x3\_2, y3\_2, z3\_2 ]

The [x,y,z] points for each spline are the same points used to generate the spline.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)  
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.md)  
[ISketch::GetSplinesInterpolate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplinesInterpolate.md)  
[ISketch::GetSplineCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineCount.md)  
[ISketch::GetSplineParams2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineParams2.md)  
[ISketch::GetSplineParamsCount2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineParamsCount2.md)  
[ISketch::IGetSplineParams2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSplineParams2.md)
