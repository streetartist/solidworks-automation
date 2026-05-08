# ReorderFeature Method (IPartDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ReorderFeature`

Reorders features and their operations.
Reorders features and their operations.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ReorderFeature( _
   ByVal FeatureToMove As System.String, _
   ByVal MoveAfterFeature As System.String _
) As System.Boolean
```

```

Dim instance As IPartDoc
Dim FeatureToMove As System.String
Dim MoveAfterFeature As System.String
Dim value As System.Boolean
 
value = instance.ReorderFeature(FeatureToMove, MoveAfterFeature)
```

```

System.bool ReorderFeature( 
   System.string FeatureToMove,
   System.string MoveAfterFeature
)
```

```

System.bool ReorderFeature( 
   System.String^ FeatureToMove,
   System.String^ MoveAfterFeature
) 
```

#### Parameters

*FeatureToMove*
:   Name of the feature to move

*MoveAfterFeature*
:   Name of the feature that now precedes the feature in the FeatureManager design tree

#### Return Value

True if successful, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)  
[IPartDoc::FirstFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~FirstFeature.md)  
[IAssemblyDoc::ReorderComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ReorderComponents.md)  
[IModelDocExtension::ReorderFeature Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ReorderFeature.md)
