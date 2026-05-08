# GetSplineParams5 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineParams5`

Gets the parameterization data of the specified spline in this sketch.
Gets the parameterization data of the specified spline in this sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSplineParams5( _
   ByVal ForceNonPeriodic As System.Boolean, _
   ByVal Index As System.Integer _
) As System.Object
```

```

Dim instance As ISketch
Dim ForceNonPeriodic As System.Boolean
Dim Index As System.Integer
Dim value As System.Object
 
value = instance.GetSplineParams5(ForceNonPeriodic, Index)
```

```

System.object GetSplineParams5( 
   System.bool ForceNonPeriodic,
   System.int Index
)
```

```

System.Object^ GetSplineParams5( 
   System.bool ForceNonPeriodic,
   System.int Index
) 
```

#### Parameters

*ForceNonPeriodic*
:   True to attempt to convert a non-periodic spline to a periodic one, false to not

*Index*
:   0-based index indicating the spline whose parameterization data to get

#### Return Value

[ISplineParamData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData.md)

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
[ISketch::GetSplineParamsCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineParamsCount.md)  
[ISketch::GetSplines Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplines.md)  
[ISketch::IGetSplines Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSplines.md)  
[ISketch::GetSplinesInterpolate Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplinesInterpolate.md)  
[ISketch::GetSplineInterpolateCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineInterpolateCount.md)  
[ISketch::GetSplineCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineCount.md)  
[ISketch::IGetSplinesInterpolate Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSplinesInterpolate.md)
