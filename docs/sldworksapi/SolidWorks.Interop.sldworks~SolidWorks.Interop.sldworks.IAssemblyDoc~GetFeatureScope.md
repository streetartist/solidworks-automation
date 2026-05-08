# GetFeatureScope Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetFeatureScope`

Gets the components affected by this feature.
Gets the components affected by this feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFeatureScope( _
   ByVal FeatureIn As Feature _
) As System.Object
```

```

Dim instance As IAssemblyDoc
Dim FeatureIn As Feature
Dim value As System.Object
 
value = instance.GetFeatureScope(FeatureIn)
```

```

System.object GetFeatureScope( 
   Feature FeatureIn
)
```

```

System.Object^ GetFeatureScope( 
   Feature^ FeatureIn
) 
```

#### Parameters

*FeatureIn*
:   [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

#### Return Value

Array of [components](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) affected by this feature

Remarks

Feature scope information is only provided if the assembly is opened in its own window.

This method gets both the components affected and potentially affected by this feature. Thus, not all of the components in this list are necessarily affected by this feature.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::IGetFeatureScope Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IGetFeatureScope.md)  
[IAssemblyDoc::AddToFeatureScope Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddToFeatureScope.md)  
[IAssemblyDoc::GetFeatureScopeCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetFeatureScopeCount.md)  
[IAssemblyDoc::UpdateFeatureScope Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~UpdateFeatureScope.md)
