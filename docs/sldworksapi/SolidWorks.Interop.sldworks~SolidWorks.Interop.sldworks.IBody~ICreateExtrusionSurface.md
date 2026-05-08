# ICreateExtrusionSurface Method (IBody)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~ICreateExtrusionSurface`

Obsolete. Superseded by IBody2::ICreateExtrusionSurface.
Obsolete. Superseded by [IBody2::ICreateExtrusionSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateExtrusionSurface.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateExtrusionSurface( _
   ByVal ProfileCurve As Curve, _
   ByVal AxisDirection As System.Object _
) As Surface
```

```

Dim instance As IBody
Dim ProfileCurve As Curve
Dim AxisDirection As System.Object
Dim value As Surface
 
value = instance.ICreateExtrusionSurface(ProfileCurve, AxisDirection)
```

```

Surface ICreateExtrusionSurface( 
   Curve ProfileCurve,
   System.object AxisDirection
)
```

```

Surface^ ICreateExtrusionSurface( 
   Curve^ ProfileCurve,
   System.Object^ AxisDirection
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
