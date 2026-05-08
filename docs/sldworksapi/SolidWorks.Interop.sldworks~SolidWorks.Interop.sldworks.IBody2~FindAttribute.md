# FindAttribute Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~FindAttribute`

Finds an attribute on a body.
Finds an attribute on a body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function FindAttribute( _
   ByVal AttributeDef As AttributeDef, _
   ByVal WhichOne As System.Integer _
) As Attribute
```

```

Dim instance As IBody2
Dim AttributeDef As AttributeDef
Dim WhichOne As System.Integer
Dim value As Attribute
 
value = instance.FindAttribute(AttributeDef, WhichOne)
```

```

Attribute FindAttribute( 
   AttributeDef AttributeDef,
   System.int WhichOne
)
```

```

Attribute^ FindAttribute( 
   AttributeDef^ AttributeDef,
   System.int WhichOne
) 
```

#### Parameters

*AttributeDef*
:   Pointer to the [attribute definition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef.md) that you want to find

*WhichOne*
:   Instance number of this type on the body (0, 1, 2, 3, and so on)

#### Return Value

Pointer to the [attribute](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute.md) instance

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)
