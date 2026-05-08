# IGetSheetBody Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetSheetBody`

Gets a sheet (surface) body in this body.
Gets a sheet (surface) body in this body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetSheetBody( _
   ByVal Index As System.Integer _
) As Body2
```

```

Dim instance As IBody2
Dim Index As System.Integer
Dim value As Body2
 
value = instance.IGetSheetBody(Index)
```

```

Body2 IGetSheetBody( 
   System.int Index
)
```

```

Body2^ IGetSheetBody( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Index of sheet body

#### Return Value

Pointer to the sheet [body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) corresponding to the index

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::GetSheetBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetSheetBody.md)
