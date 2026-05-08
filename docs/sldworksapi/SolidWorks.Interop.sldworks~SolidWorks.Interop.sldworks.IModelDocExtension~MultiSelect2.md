# MultiSelect2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~MultiSelect2`

Selects multiple objects and returns the number of objects selected in the model.
Selects multiple objects and returns the number of objects selected in the model.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function MultiSelect2( _
   ByVal Objects As System.Object, _
   ByVal AppendFlag As System.Boolean, _
   ByVal Data As System.Object _
) As System.Integer
```

```

Dim instance As IModelDocExtension
Dim Objects As System.Object
Dim AppendFlag As System.Boolean
Dim Data As System.Object
Dim value As System.Integer
 
value = instance.MultiSelect2(Objects, AppendFlag, Data)
```

```

System.int MultiSelect2( 
   System.object Objects,
   System.bool AppendFlag,
   System.object Data
)
```

```

System.int MultiSelect2( 
   System.Object^ Objects,
   System.bool AppendFlag,
   System.Object^ Data
) 
```

#### Parameters

*Objects*
:   Array of selectable objects:

    - can be the same type of objects (e.g., an array of faces or an array of edges) or different types of objects (e.g., an array of entities of faces and edges )
    - if an object is not selected, then it is ignored

*AppendFlag*
:   True to append the objects to the selection list, false to replace the current selection list with these objects

*Data*
:   [ISelectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData.md) object, Nothing, or null

#### Return Value

Number of objects selected in the model

Remarks

|  |  |
| --- | --- |
| **If using this method to populate...** | **Then...** |
| A selection box in a PropertyManager page | [IPropertyManagerPage2Handler9::OnSubmitSelection](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler9~OnSubmitSelection.md) fires when set to true and [ISelectData::Mark](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData~Mark.md) is set to either a 0 or a non-0 value.    **NOTE**: IPropertyManagerPage2Handler9::OnSubmitSelection only fires when set to true and ISelectData::Mark is set to 0 if using either of the now obsolete [ModelDocExtension::MultiSelect](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~MultiSelect.md) and [IModelDocExtension::IMultiSelect](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IMultiSelect.md) methods. |
| Multiple selection boxes with different multiple selections in a PropertyManager page | Set:   - each selection box's [IPropertyManagerPageSelectionbox::Mark](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~Mark.md) to a different power of two; for example, 1, 2, 4, 8, etc. (Setting a selection box's mark to 0 causes all selections to appear in that selection box and the active selection box.) - ISelectData::Mark and each selection box's IPropertyManagerPageSelectionbox::Mark to the same value. See the examples for details. |

**NOTE:** If an object is already selected with a mark of *x* and you attempt to select the same object again using this method with AppendFlag = true, then that object remains selected with a mark with *x*. Reselecting a previously selected object does not assign a new mark value.

Example

[Select Multiple Objects for Selection Boxes (C#)](Select_Multiple_Objects_for_Selection_Boxes_Example_CSharp.htm)  
[Select Multiple Objects for Selection Boxes (VB.NET)](Select_Multiple_Objects_for_Selection_Boxes_Example_VBNET.htm)  
[Select Multiple Objects for Selection Boxes (VBA)](Select_Multiple_Objects_for_Selection_Boxes_Example_VB.htm)  
[Specify IGES Levels and Values, Then Import IGES File (C#)](Specify_IGES_Levels_and_Values_Then_Import_IGES_File_Example_CSharp.htm)  
[Specify IGES Levels and Values, Then Import IGES File (VB.NET)](Specify_IGES_Levels_and_Values_Then_Import_IGES_File_Example_VBNET.htm)  
[Specify IGES Levels and Values, Then Import IGES File (VBA)](Specify_IGES_Levels_and_Values,_Then_Import_IGES_File_Example_VB.htm)  
[Multiselect Same and Different Objects (C#)](Multiselect_Same and_Different_Objects_Example_CSharp.htm)  
[Multiselect Same and Different Objects (VB.NET)](Multiselect_Same and_Different_Objects_Example_VBNET.htm)  
[Multiselect Same and Different Objects (VBA)](Multiselect_Same and_Different_Objects_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::SelectByID2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md)  
[IModelDocExtension::SelectAll Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectAll.md)  
[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.md)
