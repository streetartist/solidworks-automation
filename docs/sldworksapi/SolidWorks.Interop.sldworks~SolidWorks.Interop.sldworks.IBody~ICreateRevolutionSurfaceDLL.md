# ICreateRevolutionSurfaceDLL Method (IBody)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~ICreateRevolutionSurfaceDLL`

Obsolete. Superseded by IBody2::ICreateRevolutionSurfaceDLL.
Obsolete. Superseded by [IBody2::ICreateRevolutionSurfaceDLL](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateRevolutionSurfaceDLL.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateRevolutionSurfaceDLL( _
   ByVal ProfileCurve As Curve, _
   ByRef AxisPoint As System.Double, _
   ByRef AxisDirection As System.Double, _
   ByRef ProfileEndPtParams As System.Double _
) As Surface
```

```

Dim instance As IBody
Dim ProfileCurve As Curve
Dim AxisPoint As System.Double
Dim AxisDirection As System.Double
Dim ProfileEndPtParams As System.Double
Dim value As Surface
 
value = instance.ICreateRevolutionSurfaceDLL(ProfileCurve, AxisPoint, AxisDirection, ProfileEndPtParams)
```

```

Surface ICreateRevolutionSurfaceDLL( 
   Curve ProfileCurve,
   ref System.double AxisPoint,
   ref System.double AxisDirection,
   ref System.double ProfileEndPtParams
)
```

```

Surface^ ICreateRevolutionSurfaceDLL( 
   Curve^ ProfileCurve,
   System.double% AxisPoint,
   System.double% AxisDirection,
   System.double% ProfileEndPtParams
) 
```

#### Parameters

*ProfileCurve*

*AxisPoint*

*AxisDirection*

*ProfileEndPtParams*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.md)  
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.md)
