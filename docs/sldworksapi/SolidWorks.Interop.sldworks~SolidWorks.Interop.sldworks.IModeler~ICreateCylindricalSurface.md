# ICreateCylindricalSurface Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateCylindricalSurface`

Obsolete. Superseded by IModeler::ICreateCylindricalSurface2.
Obsolete. Superseded by [IModeler::ICreateCylindricalSurface2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateCylindricalSurface2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateCylindricalSurface( _
   ByRef Center As System.Double, _
   ByRef Direction As System.Double, _
   ByVal Radius As System.Double _
) As Surface
```

```

Dim instance As IModeler
Dim Center As System.Double
Dim Direction As System.Double
Dim Radius As System.Double
Dim value As Surface
 
value = instance.ICreateCylindricalSurface(Center, Direction, Radius)
```

```

Surface ICreateCylindricalSurface( 
   ref System.double Center,
   ref System.double Direction,
   System.double Radius
)
```

```

Surface^ ICreateCylindricalSurface( 
   System.double% Center,
   System.double% Direction,
   System.double Radius
) 
```

#### Parameters

*Center*

*Direction*

*Radius*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)
