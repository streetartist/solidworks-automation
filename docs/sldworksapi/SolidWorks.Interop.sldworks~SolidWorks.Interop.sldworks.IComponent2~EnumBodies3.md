# EnumBodies3 Method (IComponent2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~EnumBodies3`

Gets the bodies in the component in a multibody part.
Gets the bodies in the component in a multibody part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function EnumBodies3( _
   ByVal BodyType As System.Integer, _
   ByVal VisibleOnly As System.Boolean _
) As EnumBodies2
```

```

Dim instance As IComponent2
Dim BodyType As System.Integer
Dim VisibleOnly As System.Boolean
Dim value As EnumBodies2
 
value = instance.EnumBodies3(BodyType, VisibleOnly)
```

```

EnumBodies2 EnumBodies3( 
   System.int BodyType,
   System.bool VisibleOnly
)
```

```

EnumBodies2^ EnumBodies3( 
   System.int BodyType,
   System.bool VisibleOnly
) 
```

#### Parameters

*BodyType*
:   Type of body as defined by [swBodyType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBodyType_e.html)

*VisibleOnly*
:   True to get visible bodies only, false to get all bodies

#### Return Value

[Enumerated list of bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumBodies2.md)

Remarks

This method only supports solid and sheet (surface) types.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IComponent2::EnumRelatedBodies Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~EnumRelatedBodies.md)  
[IComponent2::EnumSectionedBodies Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~EnumSectionedBodies.md)  
[IComponent2::GetBodies3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetBodies3.md)  
[IComponent2::GetBody Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetBody.md)  
[IComponent2::IGetBody Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetBody.md)  
[IPartDoc::EnumBodies3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~EnumBodies3.md)
