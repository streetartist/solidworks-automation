# AddMenuPopupItem Method (ISldWorks)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenuPopupItem`

Obsolete. Superseded by ISldWorks::AddMenuPopupItem2.
Obsolete. Superseded by [ISldWorks::AddMenuPopupItem2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenuPopupItem2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddMenuPopupItem( _
   ByVal DocType As System.Integer, _
   ByVal SelType As System.Integer, _
   ByVal Item As System.String, _
   ByVal CallbackFcnAndModule As System.String, _
   ByVal CustomNames As System.String _
) As System.Integer
```

```

Dim instance As ISldWorks
Dim DocType As System.Integer
Dim SelType As System.Integer
Dim Item As System.String
Dim CallbackFcnAndModule As System.String
Dim CustomNames As System.String
Dim value As System.Integer
 
value = instance.AddMenuPopupItem(DocType, SelType, Item, CallbackFcnAndModule, CustomNames)
```

```

System.int AddMenuPopupItem( 
   System.int DocType,
   System.int SelType,
   System.string Item,
   System.string CallbackFcnAndModule,
   System.string CustomNames
)
```

```

System.int AddMenuPopupItem( 
   System.int DocType,
   System.int SelType,
   System.String^ Item,
   System.String^ CallbackFcnAndModule,
   System.String^ CustomNames
) 
```

#### Parameters

*DocType*

*SelType*

*Item*

*CallbackFcnAndModule*

*CustomNames*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
