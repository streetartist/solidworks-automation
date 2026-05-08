# CreateExtrusionSurface Method (IBody)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~CreateExtrusionSurface`

Obsolete. Superseded by IBody2::CreateExtrusionSurface.
Obsolete. Superseded by [IBody2::CreateExtrusionSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateExtrusionSurface.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateExtrusionSurface( _
   ByVal ProfileCurve As System.Object, _
   ByVal AxisDirection As System.Object _
) As System.Object
```

```

Dim instance As IBody
Dim ProfileCurve As System.Object
Dim AxisDirection As System.Object
Dim value As System.Object
 
value = instance.CreateExtrusionSurface(ProfileCurve, AxisDirection)
```

```

System.object CreateExtrusionSurface( 
   System.object ProfileCurve,
   System.object AxisDirection
)
```

```

System.Object^ CreateExtrusionSurface( 
   System.Object^ ProfileCurve,
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
