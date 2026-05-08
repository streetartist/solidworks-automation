# InsertWeldmentTrimFeature Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertWeldmentTrimFeature`

Inserts a weldment trim feature.
Inserts a weldment trim feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertWeldmentTrimFeature( _
   ByVal EndCond As System.Integer _
) As Feature
```

```

Dim instance As IFeatureManager
Dim EndCond As System.Integer
Dim value As Feature
 
value = instance.InsertWeldmentTrimFeature(EndCond)
```

```

Feature InsertWeldmentTrimFeature( 
   System.int EndCond
)
```

```

Feature^ InsertWeldmentTrimFeature( 
   System.int EndCond
) 
```

#### Parameters

*EndCond*
:   End condition as defined by [swSolidworksWeldmentEndCondOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSOLIDWORKSWeldmentEndCondOptions_e.html)

#### Return Value

Pointer to the [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) object

Remarks

Use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) and specify the following marks to select the body, or bodies, to trim and the trimming boundaries:

- 1 = Body or bodies to trim
- 2 = Trimming boundaries (body or face)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IWeldmentTrimExtendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData.md)  
[IFeatureManager::InsertWeldmentTrimFeature2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertWeldmentTrimFeature2.md)
