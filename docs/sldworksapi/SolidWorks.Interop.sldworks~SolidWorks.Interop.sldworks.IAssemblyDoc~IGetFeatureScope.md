# IGetFeatureScope Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IGetFeatureScope`

Gets the components affected by this feature.
Gets the components affected by this feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetFeatureScope( _
   ByVal FeatureIn As Feature, _
   ByVal NumComponents As System.Integer _
) As Component2
```

```

Dim instance As IAssemblyDoc
Dim FeatureIn As Feature
Dim NumComponents As System.Integer
Dim value As Component2
 
value = instance.IGetFeatureScope(FeatureIn, NumComponents)
```

```

Component2 IGetFeatureScope( 
   Feature FeatureIn,
   System.int NumComponents
)
```

```

Component2^ IGetFeatureScope( 
   Feature^ FeatureIn,
   System.int NumComponents
) 
```

#### Parameters

*FeatureIn*
:   [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

*NumComponents*
:   Number of components affected by this feature

#### Return Value

Array of [components](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) of size NumComponents

Remarks

Feature scope information is only provided if the assembly is opened in its own window.

COM users must call [IAssemblyDoc::GetFeatureScopeCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetFeatureScopeCount.md) before calling this method.

This method gets both the components affected and potentially affected by this feature. Thus, not all of the components in this list are necessarily affected by this feature.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::GetFeatureScope Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetFeatureScope.md)  
[IAssemblyDoc::AddToFeatureScope Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddToFeatureScope.md)  
[IAssemblyDoc::GetFeatureScope Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetFeatureScope.md)  
[IAssemblyDoc::GetFeatureScopeCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetFeatureScopeCount.md)  
[IAssemblyDoc::UpdateFeatureScope Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~UpdateFeatureScope.md)
