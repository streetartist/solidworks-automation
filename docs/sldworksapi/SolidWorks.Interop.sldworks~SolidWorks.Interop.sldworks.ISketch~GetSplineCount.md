# GetSplineCount Method (ISketch)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineCount`

Gets the number of splines in this sketch.
Gets the number of splines in this sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSplineCount( _
   ByRef PointCount As System.Integer _
) As System.Integer
```

```

Dim instance As ISketch
Dim PointCount As System.Integer
Dim value As System.Integer
 
value = instance.GetSplineCount(PointCount)
```

```

System.int GetSplineCount( 
   ref System.int PointCount
)
```

```

System.int GetSplineCount( 
   System.int% PointCount
) 
```

#### Parameters

*PointCount*
:   Number of points in this sketch

#### Return Value

Number of splines in the sketch

Remarks

Call this method before calling [ISketch::IGetSplines](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSplines.md) to get the size of the array for that method.

Example

[Get Each Spline's Parameters (C#)](Get_Each_Splines_Parameters_Example_CSharp.htm)  
[Get Each Spline's Parameters (VB.NET)](Get_Each_Splines_Parameters_Example_VBNET.htm)  
[Get Each Spline's Parameters (VBA)](Get_Each_Splines_Parameters_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)  
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.md)  
[ISketch::GetSplines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplines.md)  
[ISketch::GetSplineParamsCount2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineParamsCount2.md)  
[ISketch::GetSplinesInterpolate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplinesInterpolate.md)  
[ISketch::GetSplineParams2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineParams2.md)  
[ISketch::GetSplineInterpolateCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineInterpolateCount.md)  
[ISketch::IGetSplineParams2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSplineParams2.md)  
[ISketch::IGetSplinesInterpolate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSplinesInterpolate.md)
