# GetFinCoFin Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetFinCoFin`

Gets the ID of the CoFin that is shared by a fin.
Gets the ID of the CoFin that is shared by a fin.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFinCoFin( _
   ByVal FinId As System.Integer _
) As System.Integer
```

```

Dim instance As ITessellation
Dim FinId As System.Integer
Dim value As System.Integer
 
value = instance.GetFinCoFin(FinId)
```

```

System.int GetFinCoFin( 
   System.int FinId
)
```

```

System.int GetFinCoFin( 
   System.int FinId
) 
```

#### Parameters

*FinId*
:   Fin ID that to use to return the cofin ID

#### Return Value

Long or integer value that describes the ID number of the cofin

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.md)  
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.md)
