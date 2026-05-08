# GetSplineInterpolateCount Method (ISketchBlockDefinition)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetSplineInterpolateCount`

Gets the number of splines in the sketch block definition and the size of array required to hold the data for the interpolation of these splines.
Gets the number of splines in the sketch block definition and the size of array required to hold the data for the interpolation of these splines.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSplineInterpolateCount( _
   ByRef ArraySize As System.Integer _
) As System.Integer
```

```

Dim instance As ISketchBlockDefinition
Dim ArraySize As System.Integer
Dim value As System.Integer
 
value = instance.GetSplineInterpolateCount(ArraySize)
```

```

System.int GetSplineInterpolateCount( 
   out System.int ArraySize
)
```

```

System.int GetSplineInterpolateCount( 
   [Out] System.int ArraySize
) 
```

#### Parameters

*ArraySize*
:   Size of the array needed to hold the spline interpolation data information

#### Return Value

Number of splines in this sketch block definition

Remarks

The ArraySize value is intended to be used as the input ArraySize argument to [ISketchBlockDefinition::IGetSplinesInterpolate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~IGetSplinesInterpolate.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.md)  
[ISketchBlockDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition_members.md)  
[ISketchBlockDefinition::GetSplineCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetSplineCount.md)  
[ISketchBlockDefinition::GetSplineParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetSplineParams.md)  
[ISketchBlockDefinition::GetSplineParamsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetSplineParamsCount.md)  
[ISketchBlockDefinition::GetSplines2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetSplines2.md)  
[ISketchBlockDefinition::GetSplinesInterpolate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetSplinesInterpolate.md)  
[ISketchBlockDefinition::IGetSplineParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~IGetSplineParams.md)  
[ISketchBlockDefinition::IGetSplines2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~IGetSplines2.md)
