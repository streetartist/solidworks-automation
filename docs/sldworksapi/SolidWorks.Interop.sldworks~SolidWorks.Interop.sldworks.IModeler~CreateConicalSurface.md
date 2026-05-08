# CreateConicalSurface Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateConicalSurface`

Obsolete. Superseded by IModeler::CreateConicalSurface2.
Obsolete. Superseded by [IModeler::CreateConicalSurface2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateConicalSurface2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateConicalSurface( _
   ByVal Center As System.Object, _
   ByVal Direction As System.Object, _
   ByVal Radius As System.Double, _
   ByVal SemiAngle As System.Double _
) As System.Object
```

```

Dim instance As IModeler
Dim Center As System.Object
Dim Direction As System.Object
Dim Radius As System.Double
Dim SemiAngle As System.Double
Dim value As System.Object
 
value = instance.CreateConicalSurface(Center, Direction, Radius, SemiAngle)
```

```

System.object CreateConicalSurface( 
   System.object Center,
   System.object Direction,
   System.double Radius,
   System.double SemiAngle
)
```

```

System.Object^ CreateConicalSurface( 
   System.Object^ Center,
   System.Object^ Direction,
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
