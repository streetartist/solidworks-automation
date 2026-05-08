# ICreatePlanarSurface Method (IBody)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~ICreatePlanarSurface`

Obsolete. Superseded by IBody2::ICreatePlanarSurface.
Obsolete. Superseded by [IBody2::ICreatePlanarSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreatePlanarSurface.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreatePlanarSurface( _
   ByVal VRootPoint As System.Object, _
   ByVal VNormal As System.Object _
) As Surface
```

```

Dim instance As IBody
Dim VRootPoint As System.Object
Dim VNormal As System.Object
Dim value As Surface
 
value = instance.ICreatePlanarSurface(VRootPoint, VNormal)
```

```

Surface ICreatePlanarSurface( 
   System.object VRootPoint,
   System.object VNormal
)
```

```

Surface^ ICreatePlanarSurface( 
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

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.md)  
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.md)
