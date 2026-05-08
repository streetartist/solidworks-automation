# EnumRelatedSectionedBodies2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~EnumRelatedSectionedBodies2`

Gets an enumeration of the related sectioned bodies in a part.
Gets an enumeration of the related sectioned bodies in a part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function EnumRelatedSectionedBodies2( _
   ByVal ViewIn As ModelView _
) As EnumBodies2
```

```

Dim instance As IPartDoc
Dim ViewIn As ModelView
Dim value As EnumBodies2
 
value = instance.EnumRelatedSectionedBodies2(ViewIn)
```

```

EnumBodies2 EnumRelatedSectionedBodies2( 
   ModelView ViewIn
)
```

```

EnumBodies2^ EnumRelatedSectionedBodies2( 
   ModelView^ ViewIn
) 
```

#### Parameters

*ViewIn*
:   [Model view](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.md)

#### Return Value

[Enumeration of the related sectioned bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumBodies2.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)  
[IPartDoc::EnumRelatedBodies2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~EnumRelatedBodies2.md)  
[IPartDoc::EnumBodies3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~EnumBodies3.md)  
[IPartDoc::GetRelatedBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetRelatedBodies.md)  
[IPartDoc::GetRelatedSectionedBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetRelatedSectionedBodies.md)  
[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)
