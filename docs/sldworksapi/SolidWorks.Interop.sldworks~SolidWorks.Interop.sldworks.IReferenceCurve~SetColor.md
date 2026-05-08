# SetColor Method (IReferenceCurve)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve~SetColor`

Sets the color of the reference curve feature.
Sets the color of the reference curve feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetColor( _
   ByVal ColorIn As System.Integer _
) As System.Boolean
```

```

Dim instance As IReferenceCurve
Dim ColorIn As System.Integer
Dim value As System.Boolean
 
value = instance.SetColor(ColorIn)
```

```

System.bool SetColor( 
   System.int ColorIn
)
```

```

System.bool SetColor( 
   System.int ColorIn
) 
```

#### Parameters

*ColorIn*
:   COLORREF value of the color

#### Return Value

True if the color was set, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IReferenceCurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve.md)  
[IReferenceCurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve_members.md)
