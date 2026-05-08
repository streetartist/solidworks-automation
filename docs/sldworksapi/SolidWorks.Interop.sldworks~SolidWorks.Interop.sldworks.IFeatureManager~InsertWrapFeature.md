# InsertWrapFeature Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertWrapFeature`

Obsolete. Superseded by IFeatureManager::InsertWrapFeature2.
Obsolete. Superseded by [IFeatureManager::InsertWrapFeature2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertWrapFeature2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertWrapFeature( _
   ByVal Type As System.Integer, _
   ByVal Thickness As System.Double, _
   ByVal ReverseDir As System.Boolean _
) As Feature
```

```

Dim instance As IFeatureManager
Dim Type As System.Integer
Dim Thickness As System.Double
Dim ReverseDir As System.Boolean
Dim value As Feature
 
value = instance.InsertWrapFeature(Type, Thickness, ReverseDir)
```

```

Feature InsertWrapFeature( 
   System.int Type,
   System.double Thickness,
   System.bool ReverseDir
)
```

```

Feature^ InsertWrapFeature( 
   System.int Type,
   System.double Thickness,
   System.bool ReverseDir
) 
```

#### Parameters

*Type*
:   Type of wrap as defined in [swWrapSketchType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swWrapSketchType_e.html)

*Thickness*
:   Thickness; 0.00001 (thinnest) - 10000 (thickest)

*ReverseDir*
:   True to reverse the direction of the wrap, false to not

#### Return Value

Wrap [feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

Use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) and these values to mark these selections:

- 1 = Face on which to place the wrap feature

- 2 = Pull direction if Type is swWrapSketchType\_e.swWrapSketchType\_Emboss or swWrapSketchType\_e.swWrapSketchType\_Engrave
- 4 = 2D sketch of wrap feature; 3D sketches are invalid

Example

[Change Wrap Feature Face (C#)](Change_Wrap_Feature_Face_Example_CSharp.htm)  
[Change Wrap Feature Face (VB.NET)](Change_Wrap_Feature_Face_Example_VBNET.htm)  
[Change Wrap Feature Face (VBA)](Change_Wrap_Feature_Face_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IWrapSketchFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWrapSketchFeatureData.md)
