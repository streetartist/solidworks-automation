# AddFileSaveAsItem Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddFileSaveAsItem`

Obsolete. Superseded by ISldWorks::AddFileSaveAsItem2.
Obsolete. Superseded by [ISldWorks::AddFileSaveAsItem2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddFileSaveAsItem2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddFileSaveAsItem( _
   ByVal CallbackFcnAndModule As System.String, _
   ByVal Description As System.String, _
   ByVal Type As System.Integer _
) As System.Boolean
```

```

Dim instance As ISldWorks
Dim CallbackFcnAndModule As System.String
Dim Description As System.String
Dim Type As System.Integer
Dim value As System.Boolean
 
value = instance.AddFileSaveAsItem(CallbackFcnAndModule, Description, Type)
```

```

System.bool AddFileSaveAsItem( 
   System.string CallbackFcnAndModule,
   System.string Description,
   System.int Type
)
```

```

System.bool AddFileSaveAsItem( 
   System.String^ CallbackFcnAndModule,
   System.String^ Description,
   System.int Type
) 
```

#### Parameters

*CallbackFcnAndModule*

*Description*

*Type*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
