# EnumBodies Method (IComponent2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~EnumBodies`

Obsolete. Superseded by IComponent2::EnumBodies2.
Obsolete. Superseded by [IComponent2::EnumBodies2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~EnumBodies2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function EnumBodies( _
   ByVal BodyType As System.Integer _
) As EnumBodies2
```

```

Dim instance As IComponent2
Dim BodyType As System.Integer
Dim value As EnumBodies2
 
value = instance.EnumBodies(BodyType)
```

```

EnumBodies2 EnumBodies( 
   System.int BodyType
)
```

```

EnumBodies2^ EnumBodies( 
   System.int BodyType
) 
```

#### Parameters

*BodyType*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)
