# CreateRevolutionSurface Method (IBody)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~CreateRevolutionSurface`

Obsolete. Superseded by IBody2::CreateRevolutionSurface.
Obsolete. Superseded by [IBody2::CreateRevolutionSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateRevolutionSurface.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateRevolutionSurface( _
   ByVal ProfileCurve As System.Object, _
   ByVal AxisPoint As System.Object, _
   ByVal AxisDirection As System.Object, _
   ByVal ProfileEndPtParams As System.Object _
) As System.Object
```

```

Dim instance As IBody
Dim ProfileCurve As System.Object
Dim AxisPoint As System.Object
Dim AxisDirection As System.Object
Dim ProfileEndPtParams As System.Object
Dim value As System.Object
 
value = instance.CreateRevolutionSurface(ProfileCurve, AxisPoint, AxisDirection, ProfileEndPtParams)
```

```

System.object CreateRevolutionSurface( 
   System.object ProfileCurve,
   System.object AxisPoint,
   System.object AxisDirection,
   System.object ProfileEndPtParams
)
```

```

System.Object^ CreateRevolutionSurface( 
   System.Object^ ProfileCurve,
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
