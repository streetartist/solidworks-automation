# ICreateExtrusionSurfaceDLL Method (IBody)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~ICreateExtrusionSurfaceDLL`

Obsolete. Superseded by IBody2::ICreateExtrusionSurfaceDLL.
Obsolete. Superseded by [IBody2::ICreateExtrusionSurfaceDLL](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateExtrusionSurfaceDLL.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateExtrusionSurfaceDLL( _
   ByVal ProfileCurve As Curve, _
   ByRef AxisDirection As System.Double _
) As Surface
```

```

Dim instance As IBody
Dim ProfileCurve As Curve
Dim AxisDirection As System.Double
Dim value As Surface
 
value = instance.ICreateExtrusionSurfaceDLL(ProfileCurve, AxisDirection)
```

```

Surface ICreateExtrusionSurfaceDLL( 
   Curve ProfileCurve,
   ref System.double AxisDirection
)
```

```

Surface^ ICreateExtrusionSurfaceDLL( 
   Curve^ ProfileCurve,
   System.double% AxisDirection
) 
```

#### Parameters

*ProfileCurve*

*AxisDirection*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.md)  
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.md)
