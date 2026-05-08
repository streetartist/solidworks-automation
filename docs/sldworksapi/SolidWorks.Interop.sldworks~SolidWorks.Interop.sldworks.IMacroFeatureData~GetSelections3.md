# GetSelections3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetSelections3`

Gets the selected objects for the macro feature.
Gets the selected objects for the macro feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub GetSelections3( _
   ByRef Objects As System.Object, _
   ByRef ObjectTypes As System.Object, _
   ByRef SelMarks As System.Object, _
   ByRef DrViews As System.Object, _
   ByRef ComponentXForms As System.Object _
) 
```

```

Dim instance As IMacroFeatureData
Dim Objects As System.Object
Dim ObjectTypes As System.Object
Dim SelMarks As System.Object
Dim DrViews As System.Object
Dim ComponentXForms As System.Object
 
instance.GetSelections3(Objects, ObjectTypes, SelMarks, DrViews, ComponentXForms)
```

```

void GetSelections3( 
   out System.object Objects,
   out System.object ObjectTypes,
   out System.object SelMarks,
   out System.object DrViews,
   out System.object ComponentXForms
)
```

```

void GetSelections3( 
   [Out] System.Object^ Objects,
   [Out] System.Object^ ObjectTypes,
   [Out] System.Object^ SelMarks,
   [Out] System.Object^ DrViews,
   [Out] System.Object^ ComponentXForms
) 
```

#### Parameters

*Objects*
:   Array of selected objects

*ObjectTypes*
:   Array of selected object types as defined in [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

*SelMarks*
:   Array of marks for the selected objects

*DrViews*
:   Array of [drawing views](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)

*ComponentXForms*
:   Array of [transforms](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md) for the selections' components

Remarks

When a macro feature is inserted in-context and an entity on a different component is selected, you may need to know that component's transform.

If the assembly is the active document, then you can use [IEntity::GetComponent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~GetComponent.md) or [IComponent2::Transform2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Transform2.md) to get the component's transform.

However, if the part for the component is open for editing and a [macro feature is being edited](sldworksapiprogguide.chm::/Macro_Features/Edit_Definition_Function.htm), then you must use IMacroFeatureData::GetSelections3 to get the component's transform. This method returns the transform and the selection. If the selection belongs to the same part as the macro feature, then NULL is returned. See also [Macro Features and Component Transforms](sldworksapiprogguide.chm::/Macro_Features/Macro_Features_and_Component_Transforms.htm).

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Example

[Cut Body in Half Using Macro Feature (VBA)](Cut_Body_in_Half_using_Macro_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.md)  
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.md)  
[IMacroFeatureData::GetSelectionCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetSelectionCount.md)  
[IMacroFeatureData::IGetSelections3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetSelections3.md)  
[IMacroFeatureData::ISetSelections2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~ISetSelections2.md)  
[IMacroFeatureData::SetSelections2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetSelections2.md)
