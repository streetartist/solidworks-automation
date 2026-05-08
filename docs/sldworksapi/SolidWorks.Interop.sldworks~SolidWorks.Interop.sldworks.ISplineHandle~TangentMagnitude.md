# TangentMagnitude Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~TangentMagnitude`

Gets or sets the weight for the tangency magnitude in the specified direction for this spline handle.
Gets or sets the weight for the tangency magnitude in the specified direction for this spline handle.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TangentMagnitude( _
   ByVal WhichDirection As System.Integer _
) As System.Double
```

```

Dim instance As ISplineHandle
Dim WhichDirection As System.Integer
Dim value As System.Double
 
instance.TangentMagnitude(WhichDirection) = value
 
value = instance.TangentMagnitude(WhichDirection)
```

```

System.double TangentMagnitude( 
   System.int WhichDirection
) {get; set;}
```

```

property System.double TangentMagnitude {
   System.double get(System.int WhichDirection);
   void set (System.int WhichDirection, System.double value);
}
```

#### Parameters

*WhichDirection*
:   Direction as defined in [swTangentMagnitudeDirection\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTangentMagnitudeDirection_e.html)

#### Property Value

Weight for the tangency magnitude in the specified direction

Example

See the [ISplineHandle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISplineHandle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle.md)  
[ISplineHandle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle_members.md)  
[ISplineHandle::TangentDriving Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~TangentDriving.md)  
[ISplineHandle::TangentPolarDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~TangentPolarDirection.md)  
[ISplineHandle::TangentRadialDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~TangentRadialDirection.md)
