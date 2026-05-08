# ICreateConicalSurface Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateConicalSurface`

Obsolete. Superseded by IModeler::ICreateConicalSurface2.
Obsolete. Superseded by [IModeler::ICreateConicalSurface2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateCylindricalSurface2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateConicalSurface( _
   ByRef Center As System.Double, _
   ByRef Direction As System.Double, _
   ByVal Radius As System.Double, _
   ByVal SemiAngle As System.Double _
) As Surface
```

```

Dim instance As IModeler
Dim Center As System.Double
Dim Direction As System.Double
Dim Radius As System.Double
Dim SemiAngle As System.Double
Dim value As Surface
 
value = instance.ICreateConicalSurface(Center, Direction, Radius, SemiAngle)
```

```

Surface ICreateConicalSurface( 
   ref System.double Center,
   ref System.double Direction,
   System.double Radius,
   System.double SemiAngle
)
```

```

Surface^ ICreateConicalSurface( 
   System.double% Center,
   System.double% Direction,
   System.double Radius,
   System.double SemiAngle
) 
```

#### Parameters

*Center*

*Direction*

*Radius*

*SemiAngle*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)
