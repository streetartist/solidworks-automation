# GetLastFeatureAdded Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetLastFeatureAdded`

Gets the last feature added to the model.
Gets the last feature added to the model.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetLastFeatureAdded() As Feature
```

```

Dim instance As IModelDocExtension
Dim value As Feature
 
value = instance.GetLastFeatureAdded()
```

```

Feature GetLastFeatureAdded()
```

```

Feature^ GetLastFeatureAdded(); 
```

#### Return Value

[Feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

This method can access subfeature types such as mates, drawing views, and so on. For example, if you just added the first coincident mate to MateGroup, then IModelDocExtension::GetLastFeatureAdded will return Coincident1. [IModelDoc2::FeatureByPositionReverse](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FeatureByPositionReverse.md) and [IModelDoc2::IFeatureByPositionReverse](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IFeatureByPositionReverse.md) will return MateGroup.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)
