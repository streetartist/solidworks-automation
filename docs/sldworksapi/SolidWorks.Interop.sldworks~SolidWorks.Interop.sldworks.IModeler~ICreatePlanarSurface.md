# ICreatePlanarSurface Method (IModeler)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreatePlanarSurface`

Obsolete. Superseded by IModeler::ICreatePlanarSurface2.
Obsolete. Superseded by [IModeler::ICreatePlanarSurface2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreatePlanarSurface2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreatePlanarSurface( _
   ByRef RootPoint As System.Double, _
   ByRef Normal As System.Double _
) As Surface
```

```

Dim instance As IModeler
Dim RootPoint As System.Double
Dim Normal As System.Double
Dim value As Surface
 
value = instance.ICreatePlanarSurface(RootPoint, Normal)
```

```

Surface ICreatePlanarSurface( 
   ref System.double RootPoint,
   ref System.double Normal
)
```

```

Surface^ ICreatePlanarSurface( 
   System.double% RootPoint,
   System.double% Normal
) 
```

#### Parameters

*RootPoint*

*Normal*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)
