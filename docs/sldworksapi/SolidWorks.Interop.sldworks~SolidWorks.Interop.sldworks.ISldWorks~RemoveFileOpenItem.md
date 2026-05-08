# RemoveFileOpenItem Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveFileOpenItem`

Obsolete. Superseded by ISldWorks::RemoveFileOpenItem2.
Obsolete. Superseded by [ISldWorks::RemoveFileOpenItem2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveFileOpenItem2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function RemoveFileOpenItem( _
   ByVal CallbackFcnAndModule As System.String, _
   ByVal Description As System.String _
) As System.Boolean
```

```

Dim instance As ISldWorks
Dim CallbackFcnAndModule As System.String
Dim Description As System.String
Dim value As System.Boolean
 
value = instance.RemoveFileOpenItem(CallbackFcnAndModule, Description)
```

```

System.bool RemoveFileOpenItem( 
   System.string CallbackFcnAndModule,
   System.string Description
)
```

```

System.bool RemoveFileOpenItem( 
   System.String^ CallbackFcnAndModule,
   System.String^ Description
) 
```

#### Parameters

*CallbackFcnAndModule*

*Description*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
