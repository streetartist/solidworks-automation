# CreateSphericalSurface Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSphericalSurface`

Obsolete. Superseded by IModeler::CreateSphericalSurface2.
Obsolete. Superseded by [IModeler::CreateSphericalSurface2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSphericalSurface2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateSphericalSurface( _
   ByVal Center As System.Object, _
   ByVal Radius As System.Double _
) As System.Object
```

```

Dim instance As IModeler
Dim Center As System.Object
Dim Radius As System.Double
Dim value As System.Object
 
value = instance.CreateSphericalSurface(Center, Radius)
```

```

System.object CreateSphericalSurface( 
   System.object Center,
   System.double Radius
)
```

```

System.Object^ CreateSphericalSurface( 
   System.Object^ Center,
   System.double Radius
) 
```

#### Parameters

*Center*

*Radius*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)
