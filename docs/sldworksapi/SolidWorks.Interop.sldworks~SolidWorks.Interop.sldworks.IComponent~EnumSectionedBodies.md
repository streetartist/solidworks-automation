# EnumSectionedBodies Method (IComponent)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent~EnumSectionedBodies`

Obsolete. Superseded by IComponent2::EnumSectionedBodies.
Obsolete. Superseded by [IComponent2::EnumSectionedBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~EnumSectionedBodies.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function EnumSectionedBodies( _
   ByVal ViewIn As ModelView _
) As EnumBodies
```

```

Dim instance As IComponent
Dim ViewIn As ModelView
Dim value As EnumBodies
 
value = instance.EnumSectionedBodies(ViewIn)
```

```

EnumBodies EnumSectionedBodies( 
   ModelView ViewIn
)
```

```

EnumBodies^ EnumSectionedBodies( 
   ModelView^ ViewIn
) 
```

#### Parameters

*ViewIn*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent.md)  
[IComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent_members.md)
