# MakeSubFeature Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~MakeSubFeature`

Makes a feature become a subfeature of this feature.
Makes a feature become a subfeature of this feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function MakeSubFeature( _
   ByVal SubFeature As Feature _
) As System.Boolean
```

```

Dim instance As IFeature
Dim SubFeature As Feature
Dim value As System.Boolean
 
value = instance.MakeSubFeature(SubFeature)
```

```

System.bool MakeSubFeature( 
   Feature SubFeature
)
```

```

System.bool MakeSubFeature( 
   Feature^ SubFeature
) 
```

#### Parameters

*SubFeature*
:   Pointer to the [feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) to become a subfeature

#### Return Value

True if the feature becomes a subfeature, false if not

Remarks

- This method is not supported in assembly documents.
- This method can only be used to make subfeatures to a macro feature.
- The feature and subfeature must have a parent-child relationship. If the subfeature is a reference plane, then the feature and subfeatures of the feature are the only parents of the subfeature to be inserted.

Example

[Create Macro Feature Subfeature (VBA)](Create_Macro_Feature_Subfeature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.md)  
[IFeature::GetFirstSubFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetFirstSubFeature.md)  
[IFeature::GetNextSubFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetNextSubFeature.md)  
[IFeature::IGetFirstSubFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetFirstSubFeature.md)  
[IFeature::IGetNextSubFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetNextSubFeature.md)
