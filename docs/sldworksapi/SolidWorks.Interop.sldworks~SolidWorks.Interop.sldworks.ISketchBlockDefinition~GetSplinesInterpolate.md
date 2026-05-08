# GetSplinesInterpolate Method (ISketchBlockDefinition)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetSplinesInterpolate`

Gets all of the parameers of the splines by interpolation instead of by tessellation as is done by ISketch::GetSplines2 and ISketch::IGetSplines2.
Gets all of the parameers of the splines by interpolation instead of by tessellation as is done by [ISketch::GetSplines2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetSplines2.md) and [ISketch::IGetSplines2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~IGetSplines2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSplinesInterpolate() As System.Object
```

```

Dim instance As ISketchBlockDefinition
Dim value As System.Object
 
value = instance.GetSplinesInterpolate()
```

```

System.object GetSplinesInterpolate()
```

```

System.Object^ GetSplinesInterpolate(); 
```

#### Return Value

Array of doubles (see **Remarks**)

Remarks

The return value is an array of doubles formatted as:

[ [NumSplinePoints, [x, y, z] ], ]

This complete set of data repeats itself for each spline found in the sketch block definition. For each spline, the array returned contains the number of spline points in the spline, and the X,Y,Z value for each of those points.

The [x,y,z] parameter is an array of NumSplinePoints. For example, if your sketch block definition has two splines and each spline has three points, then the data would be in the following format:

[ 3, x1\_1, y1\_1, z1\_1, x2\_1, y2\_1, z2\_1, x3\_1, y3\_1, z3\_1, 3, x1\_2, y1\_2, z1\_2, x2\_2, y2\_2, z2\_2, x3\_2, y3\_2, z3\_2 ]

The [x,y,z] points for each spline are the same points used to generate the spline.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.md)  
[ISketchBlockDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition_members.md)  
[ISketchBlockDefinition::GetSplineInterpolateCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetSplineInterpolateCount.md)  
[ISketchBlockDefinition::IGetSplinesInterpolate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~IGetSplinesInterpolate.md)  
[ISketchBlockDefinition::GetSplineCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetSplineCount.md)  
[ISketchBlockDefinition::GetSplineParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetSplineParams.md)  
[ISketchBlockDefinition::GetSplineParamsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetSplineParamsCount.md)  
[ISketchBlockDefinition::IGetSplineParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~IGetSplineParams.md)
