# GetFeatureScopeCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetFeatureScopeCount`

Gets the number of components affected by this feature.
Gets the number of components affected by this feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFeatureScopeCount( _
   ByVal FeatureIn As Feature _
) As System.Integer
```

```

Dim instance As IAssemblyDoc
Dim FeatureIn As Feature
Dim value As System.Integer
 
value = instance.GetFeatureScopeCount(FeatureIn)
```

```

System.int GetFeatureScopeCount( 
   Feature FeatureIn
)
```

```

System.int GetFeatureScopeCount( 
   Feature^ FeatureIn
) 
```

#### Parameters

*FeatureIn*
:   [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

#### Return Value

Number of components affected by this feature

Remarks

Call this method before calling [IAssemblyDoc::IGetFeatureScope](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IGetFeatureScope.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::UpdateFeatureScope Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~UpdateFeatureScope.md)  
[IAssemblyDoc::RemoveFromFeatureScope Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~RemoveFromFeatureScope.md)  
[IAssemblyDoc::IGetFeatureScope Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IGetFeatureScope.md)  
[IAssemblyDoc::GetFeatureScope Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetFeatureScope.md)  
[IAssemblyDoc::AddToFeatureScope Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddToFeatureScope.md)  
[IAssemblyDoc::IGetFeatureScope Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IGetFeatureScope.md)
