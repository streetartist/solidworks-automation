# SetControlVertexWeights Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~SetControlVertexWeights`

Sets the weights of the control vetexes of this rational spline.
Sets the weights of the control vetexes of this rational spline.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetControlVertexWeights( _
   ByVal ControlWeightValues As System.Object _
) As System.Boolean
```

```

Dim instance As ISketchSpline
Dim ControlWeightValues As System.Object
Dim value As System.Boolean
 
value = instance.SetControlVertexWeights(ControlWeightValues)
```

```

System.bool SetControlVertexWeights( 
   System.object ControlWeightValues
)
```

```

System.bool SetControlVertexWeights( 
   System.Object^ ControlWeightValues
) 
```

#### Parameters

*ControlWeightValues*
:   Array of control vertex weights

#### Return Value

True if weights successfully set, false if not

Remarks

This method:

- is valid only if [ISketchSpline::IsRationalCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~IsRationalCurve.md) is true.
- returns false if the number of weights in ControlWeightValues is not equal to the number of control vertexes of the spline.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchSpline Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.md)  
[ISketchSpline Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline_members.md)  
[ISketchSpline::GetControlVertexWeights Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~GetControlVertexWeights.md)
