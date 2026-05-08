# Clearance Property (IDragOperator)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~Clearance`

Gets the clearance distance between the components.
Gets the clearance distance between the components.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Clearance( _
   ByVal NIndex As System.Integer _
) As System.Double
```

```

Dim instance As IDragOperator
Dim NIndex As System.Integer
Dim value As System.Double
 
value = instance.Clearance(NIndex)
```

```

System.double Clearance( 
   System.int NIndex
) {get;}
```

```

property System.double Clearance {
   System.double get(System.int NIndex);
}
```

#### Parameters

*NIndex*
:   Index of the components

#### Property Value

Clearance value

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDragOperator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator.md)  
[IDragOperator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator_members.md)
