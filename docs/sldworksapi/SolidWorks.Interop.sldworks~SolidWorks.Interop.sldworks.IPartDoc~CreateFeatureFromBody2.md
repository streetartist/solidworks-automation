# CreateFeatureFromBody2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~CreateFeatureFromBody2`

Obsolete. Superseded by IPartDoc::CreateFeatureFromBody3.
Obsolete. Superseded by [IPartDoc::CreateFeatureFromBody3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~CreateFeatureFromBody3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateFeatureFromBody2( _
   ByVal Body As System.Object, _
   ByVal MakeRefSurface As System.Boolean _
) As System.Object
```

```

Dim instance As IPartDoc
Dim Body As System.Object
Dim MakeRefSurface As System.Boolean
Dim value As System.Object
 
value = instance.CreateFeatureFromBody2(Body, MakeRefSurface)
```

```

System.object CreateFeatureFromBody2( 
   System.object Body,
   System.bool MakeRefSurface
)
```

```

System.Object^ CreateFeatureFromBody2( 
   System.Object^ Body,
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
