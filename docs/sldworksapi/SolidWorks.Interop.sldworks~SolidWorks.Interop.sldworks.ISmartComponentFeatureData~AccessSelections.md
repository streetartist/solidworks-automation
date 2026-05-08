# AccessSelections Method (ISmartComponentFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISmartComponentFeatureData~AccessSelections`

Gains access to the selection lists on the PropertyManager page of a Smart Component.
Gains access to the selection lists on the PropertyManager page of a Smart Component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AccessSelections( _
   ByVal ShowPMP As System.Boolean _
) As System.Boolean
```

```

Dim instance As ISmartComponentFeatureData
Dim ShowPMP As System.Boolean
Dim value As System.Boolean
 
value = instance.AccessSelections(ShowPMP)
```

```

System.bool AccessSelections( 
   System.bool ShowPMP
)
```

```

System.bool AccessSelections( 
   System.bool ShowPMP
) 
```

#### Parameters

*ShowPMP*
:   True to display the PropertyManager page, false to not (see **Remarks**)

#### Return Value

True if the selections where successfully accessed, false if not

Remarks

ShowPMP only controls the display of the PropertyManager page. This method allows access to the PropertyManager page selection lists regardless of whether the PropertyManager page is displayed. The selection lists have marks as defined in [swSmartComponentSelectionTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSmartComponentSelectionTypes_e.html).

This method opens the training assembly in which this Smart Component is defined.

**To delete a feature or component from a Smart Component:**

1. Open the Smart Component in SOLIDWORKS.
2. Call [IFeature::GetDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDefinition.md) on the "Smart Feature" to get the [ISmartComponentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISmartComponentFeatureData.md) object.
3. Call this method to open the training assembly of the Smart Component.
4. Call [ISldWorks::ActiveDoc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ActiveDoc.md) to set an assembly document variable.
5. To get a specific feature or component, call [ISelectionMgr::GetSelectedObject6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObject6.md)(index, mark), where mark is defined in [swSmartComponentSelectionTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSmartComponentSelectionTypes_e.html) and index is the position of the item in the selection list.
6. Select an already selected feature or component to delete it from its selection list. If the object returned by ISelectionMgr::GetSelectedObject6 is a:

   - feature, call [IFeature::Select2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Select2.md) to delete that feature from the feature selection list.
   - component, call [IComponent2::Select4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Select4.md) to delete that component from the component selection list.
7. Close the training assembly and release access to the selection lists.

**To insert a feature or component into a Smart Component:**

1. Open the Smart Component in SOLIDWORKS.
2. Call [IFeature::GetDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDefinition.md) on the "Smart Feature" to get the [ISmartComponentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISmartComponentFeatureData.md) object.
3. Call this method to open the training assembly of the Smart Component.
4. Call [ISldWorks::ActiveDoc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ActiveDoc.md) to point to the training assembly.
5. Call [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to specify the feature or component you want to insert, setting Mark to an option in [swSmartComponentSelectionTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSmartComponentSelectionTypes_e.html).
6. Close the training assembly and release access to the selection lists.

**To close the training assembly and release access to the selection lists on the PropertyManager page:**

- Call [ISmartComponentFeatureData::ReleaseSelectionAccess](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISmartComponentFeatureData~ReleaseSelectionAccess.md) if you did not insert or delete features and components.
- Call [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.md) or [IFeature::IModifyDefinition2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IModifyDefinition2.md) to rebuild the Smart Component if you inserted or deleted features and components.

Example

[Delete Smart Feature (C#)](Delete_Smart_Feature_Example_CSharp.htm)  
[Delete Smart Feature (VB.NET)](Delete_Smart_Feature_Example_VBNET.htm)  
[Delete Smart Feature (VBA)](Delete_Smart_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISmartComponentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISmartComponentFeatureData.md)  
[ISmartComponentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISmartComponentFeatureData_members.md)
