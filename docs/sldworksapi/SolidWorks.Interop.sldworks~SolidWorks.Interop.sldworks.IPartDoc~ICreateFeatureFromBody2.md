# ICreateFeatureFromBody2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ICreateFeatureFromBody2`

Obsolete. Superseded by IPartDoc::ICreateFeatureFromBody4.
Obsolete. Superseded by [IPartDoc::ICreateFeatureFromBody4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ICreateFeatureFromBody4.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateFeatureFromBody2( _
   ByVal Body As Body, _
   ByVal MakeRefSurface As System.Boolean _
) As Feature
```

```

Dim instance As IPartDoc
Dim Body As Body
Dim MakeRefSurface As System.Boolean
Dim value As Feature
 
value = instance.ICreateFeatureFromBody2(Body, MakeRefSurface)
```

```

Feature ICreateFeatureFromBody2( 
   Body Body,
   System.bool MakeRefSurface
)
```

```

Feature^ ICreateFeatureFromBody2( 
   Body^ Body,
   System.bool MakeRefSurface
) 
```

#### Parameters

*Body*

*MakeRefSurface*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)
