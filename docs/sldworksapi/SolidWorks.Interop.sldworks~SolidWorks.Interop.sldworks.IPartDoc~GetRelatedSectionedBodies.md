# GetRelatedSectionedBodies Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetRelatedSectionedBodies`

Gets all of the related sectioned bodies in a part.
Gets all of the related sectioned bodies in a part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetRelatedSectionedBodies( _
   ByVal ViewIn As System.Object _
) As System.Object
```

```

Dim instance As IPartDoc
Dim ViewIn As System.Object
Dim value As System.Object
 
value = instance.GetRelatedSectionedBodies(ViewIn)
```

```

System.object GetRelatedSectionedBodies( 
   System.object ViewIn
)
```

```

System.Object^ GetRelatedSectionedBodies( 
   System.Object^ ViewIn
) 
```

#### Parameters

*ViewIn*
:   [Model view](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.md)

#### Return Value

Array of related sectioned bodies.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)  
[IPartDoc::EnumBodies3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~EnumBodies3.md)  
[IPartDoc::EnumRelatedBodies2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~EnumRelatedBodies2.md)  
[IPartDoc::EnumRelatedSectionedBodies2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~EnumRelatedSectionedBodies2.md)  
[IPartDoc::GetRelatedBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetRelatedBodies.md)
