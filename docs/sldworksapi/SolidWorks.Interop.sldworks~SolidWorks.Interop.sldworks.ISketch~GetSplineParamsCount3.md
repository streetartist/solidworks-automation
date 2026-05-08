# GetSplineParamsCount3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineParamsCount3`

Gets the number of splines in the sketch and the size of array required to hold the data for them.
Gets the number of splines in the sketch and the size of array required to hold the data for them.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSplineParamsCount3( _
   ByVal ForceNonPeriodic As System.Boolean, _
   ByRef Size As System.Integer _
) As System.Integer
```

```

Dim instance As ISketch
Dim ForceNonPeriodic As System.Boolean
Dim Size As System.Integer
Dim value As System.Integer
 
value = instance.GetSplineParamsCount3(ForceNonPeriodic, Size)
```

```

System.int GetSplineParamsCount3( 
   System.bool ForceNonPeriodic,
   out System.int Size
)
```

```

System.int GetSplineParamsCount3( 
   System.bool ForceNonPeriodic,
   [Out] System.int Size
) 
```

#### Parameters

*ForceNonPeriodic*
:   True to attempt to convert all non-periodic splines to periodic, false to not

*Size*
:   Size of array required for a call to [ISketch::IGetSplineParams3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSplineParams3.md)

#### Return Value

Number of [splines](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineParams3.md)

Example

[Get Spline's Parameters (C#)](Get_Spline's_Parameters_Example_CSharp.htm)  
[Get Spline's Parameters (VB.NET)](Get_Spline's_Parameters_Example_VBNET.htm)  
[Get Spline's Parameters (VBA)](Get_Spline's_Parameters_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)  
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.md)  
[ISketch::GetSplines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplines.md)  
[ISketch::GetSplinesInterpolate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplinesInterpolate.md)  
[ISketch::IGetSplines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSplines.md)  
[ISketch::IGetSplinesInterpolate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSplinesInterpolate.md)  
[ISketch::GetSplineCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineCount.md)  
[ISketch::GetSplineInterpolateCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineInterpolateCount.md)  
[ISketch::GetSplineParams3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineParams3.md)
