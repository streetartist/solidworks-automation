# EnumBodies2 Method (IComponent2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~EnumBodies2`

Obsolete. Superseded by IComponent2::EnumBodies3.
Obsolete. Superseded by [IComponent2::EnumBodies3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~EnumBodies3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function EnumBodies2( _
   ByVal BodyType As System.Integer _
) As EnumBodies2
```

```

Dim instance As IComponent2
Dim BodyType As System.Integer
Dim value As EnumBodies2
 
value = instance.EnumBodies2(BodyType)
```

```

EnumBodies2 EnumBodies2( 
   System.int BodyType
)
```

```

EnumBodies2^ EnumBodies2( 
   System.int BodyType
) 
```

#### Parameters

*BodyType*
:   Type of body as defined by [swBodyType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBodyType_e.html)

#### Return Value

[Enumerated list of bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumBodies2.md)

Remarks

This method only supports solid and sheet (surface) body types.

The difference between this method and the now obsolete IComponent2::EnumBodies is that the new method supports lightweight components. The now obsolete IComponent2::EnumBodies does not.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IComponent2::GetBodies3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetBodies3.md)  
[IComponent2::GetBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetBody.md)  
[IComponent2::IGetBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetBody.md)
