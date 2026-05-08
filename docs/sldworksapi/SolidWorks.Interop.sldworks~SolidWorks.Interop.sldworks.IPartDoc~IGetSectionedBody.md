# IGetSectionedBody Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetSectionedBody`

Obsolete. Superseded by IPartDoc::IGetSectionedBody2.
Obsolete. Superseded by [IPartDoc::IGetSectionedBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetSectionedBody2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetSectionedBody( _
   ByVal ViewIn As ModelView _
) As Body
```

```

Dim instance As IPartDoc
Dim ViewIn As ModelView
Dim value As Body
 
value = instance.IGetSectionedBody(ViewIn)
```

```

Body IGetSectionedBody( 
   ModelView ViewIn
)
```

```

Body^ IGetSectionedBody( 
   ModelView^ ViewIn
) 
```

#### Parameters

*ViewIn*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)
