# FindAttribute Method (IComponent)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent~FindAttribute`

Obsolete. Superseded by IComponent2::FindAttribute.
Obsolete. Superseded by [IComponent2::FindAttribute](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~FindAttribute.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function FindAttribute( _
   ByVal AttributeDef As System.Object, _
   ByVal WhichOne As System.Integer _
) As System.Object
```

```

Dim instance As IComponent
Dim AttributeDef As System.Object
Dim WhichOne As System.Integer
Dim value As System.Object
 
value = instance.FindAttribute(AttributeDef, WhichOne)
```

```

System.object FindAttribute( 
   System.object AttributeDef,
   System.int WhichOne
)
```

```

System.Object^ FindAttribute( 
   System.Object^ AttributeDef,
   System.int WhichOne
) 
```

#### Parameters

*AttributeDef*

*WhichOne*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent.md)  
[IComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent_members.md)
