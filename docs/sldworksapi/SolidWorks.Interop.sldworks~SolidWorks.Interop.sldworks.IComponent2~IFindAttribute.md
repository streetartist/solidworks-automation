# IFindAttribute Method (IComponent2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IFindAttribute`

Finds an attribute on a component.
Finds an attribute on a component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IFindAttribute( _
   ByVal AttributeDef As AttributeDef, _
   ByVal WhichOne As System.Integer _
) As Attribute
```

```

Dim instance As IComponent2
Dim AttributeDef As AttributeDef
Dim WhichOne As System.Integer
Dim value As Attribute
 
value = instance.IFindAttribute(AttributeDef, WhichOne)
```

```

Attribute IFindAttribute( 
   AttributeDef AttributeDef,
   System.int WhichOne
)
```

```

Attribute^ IFindAttribute( 
   AttributeDef^ AttributeDef,
   System.int WhichOne
) 
```

#### Parameters

*AttributeDef*
:   Pointer to an [attribute definition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef.md) that you are looking for on this component

*WhichOne*
:   Index number of the attribute that you want to return; there might be several attributes on this component

#### Return Value

Pointer to the [attribute](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IComponent2::FindAttribute Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~FindAttribute.md)
