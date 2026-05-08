# CreatePlanarSurface Method (IModeler)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreatePlanarSurface`

Obsolete. Superseded by IModeler::CreatePlanarSurface2.
Obsolete. Superseded by [IModeler::CreatePlanarSurface2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreatePlanarSurface2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreatePlanarSurface( _
   ByVal VRootPoint As System.Object, _
   ByVal VNormal As System.Object _
) As System.Object
```

```

Dim instance As IModeler
Dim VRootPoint As System.Object
Dim VNormal As System.Object
Dim value As System.Object
 
value = instance.CreatePlanarSurface(VRootPoint, VNormal)
```

```

System.object CreatePlanarSurface( 
   System.object VRootPoint,
   System.object VNormal
)
```

```

System.Object^ CreatePlanarSurface( 
   System.Object^ VRootPoint,
   System.Object^ VNormal
) 
```

#### Parameters

*VRootPoint*

*VNormal*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)
