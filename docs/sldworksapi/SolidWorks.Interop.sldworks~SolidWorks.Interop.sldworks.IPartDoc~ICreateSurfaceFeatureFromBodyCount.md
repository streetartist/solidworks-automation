# ICreateSurfaceFeatureFromBodyCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ICreateSurfaceFeatureFromBodyCount`

Obsolete. Superseded by IPartDoc::ICreateSurfaceFeatureFromBodyCount2.
Obsolete. Superseded by [IPartDoc::ICreateSurfaceFeatureFromBodyCount2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ICreateSurfaceFeatureFromBodyCount2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateSurfaceFeatureFromBodyCount( _
   ByVal Body As Body, _
   ByVal Options As System.Integer _
) As System.Integer
```

```

Dim instance As IPartDoc
Dim Body As Body
Dim Options As System.Integer
Dim value As System.Integer
 
value = instance.ICreateSurfaceFeatureFromBodyCount(Body, Options)
```

```

System.int ICreateSurfaceFeatureFromBodyCount( 
   Body Body,
   System.int Options
)
```

```

System.int ICreateSurfaceFeatureFromBodyCount( 
   Body^ Body,
   System.int Options
) 
```

#### Parameters

*Body*

*Options*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)
