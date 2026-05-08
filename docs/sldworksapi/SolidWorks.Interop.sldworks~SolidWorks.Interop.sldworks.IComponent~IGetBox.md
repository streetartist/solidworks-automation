# IGetBox Method (IComponent)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent~IGetBox`

Obsolete. Superseded by IComponent2::IGetBox.
Obsolete. Superseded by [IComponent2::IGetBox](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetBox.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetBox( _
   ByVal IncludeRefPlanes As System.Boolean, _
   ByVal IncludeSketches As System.Boolean _
) As System.Double
```

```

Dim instance As IComponent
Dim IncludeRefPlanes As System.Boolean
Dim IncludeSketches As System.Boolean
Dim value As System.Double
 
value = instance.IGetBox(IncludeRefPlanes, IncludeSketches)
```

```

System.double IGetBox( 
   System.bool IncludeRefPlanes,
   System.bool IncludeSketches
)
```

```

System.double IGetBox( 
   System.bool IncludeRefPlanes,
   System.bool IncludeSketches
) 
```

#### Parameters

*IncludeRefPlanes*

*IncludeSketches*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent.md)  
[IComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent_members.md)
