# EnumBodies3 Method (IPartDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~EnumBodies3`

Enumerates the bodies in this part.
Enumerates the bodies in this part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function EnumBodies3( _
   ByVal BodyType As System.Integer, _
   ByVal BVisibleOnly As System.Boolean _
) As EnumBodies2
```

```

Dim instance As IPartDoc
Dim BodyType As System.Integer
Dim BVisibleOnly As System.Boolean
Dim value As EnumBodies2
 
value = instance.EnumBodies3(BodyType, BVisibleOnly)
```

```

EnumBodies2 EnumBodies3( 
   System.int BodyType,
   System.bool BVisibleOnly
)
```

```

EnumBodies2^ EnumBodies3( 
   System.int BodyType,
   System.bool BVisibleOnly
) 
```

#### Parameters

*BodyType*
:   Type of body as defined in [swBodyType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBodyType_e.html)

*BVisibleOnly*
:   True gets only visible bodies, false gets all bodies

#### Return Value

[Enumerated list of bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumBodies2.md)

Remarks

To use the enumerated list, see [IEnumBodies2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumBodies2.md) functions.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)  
[IPartDoc::EnumRelatedBodies2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~EnumRelatedBodies2.md)  
[IPartDoc::EnumRelatedSectionedBodies2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~EnumRelatedSectionedBodies2.md)  
[IPartDoc::GetRelatedBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetRelatedBodies.md)  
[IPartDoc::GetRelatedSectionedBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetRelatedSectionedBodies.md)  
[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)
