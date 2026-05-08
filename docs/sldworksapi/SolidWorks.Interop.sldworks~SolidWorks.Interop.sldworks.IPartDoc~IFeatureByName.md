# IFeatureByName Method (IPartDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IFeatureByName`

Gets the named feature in the part.
Gets the named feature in the part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IFeatureByName( _
   ByVal Name As System.String _
) As Feature
```

```

Dim instance As IPartDoc
Dim Name As System.String
Dim value As Feature
 
value = instance.IFeatureByName(Name)
```

```

Feature IFeatureByName( 
   System.string Name
)
```

```

Feature^ IFeatureByName( 
   System.String^ Name
) 
```

#### Parameters

*Name*
:   Name of feature

#### Return Value

[Feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)  
[IPartDoc::IFeatureById Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IFeatureById.md)  
[IPartDoc::FeatureByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~FeatureByName.md)  
[IPartDoc::FeatureById Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~FeatureById.md)
