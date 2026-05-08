# EnumRelatedSectionedBodies Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~EnumRelatedSectionedBodies`

Obsolete. Superseded by IPartDoc::EnumRelatedSectionedBodies.
Obsolete. Superseded by [IPartDoc::EnumRelatedSectionedBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~EnumRelatedSectionedBodies2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function EnumRelatedSectionedBodies( _
   ByVal ViewIn As ModelView _
) As EnumBodies
```

```

Dim instance As IPartDoc
Dim ViewIn As ModelView
Dim value As EnumBodies
 
value = instance.EnumRelatedSectionedBodies(ViewIn)
```

```

EnumBodies EnumRelatedSectionedBodies( 
   ModelView ViewIn
)
```

```

EnumBodies^ EnumRelatedSectionedBodies( 
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
