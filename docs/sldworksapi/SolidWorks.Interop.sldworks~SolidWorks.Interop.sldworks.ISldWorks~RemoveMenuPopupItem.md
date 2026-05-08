# RemoveMenuPopupItem Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveMenuPopupItem`

Obsolete. Superseded by ISldWorks::RemoveMenuPopupItem2.
Obsolete. Superseded by [ISldWorks::RemoveMenuPopupItem2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveMenuPopupItem2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function RemoveMenuPopupItem( _
   ByVal DocType As System.Integer, _
   ByVal SelectType As System.Integer, _
   ByVal Item As System.String, _
   ByVal CallbackFcnAndModule As System.String, _
   ByVal CustomNames As System.String, _
   ByVal Unused As System.Integer _
) As System.Boolean
```

```

Dim instance As ISldWorks
Dim DocType As System.Integer
Dim SelectType As System.Integer
Dim Item As System.String
Dim CallbackFcnAndModule As System.String
Dim CustomNames As System.String
Dim Unused As System.Integer
Dim value As System.Boolean
 
value = instance.RemoveMenuPopupItem(DocType, SelectType, Item, CallbackFcnAndModule, CustomNames, Unused)
```

```

System.bool RemoveMenuPopupItem( 
   System.int DocType,
   System.int SelectType,
   System.string Item,
   System.string CallbackFcnAndModule,
   System.string CustomNames,
   System.int Unused
)
```

```

System.bool RemoveMenuPopupItem( 
   System.int DocType,
   System.int SelectType,
   System.String^ Item,
   System.String^ CallbackFcnAndModule,
   System.String^ CustomNames,
   System.int Unused
) 
```

#### Parameters

*DocType*

*SelectType*

*Item*

*CallbackFcnAndModule*

*CustomNames*

*Unused*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
