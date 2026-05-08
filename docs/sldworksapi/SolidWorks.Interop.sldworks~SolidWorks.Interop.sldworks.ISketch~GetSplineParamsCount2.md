# GetSplineParamsCount2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineParamsCount2`

Obsolete. Superseded by ISketch::GetSplineParamsCount3.
Obsolete. Superseded by [ISketch::GetSplineParamsCount3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineParamsCount3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSplineParamsCount2( _
   ByRef Size As System.Integer _
) As System.Integer
```

```

Dim instance As ISketch
Dim Size As System.Integer
Dim value As System.Integer
 
value = instance.GetSplineParamsCount2(Size)
```

```

System.int GetSplineParamsCount2( 
   out System.int Size
)
```

```

System.int GetSplineParamsCount2( 
   [Out] System.int Size
) 
```

#### Parameters

*Size*
:   Size of array required for a call to [ISketch::IGetSplineParams2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSplineParams2.md)

#### Return Value

Number of [splines](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineParams3.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)  
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.md)  
[ISketch::GetSplineCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineCount.md)  
[ISketch::GetSplineInterpolateCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineInterpolateCount.md)  
[ISketch::GetSplines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplines.md)  
[ISketch::GetSplinesInterpolate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplinesInterpolate.md)  
[ISketch::IGetSplines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSplines.md)  
[ISketch::IGetSplinesInterpolate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSplinesInterpolate.md)  
[ISketch::GetSplineParams2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineParams2.md)
