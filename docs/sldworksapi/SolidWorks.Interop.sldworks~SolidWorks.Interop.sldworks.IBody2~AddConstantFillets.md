# AddConstantFillets Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~AddConstantFillets`

Creates constant radius fillets on the specified edges on this body.
Creates constant radius fillets on the specified edges on this body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddConstantFillets( _
   ByVal Radius As System.Double, _
   ByVal EdgesToFillet As System.Object _
) As System.Object
```

```

Dim instance As IBody2
Dim Radius As System.Double
Dim EdgesToFillet As System.Object
Dim value As System.Object
 
value = instance.AddConstantFillets(Radius, EdgesToFillet)
```

```

System.object AddConstantFillets( 
   System.double Radius,
   System.object EdgesToFillet
)
```

```

System.Object^ AddConstantFillets( 
   System.double Radius,
   System.Object^ EdgesToFillet
) 
```

#### Parameters

*Radius*
:   Fillet radius

*EdgesToFillet*
:   Array of [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) to fillet

#### Return Value

Array of newly created [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

Remarks

This method does not work for sheet bodies.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)
