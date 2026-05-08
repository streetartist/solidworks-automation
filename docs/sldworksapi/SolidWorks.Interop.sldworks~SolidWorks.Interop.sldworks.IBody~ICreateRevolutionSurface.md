# ICreateRevolutionSurface Method (IBody)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~ICreateRevolutionSurface`

Obsolete. Superseded by IBody2::ICreateRevolutionSurface.
Obsolete. Superseded by [IBody2::ICreateRevolutionSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateRevolutionSurface.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateRevolutionSurface( _
   ByVal ProfileCurve As Curve, _
   ByVal AxisPoint As System.Object, _
   ByVal AxisDirection As System.Object, _
   ByVal ProfileEndPtParams As System.Object _
) As Surface
```

```

Dim instance As IBody
Dim ProfileCurve As Curve
Dim AxisPoint As System.Object
Dim AxisDirection As System.Object
Dim ProfileEndPtParams As System.Object
Dim value As Surface
 
value = instance.ICreateRevolutionSurface(ProfileCurve, AxisPoint, AxisDirection, ProfileEndPtParams)
```

```

Surface ICreateRevolutionSurface( 
   Curve ProfileCurve,
   System.object AxisPoint,
   System.object AxisDirection,
   System.object ProfileEndPtParams
)
```

```

Surface^ ICreateRevolutionSurface( 
   Curve^ ProfileCurve,
   System.Object^ AxisPoint,
   System.Object^ AxisDirection,
   System.Object^ ProfileEndPtParams
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
