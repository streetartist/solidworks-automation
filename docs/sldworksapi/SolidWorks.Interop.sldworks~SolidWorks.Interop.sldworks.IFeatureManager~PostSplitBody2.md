# PostSplitBody2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PostSplitBody2`

Creates a Split feature.
Creates a Split feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function PostSplitBody2( _
   ByVal BodiesToMark As System.Object, _
   ByVal ConsumeCut As System.Boolean, _
   ByVal Origins As System.Object, _
   ByVal SavePaths As System.Object, _
   ByVal OverrideTemplateName As System.String _
) As System.Object
```

```

Dim instance As IFeatureManager
Dim BodiesToMark As System.Object
Dim ConsumeCut As System.Boolean
Dim Origins As System.Object
Dim SavePaths As System.Object
Dim OverrideTemplateName As System.String
Dim value As System.Object
 
value = instance.PostSplitBody2(BodiesToMark, ConsumeCut, Origins, SavePaths, OverrideTemplateName)
```

```

System.object PostSplitBody2( 
   System.object BodiesToMark,
   System.bool ConsumeCut,
   System.object Origins,
   System.object SavePaths,
   System.string OverrideTemplateName
)
```

```

System.Object^ PostSplitBody2( 
   System.Object^ BodiesToMark,
   System.bool ConsumeCut,
   System.Object^ Origins,
   System.Object^ SavePaths,
   System.String^ OverrideTemplateName
) 
```

#### Parameters

*BodiesToMark*
:   Array of bodies to mark for the split operation

*ConsumeCut*
:   True to remove the bodies from the part, false to not

*Origins*
:   Array of origins of the bodies to save

*SavePaths*
:   Array of paths and filenames of the part documents to which to save BodiesToMark

*OverrideTemplateName*
:   Path and filename of the part or assembly template that overrides the default (see **Remarks**)

#### Return Value

Split [feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

To create a Split feature:

1. Select the entities to use to split the part into multiple bodies.
2. Call [IFeatureManager::PreSplitBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PreSplitBody.md) to get all of the bodies created by splitting the part.
3. Call this method to create the Split feature.

The size of the BodiesToMark, Origins, and SavePaths arrays must be equal and greater than 0. If you pass an empty path and filename for a body, then that body is only marked, is not saved to a separate part document, and remains with the original part.

OverrideTemplateName overrides the default part or assembly template that is specified in **Tools > Options > System Options > File Locations**. The template is applied to all new part or assembly files created during the split operation.

To find out whether the bodies in a Split feature are consumed, use [ISplitBodyFeatureData::Consume](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~Consume.md).

[IFeature::GetTypeName2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetTypeName2.md) and [IFeature::GetTypeName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetTypeName.md) return:

- **Split** for a feature that was created by splitting a part into multiple parts by using either this method or the **Split** feature in the user interface. You can access a split-body feature's data using [ISplitBodyFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData.md).
- **SplitBody** for a body created by splitting a part and saving the body to a part. You cannot access the data of a split body saved to a part.

Example

[Create Split Feature (VBA)](Create_Split-body_Feature_Example_VB.htm)  
[Create Split Feature (VB.NET)](Create_Split-body_Feature_Example_VBNET.htm)  
[Create Split Feature (C#)](Create_Split-body_Feature_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[ISplitBodyFeatureData::GetSplitBodies Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~GetSplitBodies.md)  
[ISplitBodyFeatureData::SetSplitBodies2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~SetSplitBodies2.md)
