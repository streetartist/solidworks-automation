# ReorderFeature Method (IModelDocExtension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ReorderFeature`

Obsolete. Superseded by IModelDocExtension::ReorderFeature2.
Obsolete. Superseded by [IModelDocExtension::ReorderFeature2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ReorderFeature2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ReorderFeature( _
   ByVal FeatureToMove As System.String, _
   ByVal TargetFeature As System.String, _
   ByVal MoveLocation As System.Integer _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim FeatureToMove As System.String
Dim TargetFeature As System.String
Dim MoveLocation As System.Integer
Dim value As System.Boolean
 
value = instance.ReorderFeature(FeatureToMove, TargetFeature, MoveLocation)
```

```

System.bool ReorderFeature( 
   System.string FeatureToMove,
   System.string TargetFeature,
   System.int MoveLocation
)
```

```

System.bool ReorderFeature( 
   System.String^ FeatureToMove,
   System.String^ TargetFeature,
   System.int MoveLocation
) 
```

#### Parameters

*FeatureToMove*
:   Name of feature to move

*TargetFeature*
:   Name of feature before or after which to move FeatureToMove; valid only if MoveLocation is [swMoveLocation\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMoveLocation_e.html).swMoveAfter

    - or -

    Name of folder; valid only if MoveLocation is swMoveLocation\_e.swMoveToFolder

*MoveLocation*
:   Move type as defined by [swMoveLocation\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMoveLocation_e.html)

#### Return Value

True if feature moved successfully, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IPartDoc::ReorderFeature Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ReorderFeature.md)  
[IAssemblyDoc::ReorderComponents Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ReorderComponents.md)
