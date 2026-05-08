# GetRelatedBodies Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetRelatedBodies`

Creates a list of all the related bodies in a part.
Creates a list of all the related bodies in a part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetRelatedBodies() As System.Object
```

```

Dim instance As IPartDoc
Dim value As System.Object
 
value = instance.GetRelatedBodies()
```

```

System.object GetRelatedBodies()
```

```

System.Object^ GetRelatedBodies(); 
```

#### Return Value

Array of related bodies

Remarks

The list contains only those bodies associated with reference surfaces. What results is a list of bodies, which is related to the model, but it does not include the part body itself.

A reference surface feature can consist of one or more surfaces knitted together. Each reference surface feature has two [IBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) objects:

- One for the front faces
- One for the back faces

Each IBody2 object has one or more faces depending on whether the reference surface feature is a set of knitted surfaces or a single underlying surface. The corresponding faces for each body pair should have normal vectors that are opposite.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)  
[IPartDoc::EnumBodies3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~EnumBodies3.md)  
[IPartDoc::EnumRelatedSectionedBodies2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~EnumRelatedSectionedBodies2.md)  
[IPartDoc::EnumRelatedBodies2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~EnumRelatedBodies2.md)  
[IPartDoc::GetRelatedSectionedBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetRelatedSectionedBodies.md)
