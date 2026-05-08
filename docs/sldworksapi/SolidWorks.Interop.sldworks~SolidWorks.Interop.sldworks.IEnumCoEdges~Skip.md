# Skip Method (IEnumCoEdges)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumCoEdges~Skip`

Skips the specified number of coedges in the coedges enumeration.
Skips the specified number of coedges in the coedges enumeration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Skip( _
   ByVal Celt As System.Integer _
) 
```

```

Dim instance As IEnumCoEdges
Dim Celt As System.Integer
 
instance.Skip(Celt)
```

```

void Skip( 
   System.int Celt
)
```

```

void Skip( 
   System.int Celt
) 
```

#### Parameters

*Celt*
:   Number of coedges to skip

Remarks

For use in in-process DLLs only.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEnumCoEdges Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumCoEdges.md)  
[IEnumCoEdges Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumCoEdges_members.md)
