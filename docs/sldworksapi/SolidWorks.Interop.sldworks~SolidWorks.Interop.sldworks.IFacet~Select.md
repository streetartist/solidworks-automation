# Select Method (IFacet)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFacet~Select`

Selects the specified facet.
Selects the specified facet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Select( _
   ByVal Append As System.Boolean, _
   ByVal Data As System.Object _
) As System.Boolean
```

```

Dim instance As IFacet
Dim Append As System.Boolean
Dim Data As System.Object
Dim value As System.Boolean
 
value = instance.Select(Append, Data)
```

```

System.bool Select( 
   System.bool Append,
   System.object Data
)
```

```

System.bool Select( 
   System.bool Append,
   System.Object^ Data
) 
```

#### Parameters

*Append*
:   True to append this selection to the selection list, false to replace the selection list with this selection

*Data*
:   Pointer to the [ISelectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData.md) object

#### Return Value

True if the facet is selected, false if not

Example

See the [IFacet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFacet.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFacet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFacet.md)  
[IFacet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFacet_members.md)
