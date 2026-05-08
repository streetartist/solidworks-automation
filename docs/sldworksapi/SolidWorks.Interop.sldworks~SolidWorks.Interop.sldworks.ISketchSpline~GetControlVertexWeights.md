# GetControlVertexWeights Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~GetControlVertexWeights`

Gets the weights of the control vetexes of this rational spline.
Gets the weights of the control vetexes of this rational spline.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetControlVertexWeights() As System.Object
```

```

Dim instance As ISketchSpline
Dim value As System.Object
 
value = instance.GetControlVertexWeights()
```

```

System.object GetControlVertexWeights()
```

```

System.Object^ GetControlVertexWeights(); 
```

#### Return Value

Array of control vertex weights

Remarks

This method:

- is valid only if [ISketchSpline::IsRationalCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~IsRationalCurve.md) is true.
- returns an empty array if the spline is non-rational.

Example

[Edit Spline (VBA)](Edit_Spline_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchSpline Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.md)  
[ISketchSpline Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline_members.md)  
[ISketchSpline::SetControlVertexWeights Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~SetControlVertexWeights.md)
